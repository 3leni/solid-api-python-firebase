from flask import Blueprint, request, jsonify
from models.user import User

def create_upload_blueprint(storage, converter):
    upload_bp = Blueprint('upload', __name__)

    @upload_bp.route('/upload', methods=['POST'])
    def upload():
        image_file = request.files.get('image')
        name = request.form.get('name')
        email = request.form.get('email')
        
        pdf_bytes = converter.to_pdf(image_file)
        filename = f"pdfs/{name.replace(' ', '_')}.pdf"
        file_url = storage.upload(pdf_bytes, filename)

        user = User(name=name, email=email, file_url=file_url)
        storage.save_user(user.dict())

        return jsonify({"message": "Archivo subido exitosamente", "file_url": file_url})

    return upload_bp
