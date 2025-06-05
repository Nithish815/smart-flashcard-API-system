from flask import Flask
from flask_restful import Api
from models.flashcard import db
from resources.flashcard import FlashcardAPI
from resources.get_flashcards import GetFlashcardsBySubject

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
api = Api(app)
api.add_resource(FlashcardAPI, '/flashcard')

api.add_resource(GetFlashcardsBySubject, '/get-subject')

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)