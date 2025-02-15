from flask import Flask
from controllers.upload import create_upload_blueprint
from repositories.firebase import FirebaseRepository
from services.image import ImageService

app = Flask(__name__)

firebase_repo = FirebaseRepository()
image_service = ImageService()
upload_bp = create_upload_blueprint(firebase_repo, image_service)
app.register_blueprint(upload_bp)

if __name__ == '__main__':
    app.run(debug=True)
