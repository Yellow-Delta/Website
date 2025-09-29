from flask import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from functions import *

admin = Blueprint("admin", __name__)


# Format: {title, description}
@admin.route("/api/admin/project/add", methods=["POST"])
def add_project():
    try:
        title = request.form.get("title")
        description = request.form.get("description")
        image = request.form.get("image")
        link = request.form.get("link")
        slug = request.form.get("slug")

        return jsonify(error=None, success=True)
    except Exception as e:
        return jsonify(
            error=str(e), success=False
        )
    
#Return Format: {error, success}