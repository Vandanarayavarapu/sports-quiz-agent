import streamlit as st
from quiz_generator import generate_quiz

st.title("🏏 AI Sports Quiz Generator")

st.write("Generate sports quizzes using AI + RAG")

# Select sport
sport = st.selectbox(
    "Select Sport",
    ["Cricket", "Football", "Tennis", "Badminton", "Basketball"]
)

# Select difficulty
difficulty = st.selectbox(
    "Select Difficulty",
    ["Easy", "Medium", "Hard"]
)

# Button
if st.button("Generate Quiz"):
    st.subheader("Your Quiz")

    quiz = generate_quiz(sport, difficulty)
    st.write(quiz)