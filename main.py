from flask import *
import bcrypt
from functions import *
import dotenv
import os
from flask_sessions import Session

app = Flask(__name__)
config = dotenv.dotenv_values(".env")
app.secret_key = config["SECRET_KEY"]
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
insert_row("AUTH", {"name": "supermutec", "email": "supermutec@gmail.com", "password": bcrypt.hashpw("BakedPotatoes1234".encode("utf-8"), salt=bcrypt.gensalt())}, "auth.db")
Session()

projects_dat = select_rows("PROJECTS", "data.db")
projects = []

for project in projects_dat:
    project_dat={
        "title": None,
        "description": None,
        "image": None,
        "link": None,
        "slug": None,
    }
    project_dat["title"]=project[0]
    project_dat["description"]=project[1]
    project_dat["image"]=project[2]
    project_dat["link"]=project[3]
    project_dat["slug"]=project[4]
    projects.append(project_dat)
        

def checkSession():
    try:
        email = session["email"]
        return True
    except:
        return False

@app.route("/")
def home():
    return render_template("Pages/Landing.html")

@app.route("/debug")
def debug():
    return render_template("Components/Button.html")
@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        dat = request.form
        email = dat["email"]
        password = dat["password"]
        try:
            db_dat = select_rows("AUTH", "auth.db", {"email": email})
            db_dat = db_dat[0]
            if bcrypt.checkpw(password=password.encode("utf-8"), hashed_password=db_dat[2]):
                flash("You have logged in", "success")
                session["email"] = email
                session["name"] = db_dat[0]
                return redirect(url_for("home"))
            else:
                flash("Wrong Password", "error")
        except:
            flash("Email does not exist, check your members page to see if your email is included", "error")
    return render_template("Pages/Login.html")
@app.route("/projects")
def projects():
    

    return render_template("Pages/Projects.html", projects=projects)


@app.route("/projects/<slug>")
def project_detail(slug):
    project = next((p for p in projects if p["slug"] == slug), None)
    if not project:
        return "Project not found", 404
    
    return render_template("Pages/ProjectDetail.html", project=project)


if __name__ == "__main__":
    app.run(debug=True)
