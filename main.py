import streamlit as st
from transformers import pipeline

page_bg_img = """
<style>
body {
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
background-size: cover;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("Text Input")

user_input = st.text_input("Enter your text")

if user_input:
    st.write("You entered: ", user_input)
else:
    st.write("Please enter some text")

if st.button("Submit"):
    distilled_student_sentiment_classifier = pipeline(
        model="lxyuan/distilbert-base-multilingual-cased-sentiments-student", top_k=1
    )
    # english
    score = distilled_student_sentiment_classifier(user_input)
    st.write("Result: ", score[0][0]["label"], score[0][0]["score"])
