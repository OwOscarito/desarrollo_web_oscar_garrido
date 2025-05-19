from flask import Flask, request, render_template, redirect, url_for
from app.database import db
from app.utils import validate
import bleach
from datetime import datetime
import pathlib

UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)

app.secret_key = "m3g4_s3cr3t_k3y"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000


def sanitize_input(string):
    if None or not string or not isinstance(string, str):
        return string
    return bleach.clean(string)

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
        if sector:
            if not validate.valid_sector(sector):
                error_list.append("Sector inválido")
        else:
            sector = None

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
        if phone:
            if not validate.valid_phone(phone):
                error_list.append("Teléfono inválido")
        else:
            phone = None

        for i in range(len(contact_checks)):
            if not contact_checks[i]:
                contact_ids[i] = None
            elif contact_checks[i] == "on" and not validate.valid_contact(contact_ids[i]):
                error_list.append("Contacto inválido")

        contacts = []
        for i in range(len(contact_checks)):
            if contact_checks[i] == "on":
                contacts.append((CONTACTS[i], contact_ids[i]))
        print(contacts)

        # When 
        start_date = request.form.get('start-datetime-input')
        end_checkbox = request.form.get('end-checkbox')
        end_date = request.form.get('end-datetime-input')

        if not validate.valid_date(start_date):
            error_list.append("Fecha de inicio inválida")
        if end_checkbox == "on":
            if not validate.valid_end_date(start_date, end_date):
                error_list.append("Fecha de término inválida")
        else:
            end_date = None

        print(f"when: {start_date}, {end_date}")


        # What
        topic = request.form.get('select-topic').lower()
        other_topic = sanitize_input(request.form.get('other-topic'))
        description = sanitize_input(request.form.get('description'))
        print(f"what: {topic}, {other_topic}, {description}")

        if topic == "otro":
            if not validate.valid_other_topic(other_topic):
                error_list.append("Tema inválido")
        else:
            other_topic = None
            if not validate.valid_topic(topic):
                error_list.append("Tema inválido")
     
        if description:
            if not validate.valid_description(description):
                error_list.append("Descripción inválida")
        else:
            description = None

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


        base_path = db.create_activity(
            comuna_id=commune,
            nombre=name,
            email=email,
            dia_hora_inicio=datetime.strptime(start_date, '%Y-%m-%dT%H:%M'),
            uploads_folder=app.config['UPLOAD_FOLDER'],
            sector=sector,
            celular=phone,
            dia_hora_termino=datetime.strptime(end_date, '%Y-%m-%dT%H:%M') if end_checkbox == "on" else None,
            descripcion=description,
            tema=topic,
            glosa_otro=other_topic,
            contactos = contacts,
            fotos = photos,
        )


        path = pathlib.Path('app/static').joinpath(str(base_path))
        path.mkdir(parents=True, exist_ok=True)
        for photo in photos:
            photo.save(path.joinpath(photo.filename))
        print(f"saved in {path}")

        return redirect(url_for('listado'))
                        
    if request.method == "GET":
        return render_template('agregar-actividad.html')

@app.route('/actividad/<int:id>',methods=["GET"])
@app.route('/actividad',methods=["GET"])
def actividad(id=None):
    if not id:
        return redirect(url_for('listado'))
    
    activity_db = db.get_activity_by_id(id)
    if not activity_db:
        return redirect(url_for('listado'))
    
    commune_db = db.get_commune_by_id(activity_db.comuna_id)
    region_db = db.get_region_by_id(commune_db.region_id)

    contactos_db = db.get_contacts_by_activity_id(activity_db.id)
    contacts = [{"name": contact.nombre.name.capitalize(), "id": contact.identificador} for contact in contactos_db]

    dt_end = activity_db.dia_hora_termino
    if not dt_end:
        dt_end = ""

    topic_db = db.get_topic_by_activity_id(activity_db.id)[0]
    if topic_db.tema.name == "otro":
        topic = topic_db.glosa_otro
    else:
        topic = topic_db.tema.name.capitalize()
    print(topic)
    photos_db = db.get_photos_by_activity_id(activity_db.id)
    photo_paths = [url_for('static', filename=pathlib.Path(photo.ruta_archivo).joinpath(photo.nombre_archivo).as_posix()) for photo in photos_db]
    activity = {
        'id': activity_db.id,
        'commune': commune_db.nombre,
        'region': region_db.nombre,
        'sector': activity_db.sector,
        'start': activity_db.dia_hora_inicio,
        'end': dt_end,

        'name': activity_db.nombre,
        'email': activity_db.email,
        'phone': activity_db.celular,
        'contacts': contacts,

        'description': activity_db.descripcion,

        'topic': topic,
        'photos': photo_paths
    }
    print(activity)
    return render_template('informacion-actividad.html', activity=activity)

@app.route('/listado',methods=["GET"])
def listado():
    activities = []
    for activity in db.get_last_activities(5):
        photos = db.get_photos_by_activity_id(activity.id)
        dt_end = activity.dia_hora_termino
        if not dt_end:
            dt_end = ""
        db_topic = db.get_topic_by_activity_id(activity.id)[0]
        if db_topic.tema.name == "otro":
            topic = db_topic.glosa_otro
        else:
            topic = db_topic.tema.name

        activities.append({
            'id': activity.id,
            'start': activity.dia_hora_inicio,
            'end': dt_end,
            'commune': db.get_commune_by_id(activity.comuna_id).nombre,
            'sector': activity.sector,
            'topic': topic,
            'name': activity.nombre,
            'photo': url_for('static',filename=pathlib.Path(photos[0].ruta_archivo).joinpath(photos[0].nombre_archivo).as_posix())
        })
    print(activities)
    return render_template('listado-actividades.html', activities=activities)

@app.route('/',methods=["GET"])
def index():
    activities = []
    for activity in db.get_last_activities(5):
        photos = db.get_photos_by_activity_id(activity.id)
        dt_end = activity.dia_hora_termino
        if not dt_end:
            dt_end = ""
        db_topic = db.get_topic_by_activity_id(activity.id)[0]
        if db_topic.tema.name == "otro":
            topic = db_topic.glosa_otro
        else:
            topic = db_topic.tema.name.capitalize()

        activities.append({
            'id': activity.id,
            'start': activity.dia_hora_inicio,
            'end': dt_end,
            'commune': db.get_commune_by_id(activity.comuna_id).nombre,
            'sector': activity.sector,
            'topic': topic,
            'photo': url_for('static', filename=pathlib.Path(photos[0].ruta_archivo).joinpath(photos[0].nombre_archivo).as_posix())
        })
    print(activities)
    return render_template('index.html', activities=activities)

if __name__ == "__main__":
    app.run(debug=True)
