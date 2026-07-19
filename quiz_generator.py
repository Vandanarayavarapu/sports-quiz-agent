from search_database import collection, model
from web_search import search_sports_news


def generate_quiz(sport, difficulty):

    query = f"{sport} sports facts"

    query_embedding = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=3
    )

    facts = results["documents"][0]

    news = search_sports_news(
        f"latest {sport} news"
    )

    option_a = facts[0] if len(facts) > 0 else "No information"
    option_b = facts[1] if len(facts) > 1 else "No information"
    option_c = facts[2] if len(facts) > 2 else "No information"

    quiz_text = f"""
# AI Sports Quiz Generator

Sport: {sport}  
Difficulty: {difficulty}

## Question 1:

Which fact is related to {sport}?

A. {option_a}

B. {option_b}

C. {option_c}

D. None of these


Correct Answer: A

Explanation:  
The answer is generated using retrieved sports knowledge from ChromaDB.

---

## Question 2:

Which information is related to {sport}?

A. {option_b}

B. {option_c}

C. Unknown information

D. None of these


Correct Answer: A

Explanation:  
The answer is generated from the retrieved sports facts.

---

## Question 3:

Choose the correct sports fact:

A. {option_c}

B. None of these

C. Unknown information

D. Not related


Correct Answer: A

Explanation: 
The information is retrieved from ChromaDB.

---

## Question 4:

Which option contains sports information?

A. {option_a}

B. Not related

C. Unknown information

D. None of these


Correct Answer: A

Explanation:  
The answer comes from the sports knowledge database.

---

## Question 5:

Select the correct statement:

A. {option_b}

B. None of these

C. Unknown information

D. Not related


Correct Answer: A

Explanation:  
The quiz is created using retrieved sports information.

"""

    return quiz_text