import streamlit as st
import joblib
import re
import string

# Load model and vectorizer
vectorizer = joblib.load('vectorizer.jb')
lr_model = joblib.load('lr_model.jb')

# Cleaning function (must match training exactly)
def clean_text(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('\\W', ' ', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

st.title("Fake News Detector")
st.write("Enter news Article below to check if it is real or fake.")

news_input = st.text_area("News Article","Type Here")

if st.button("Check News"):
    if news_input.strip() != "":
        # CLEAN the input before transforming
        cleaned_input = clean_text(news_input)
        transform_input = vectorizer.transform([cleaned_input])
        prediction = lr_model.predict(transform_input)

        if prediction[0] == 1:
            st.success("The news article is Real.")
        else:
            st.error("The news article is Fake.")
    else:
        st.warning("Please enter a news article to analyze.")
