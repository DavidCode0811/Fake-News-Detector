import streamlit as st
import joblib

vectorizer = joblib.load('vectorizer.jb')
lr_model = joblib.load('lr_model.jb')

st.title("Fake News Detector")
st.write("Enter news Article below to check if it is real or fake.")

news_input = st.text_area("News Article","Type Here")

if st.button("Check News"):
    if news_input.strip() != "":
        transform_input = vectorizer.transform([news_input])
        prediction = lr_model.predict(transform_input)

        if prediction[0] == 1:
            st.success("The news article is Real.")
        else:
            st.error("The news article is Fake.")
    else:
        st.warning("Please enter a news article to analyze.")
