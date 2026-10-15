
import joblib
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Phishing Detection",
    page_icon="🛡️"
)

st.title("🛡️ Phishing Website Detection")
st.write(
    "Enter the encoded website features to get a "
    "machine-learning prediction."
)

st.warning(
    "This demo accepts dataset feature values, not raw URLs. "
    "It is not a browser security scanner."
)

@st.cache_resource
def load_model():
    return joblib.load("models/phishing_model.joblib")

try:
    saved = load_model()
    model = saved["model"]
    features = saved["features"]
except FileNotFoundError:
    st.error("Model not found. Run python train_model.py first.")
    st.stop()

st.subheader("Website features")
st.caption(
    "The dataset uses encoded feature values. "
    "Choose -1, 0, or 1 for each feature."
)

values = {}

columns = st.columns(3)

for i, feature in enumerate(features):
    with columns[i % 3]:
        values[feature] = st.selectbox(
            feature,
            options=[-1, 0, 1],
            index=1,
            key=feature
        )

if st.button("Predict website class", type="primary"):
    sample = pd.DataFrame(
        [[values[f] for f in features]],
        columns=features
    )

    prediction = int(model.predict(sample)[0])

    if prediction == 1:
        st.error("Prediction: Potential Phishing Website")
    else:
        st.success("Prediction: Potentially Legitimate Website")

    st.caption(
        "This is a model prediction, not a guarantee of safety. "
        "Do not enter sensitive information based on this result."
    )
