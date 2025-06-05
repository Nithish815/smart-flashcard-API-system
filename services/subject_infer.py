def infer_subject(text):
    subject_keywords = {
        "Physics": ["force", "acceleration", "velocity", "gravity", "newton", "mass"],
        "Biology": ["photosynthesis", "cell", "organism", "plant", "animal", "biology"],
        "Chemistry": ["atom", "molecule", "reaction", "acid", "base", "chemical"],
        "Math": ["algebra", "equation", "geometry", "calculus", "integral", "derivative"],
        "History": ["war", "empire", "ancient", "revolution", "king", "history"]
    }

    text = text.lower()
    for subject, keywords in subject_keywords.items():
        if any(keyword in text for keyword in keywords):
            return subject
    return "General"
