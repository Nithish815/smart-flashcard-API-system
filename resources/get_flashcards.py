from flask import request
from flask_restful import Resource
from models.flashcard import Flashcard, db
from sqlalchemy import func
import random

class GetFlashcardsBySubject(Resource):
    def get(self):
        student_id = request.args.get('student_id')
        limit = request.args.get('limit', type=int)

        if not student_id or not limit:
            return {"message": "student_id and limit are required as query parameters"}, 400

        # Get unique subjects for the student
        subjects = db.session.query(Flashcard.subject)\
            .filter_by(student_id=student_id)\
            .distinct().all()
        subjects = [s[0] for s in subjects]

        flashcards = []
        for subject in subjects:
            card = Flashcard.query.filter_by(student_id=student_id, subject=subject)\
                                  .order_by(func.random())\
                                  .first()
            if card:
                flashcards.append(card)

        # Fill up remaining limit
        if len(flashcards) < limit:
            additional_needed = limit - len(flashcards)
            additional_cards = Flashcard.query.filter_by(student_id=student_id)\
                                              .filter(Flashcard.id.notin_([f.id for f in flashcards]))\
                                              .order_by(func.random())\
                                              .limit(additional_needed)\
                                              .all()
            flashcards.extend(additional_cards)

        # Shuffle
        random.shuffle(flashcards)

        return [
            {
                "question": card.question,
                "answer": card.answer,
                "subject": card.subject
            }
            for card in flashcards[:limit]
        ]
