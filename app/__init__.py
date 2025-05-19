from flask import Flask, request, render_template, redirect, url_for
from app.database import db
from app.utils import validate
import bleach
import os

UPLOAD_FOLDER = 'static/uploads'

app = Flask(__name__)

app.secret_key = "m3g4_s3cr3t_k3y"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000


def sanitize_input(string):
    if None or not string or not isinstance(string, str):
        return string
    return bleach.clean(string)

def dict_map(func, d):
    return {k: func(v) for k, v in d.items()}

@app.route('/base',methods=["GET"])
def base():
    return render_template('base.html')

@app.route('/estadisticas',methods=["GET"])
def estadisticas():
    return render_template('estadisticas.html')

@app.route('/agregar',methods=["GET", "POST"])
def agregar():
    if request.method == "POST":
        print(request.form)
        print(request.files)

        error_list = []
        # Where
        region = request.form.get('select-region')
        commune = request.form.get('select-commune')
        sector = sanitize_input(request.form.get('sector'))
        
        print(f"location: {region}, {commune}, {sector}")

        if not validate.valid_location(region, commune):
            error_list.append("Ubicación inválida")
        if not validate.valid_sector(sector):
            error_list.append("Sector inválido")

        # Who
        name = sanitize_input(request.form.get('name'))
        email = request.form.get('email')
        phone = request.form.get('phone')
        CONTACTS = [
            "whatsapp",
            "instagram",
            "telegram",
            "tiktok",
            "x",
            "otro"
        ]
        contact_checks = [
            request.form.get(CONTACTS[0]),
            request.form.get(CONTACTS[1]),
            request.form.get(CONTACTS[2]),
            request.form.get(CONTACTS[3]),
            request.form.get(CONTACTS[4]),
            request.form.get(CONTACTS[5])
        ]
        contact_ids = [
            sanitize_input(request.form.get(f'{CONTACTS[0]}-id')),
            sanitize_input(request.form.get(f'{CONTACTS[1]}-id')),
            sanitize_input(request.form.get(f'{CONTACTS[2]}-id')),
            sanitize_input(request.form.get(f'{CONTACTS[3]}-id')),
            sanitize_input(request.form.get(f'{CONTACTS[4]}-id')),
            sanitize_input(request.form.get(f'{CONTACTS[5]}-id')),
        ]
        print(f'who: {name}, {email}, {phone}, {contact_checks}, {contact_ids}')

        if not validate.valid_name(name):
            error_list.append("Nombre inválido")
        if not validate.valid_email(email):
            error_list.append("Email inválido")
        if not validate.valid_phone(phone):
            error_list.append("Teléfono inválido")

        for i in range(len(contact_checks)):
            if not contact_checks[i]:
                contact_ids[i] = None
            elif contact_checks[i] == "on" and not validate.valid_contact(contact_ids[i]):
                error_list.append("Contacto inválido")

        # When 
        start_date = request.form.get('start-datetime')
        end_date = request.form.get('end-datetime')
        if not validate.valid_date(start_date):
            error_list.append("Fecha de inicio inválida")
        if not validate.valid_end_date(start_date, end_date):
            error_list.append("Fecha de término inválida")

        print(f"when: {start_date}, {end_date}")


        # What
        topic = request.form.get('select-topic').lower()
        other_topic = request.form.get('other_topic')
        description = request.form.get('description')
        print(f"what: {topic}, {other_topic}, {description}")

        if not validate.valid_topic(topic, other_topic):
            error_list.append("Tema inválido")
        if not validate.valid_description(description):
            error_list.append("Descripción inválida")

        # Files
        photos = [
            request.files.get("photo0"),
            request.files.get("photo1"),
            request.files.get("photo2"),
            request.files.get("photo3"),
            request.files.get("photo4")
        ]

        photos = [photo for photo in photos if photo and photo.filename]

        if not validate.valid_photos(photos):
            error_list.append("Archivos invalidos")

        if error_list:
            error = ", ".join(error_list)
            print(error)
            return render_template('agregar-actividad.html', error=error)

        print("no error")

        db_objects = db.create_activity(
            comuna_id=commune,
            nombre=name,
            email=email,
            dia_hora_inicio=start_date,
            sector=sector,
            celular=phone,
            dia_hora_termino=end_date,
            uploads_folder=app.config['UPLOAD_FOLDER'],
        )
        
        db_photos:list[db.Foto] = db_objects["fotos"]
        for photo, db_photo in photos, db_photos:
            if photo and db_photo:
                path = os.path.join(db_photo.ruta_archivo, db_photo.nombre_archivo)
                if not os.path.exists(path):
                    os.makedirs(path)
                photo.save(path)

        return redirect(url_for('listado'))
                        
    if request.method == "GET":
        return render_template('agregar-actividad.html')

@app.route('/actividad/<int:id>',methods=["GET"])
@app.route('/actividad',methods=["GET"])
def actividad(id=None):
    if not id:
        return redirect(url_for('listado'))
    
    actividad = db.get_activity_by_id(id)
    if not actividad:
        return redirect(url_for('listado'))
    return render_template('informacion-actividad.html', actividad=actividad)

@app.route('/listado',methods=["GET"])
def listado():
    actividades = []
    #for actividad in db.get_activities(5):
    #    actividades.append(actividad)
    return render_template('listado-actividades.html', actividades=actividades)

@app.route('/',methods=["GET"])
def index():
    actividades = []
    for actividad in db.get_activities(5):
        actividades.append({
            'id': actividad.id,
            'nombre': actividad.nombre,
            'descripcion': actividad.descripcion,
            'fecha_inicio': actividad.fecha_inicio,
            'fecha_fin': actividad.fecha_fin,
            'region': actividad.region,
            'comuna': actividad.comuna,
            'sector': actividad.sector,
            'foto': actividad.foto,
        })
    return render_template('index.html', actividades=actividades)

if __name__ == "__main__":
    app.run(debug=True)
