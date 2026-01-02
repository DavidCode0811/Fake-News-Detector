Fake News Detector

A web-based Fake News Detection application built with Python, Machine Learning, and Natural Language Processing (NLP), and deployed using Streamlit.
The application allows users to input news text and instantly receive a prediction indicating whether the content is Fake or True.

🔗 Live Demo:
https://fake-news-detector012.streamlit.app/

Overview

The Fake News Detector analyzes textual news content using NLP techniques and a trained machine learning model.
It learns linguistic patterns from labeled datasets and predicts the credibility of unseen news articles in real time through a simple web interface.

This repository contains the source code used to build and deploy the application.
Large datasets and trained model files are intentionally excluded.

Features

Interactive web interface built with Streamlit

Accepts raw news text as user input

Predicts Fake or True news instantly

Lightweight and responsive UI

Suitable for academic demonstrations and research projects

Project Structure
Fake-News-Detector/
│
├── app.py               # Streamlit application entry point
├── src/                 # Core ML and NLP logic
├── models/              # Model training scripts (no large binaries)
├── data_sample/         # Small sample datasets
├── requirements.txt     # Project dependencies
├── .gitignore           # Excludes large files and environments
└── README.md

How It Works

User inputs a news article or headline

Text is cleaned and preprocessed

NLP techniques convert text into numerical features

A trained ML classifier evaluates the input

The app outputs a Fake or True prediction

Running the Project Locally

Clone the repository

git clone https://github.com/DavidCode0811/Fake-News-Detector.git
cd Fake-News-Detector


Create and activate a virtual environment

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate


Install dependencies

pip install -r requirements.txt


Run the Streamlit application

streamlit run app.py

Deployment

The application is deployed using Streamlit Community Cloud.

Live URL:
https://fake-news-detector012.streamlit.app/

Dataset and Models

Full datasets and trained model files are not included in this repository due to size constraints.

The project uses labeled true and fake news datasets commonly applied in NLP research.

Large files such as datasets, trained models, and virtual environments are excluded using .gitignore.

Disclaimer

This project is intended for educational and research purposes only.
Predictions should not be considered definitive or used as a sole source of truth.

Author

Bingham University computer Science Students Group 8
Course Title: Artificial Intelligence (CMP 409)
Computer Science Undergraduate
Machine Learning & NLP Enthusiast