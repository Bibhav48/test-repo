from flask import Flask,render_template
import os

app = Flask(__name__)
@app.route('/notes')
def notes():
    files =[]
    folder_path = "static/notes/physics"
    if os.path.exists(folder_path):
        file_names = sorted(os.listdir(folder_path))
        files = [(i,f.split(".")[0]) for i,f in enumerate(file_names,start=1)]
        links = [f"{folder_path}/{file}" for file in file_names]
        files_phy=zip(files,links)
    return render_template("notes.html", active="notes",files_phy=files_phy)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")