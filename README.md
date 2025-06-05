# Smart Flashcard API (Flask-RESTful)

This is a simple backend API for a Smart Flashcard System that detects the subject of a flashcard based on keywords and allows students to retrieve flashcards by subject.

## 🚀 Features

- Add flashcards (automatically infers subject)
- Retrieve mixed flashcards by subject for a student
- Rule-based subject inference
- SQLite backend
- Built with Flask + Flask-RESTful

## 📁 File Structure
flash/
├── app.py
├── models/
│ └── flashcard.py
├── resources/
│ ├── flashcard.py
│ └── get_flashcards.py
├── requirements.txt
└── README.md

## ⚙️ Installation

```bash
git clone https://github.com/nithish815/smart-flashcard-api-system.git
cd smart-flashcard-api-system
pip install -r requirements.txt
python app.py
