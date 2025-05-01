from flask import Flask, request, render_template, redirect, url_for, session
from app.database import db
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = 'static/uploads'

app = Flask(__name__)

app.secret_key = "s3cr3t_k3y"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

@app.route('/base',methods=["GET"])
def base():
    return render_template('base.html')

@app.route('/',methods=["GET"])
def index():
    data = []
    activities = db.get_activities(5)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
