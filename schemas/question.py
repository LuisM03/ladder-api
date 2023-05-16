def questionSchema(question) -> dict:
  return {
      "id": str(question["_id"]),
      "question": question["question"],
      "answer": question["answer"],
      "category": question["category"]
    }

def questionsSchema(questions) -> list:
  return [questionSchema(question) for question in questions]