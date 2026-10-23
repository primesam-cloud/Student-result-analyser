
import streamlit as st

st.title("Student Result Analyzer")
st.write("Calculate the average of your students' scores.")

scores_text = st.text_input(
    "Enter scores separated by commas",
    "85, 72, 64, 48, 91"
)

if st.button("Analyze Results"):
    try:
        scores = [
            float(score.strip())
            for score in scores_text.split(",")
        ]

        if not scores or not all(
            0 <= score <= 100 for score in scores
        ):
            st.error("Enter scores between 0 and 100.")
        else:
            average = sum(scores) / len(scores)

            st.metric("Class Average", f"{average:.2f}%")
            st.metric("Highest Score", max(scores))
            st.metric("Lowest Score", min(scores))
            st.metric("Number of Students", len(scores))

    except ValueError:
        st.error("Please enter valid numbers separated by commas.")
