from search_database import collection, model
from web_search import search_sports_news


def generate_quiz(sport, difficulty):

    # Search sports facts from ChromaDB
    query = f"{sport} sports facts"

    query_embedding = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=5
    )

    facts = results["documents"][0]

    # Get latest sports news
    news = search_sports_news(
        f"latest {sport} news"
    )

    # Create quiz
    quiz_text = f"""
🏆 AI Sports Quiz Generator

Sport: {sport}
Difficulty: {difficulty}


Question 1:
Which statement is related to {sport}?

A. {facts[0] if len(facts) > 0 else "No information"}
B. {facts[1] if len(facts) > 1 else "No information"}
C. {facts[2] if len(facts) > 2 else "No information"}
D. None of these

Correct Answer: A

Explanation:
The answer is based on retrieved sports knowledge from ChromaDB.


Question 2:
Which information is related to {sport}?

A. {facts[1] if len(facts) > 1 else "No information"}
B. {facts[2] if len(facts) > 2 else "No information"}
C. Unknown information
D. None of these

Correct Answer: A

Explanation:
The answer is generated using sports facts stored in the database.


Question 3:
Choose the correct sports fact:

A. {facts[2] if len(facts) > 2 else "No information"}
B. None of these
C. Unknown information
D. Not related

Correct Answer: A

Explanation:
The information is retrieved from ChromaDB.


Question 4:
Which option contains sports information?

A. {facts[0] if len(facts) > 0 else "No information"}
B. Not related
C. Unknown
D. None of these

Correct Answer: A

Explanation:
The answer comes from the sports knowledge database.


Question 5:
Select the correct statement:

A. {facts[1] if len(facts) > 1 else "No information"}
B. None of these
C. Unknown information
D. Not related

Correct Answer: A

Explanation:
The quiz is created using retrieved sports information.


"""

    print(quiz_text)

    return quiz_text