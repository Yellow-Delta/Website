from flask import *
import sys
import os
import dotenv
import bcrypt

from functions import *
 
admin = Blueprint("admin", __name__)
config = dotenv.dotenv_values(".env")

admin_key=config["ADMIN_KEY"]
admin_key = bcrypt.hashpw(admin_key.encode("UTF-8"), bcrypt.gensalt())

# Format: {title, description}
@admin.route("/api/admin/project/add", methods=["POST"])
def add_project():
    try:
        input_key=request.form.get("admin_key")
        if bcrypt.checkpw(input_key.encode("UTF-8"), admin_key):
            title = request.form.get("title")
            description = request.form.get("description")
            image = request.form.get("image")
            link = request.form.get("link")
            slug = request.form.get("slug")
        else:
            return jsonify(error="403 Unauthorized", success=False)

        return jsonify(error=None, success=True)
    except Exception as e:
        return jsonify(
            error=str(e), success=False
        )
    
#Return Format: {error, success}