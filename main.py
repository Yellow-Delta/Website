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

session = Session()

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
        password = dat["pass"]
        try:
            db_dat = select_rows("AUTH", "auth.db", {"email": email})
            db_dat = db_dat[0]
            if bcrypt.checkpw(password=password.encode("utf-8"), hashed_password=db_dat[2]):
                flash("You have logged in", "success")
                return redirect(url_for(home))
            else:
                flash("Wrong Password", "error")
        except:
            flash("Email does not exist, check your members page to see if your email is included", "error")
    return render_template("Pages/Login.html")
if __name__ == "__main__":
    app.run(debug=True)
