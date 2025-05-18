from flask import Flask, request, render_template, redirect, url_for
from app.database import db
from werkzeug.utils import secure_filename
from app.utils import validate
import bleach
import os

UPLOAD_FOLDER = 'static/uploads'
DEBUG_POST = True

app = Flask(__name__)

app.secret_key = "m3g4_s3cr3t_k3y"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000


def sanitize_input(string):
    if not string or not isinstance(string, str):
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
        activity_form = request.form
        if DEBUG_POST: 
            print(activity_form)

        error_list = []
        # Where
        region = activity_form['region']
        commune = activity_form['commune']
        sector = bleach.clean(activity_form['sector'])

        if not validate.valid_location(region, commune):
            error_list.append("Ubicación inválida")
        if not validate.valid_sector(sector):
            error_list.append("Sector inválido")
        
        # Who
        name = bleach.clean(activity_form['name'])
        email = activity_form['email']
        phone = activity_form['phone']

        contactos = [
            activity_form['whatsapp-id'],
            activity_form['email-id'],
            activity_form['phone-id'],
            activity_form['facebook-id'],
            activity_form['twitter-id'],
        ]
        if not validate.valid_name(name):
            error_list.append("Nombre inválido")
        if not validate.valid_email(email):
            error_list.append("Email inválido")
        if not validate.valid_phone(phone):
            error_list.append("Teléfono inválido")

        # When 
        start_date = activity_form['start_date']
        end_date = activity_form['end_date']
        if not validate.valid_date(start_date):
            error_list.append("Fecha de término inválida")
        if not validate.valid_end_date(start_date, end_date):
            error_list.append("Fecha de término inválida")
    
        
        # What
        topic = activity_form['topic']
        other_topic = activity_form['other_topic']
        description = activity_form['description']

        if validate.valid_topic(topic, other_topic):
            error_list.append("Tema inválido")
        if validate.valid_description(description):
            error_list.append("Descripción inválida")
        
        activity_files = 
        if DEBUG_POST:
            print(request.files)

        # Files

        photos = [
            request.files.get("photo0"),
            request.files.get("photo1"),
            request.files.get("photo2"),
            request.files.get("photo3"),
            request.files.get("photo4")
        ]
        for photo in photos:
            if photo and photo.filename:
                filename = secure_filename(photo.filename)
                
        if not validate.valid_photos(photos):
            error_list.append("Archivos invalidos")

        if error_list:
            error = "Error en el formulario: " + ", ".join(error_list)
            render_template('agregar-actividad.html', error=error)

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
        
        db_photos = db_objects["fotos"]
        for db_photo in db_photos:
            if DEBUG_POST:
                print(db_photo)
            filename = secure_filename(db_photo.nombre_archivo)
            base_path = os.path.join(app.config['UPLOAD_FOLDER'], str(db_photo.actividad_id))
            if not os.path.exists(base_path):
                os.makedirs(base_path)
            db_photo.ruta_archivo = os.path.join(base_path, filename)
            db_photo.save()

        return redirect(url_for('index'))
                        
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
