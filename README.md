
# Phishing Website Detection Using Machine Learning

## Problem Statement
Phishing websites can trick users into sharing sensitive
information. This project demonstrates a machine learning
approach to classifying websites using encoded features.

## Objective
Train and evaluate a classification model using a labelled
phishing website dataset.

## Dataset
UCI Machine Learning Repository - Phishing Websites
https://archive.ics.uci.edu/dataset/327/phishing+websites

The dataset contains 11,055 instances and 30 input features.

## Technologies
- Python
- Pandas
- Scikit-learn
- Joblib
- Streamlit

## Methodology
1. Load the labelled dataset.
2. Inspect features and missing values.
3. Split the data into training and testing sets.
4. Train a Decision Tree classifier.
5. Evaluate predictions using classification metrics.
6. Save the model and run a Streamlit interface.

## Run Locally
Install dependencies:

python -m pip install -r requirements.txt

Train the model:

python train_model.py

Launch the application:

python -m streamlit run app.py

## Evaluation
Add the actual accuracy, precision, recall, F1-score and
confusion matrix produced by your run.

## Limitations
The current interface accepts encoded dataset features.
It does not extract features from a pasted URL and should
not be treated as a real-time security scanner.

## Dataset Attribution
R. Mohammad, L. McCluskey and F. Thabtah,
Phishing Websites, UCI Machine Learning Repository.
https://doi.org/10.24432/C51W2X

Dataset licence: CC BY 4.0.
    