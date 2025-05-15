from flask import Flask, request, render_template, redirect, url_for
from app.database import db
from werkzeug.utils import secure_filename
from app.utils import validate

UPLOAD_FOLDER = 'static/uploads'

app = Flask(__name__)

app.secret_key = "s3cr3t_k3y"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

@app.route('/base',methods=["GET"])
def base():
    return render_template('base.html')

@app.route('/estadisticas',methods=["GET"])
def estadisticas():
    return render_template('estadisticas.html')

@app.route('/agregar',methods=["GET", "POST"])
def agregar():
    if request.method == "POST":
        req = request.form
        error = ""
        render_template('agregar-actividad.html', error=error)
        return redirect(url_for('index'))
                        
    if request.method == "GET":
        return render_template('agregar-actividad.html')

    return render_template('agregar-actividad.html')

@app.route('/actividad/<int:id>',methods=["GET"])
@app.route('/actividad',methods=["GET"])
def actividad(id=None):
    if not id:
        return redirect(url_for('listado'))
    
    actividad = db.get_activity(id)
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
    #for actividad in db.get_activities(5):
    #    actividades.append(actividad)
    return render_template('index.html', actividades=actividades)

if __name__ == "__main__":
    app.run(debug=True)
