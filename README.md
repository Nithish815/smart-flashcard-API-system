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
## API Endpoints

POST /flashcard

{
  "student_id": "stu008",
  "question": "What is Newton's Third Law?",
  "answer": "For every action, there is an equal and opposite reaction."
}

Response:

{
  "message": "Flashcard added successfully",
  "subject": "Physics"
}


## This is the Output screenshot from postman
![image](https://github.com/user-attachments/assets/d9e84b96-cfdd-42d8-a3a4-d965d965e811)


GET /http://127.0.0.1:5000/get-subject?student_id=stu001&limit=5

Response:

[
  {
    "question": "What is Newton's Second Law?",
    "answer": "Force equals mass times acceleration",
    "subject": "Physics"
  }
]

## This is the Output screenshot from postman
![image](https://github.com/user-attachments/assets/e3f03db4-a4d4-4a10-9ade-0869f03d837d)
