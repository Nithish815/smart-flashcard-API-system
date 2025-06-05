from flask_restful import Resource, reqparse
from models.flashcard import Flashcard, db
from services.subject_infer import infer_subject

parser = reqparse.RequestParser()
parser.add_argument('student_id', type=str, required=True, help="Student ID is required")
parser.add_argument('question', type=str, required=True, help="Question is required")
parser.add_argument('answer', type=str, required=True, help="Answer is required")

class FlashcardAPI(Resource):
    def post(self):
        args = parser.parse_args()
        subject = infer_subject(args['question'])

        flashcard = Flashcard(
            student_id=args['student_id'],
            question=args['question'],
            answer=args['answer'],
            subject=subject
        )
        db.session.add(flashcard)
        db.session.commit()

        return {
            "message": "Flashcard added successfully",
            "subject": subject
        }, 201
