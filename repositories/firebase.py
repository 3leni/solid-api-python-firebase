from firebase_admin import credentials, storage, firestore, initialize_app
from interfaces.storage import Storage

class FirebaseRepository(Storage):
    def __init__(self):
        cred = credentials.Certificate("firebase_config.json")
        initialize_app(cred, {'storageBucket': 'bucket.appspot.com'})
        self.bucket = storage.bucket()
        self.db = firestore.client()

    def upload(self, file_bytes, filename: str) -> str:
        blob = self.bucket.blob(filename)
        blob.upload_from_file(file_bytes, content_type="application/pdf")
        blob.make_public()
        return blob.public_url

    def save_user(self, user_data: dict) -> None:
        self.db.collection("users").add(user_data)
