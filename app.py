import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('model.pkl')

st.title("🐾 Animal Danger Prediction App")
st.write("Enter animal symptoms to check if it's dangerous")

# Inputs
animal_name = st.selectbox("Animal", ["Dog", "Cat"])

symptom1 = st.selectbox("Symptom 1", ["fever", "coughing", "diarrhea","tarry stool","Tiredness","Back pain"])
symptom2 = st.selectbox("Symptom 2", ["fever", "coughing", "diarrhea","tarry stool","Tiredness","Back pain"])
symptom3 = st.selectbox("Symptom 3", ["fever", "coughing", "diarrhea","tarry stool","Tiredness","Back pain"])
symptom4 = st.selectbox("Symptom 4", ["fever", "coughing", "diarrhea","tarry stool","Tiredness","Back pain"])
symptom5 = st.selectbox("Symptom 5", ["fever", "coughing", "diarrhea","tarry stool","Tiredness","Back pain"])

# Encoding maps
animal_map = {
    "Dog": 0,
    "Cat": 1
}

symptom_map = {
    "fever": 0,
    "coughing": 1,
    "diarrhea": 2
}

if st.button("Predict"):
    try:
        # Encode inputs
        animal_input = animal_map[animal_name]
        s1 = symptom_map[symptom1]
        s2 = symptom_map[symptom2]
        s3 = symptom_map[symptom3]
        s4 = symptom_map[symptom4]
        s5 = symptom_map[symptom5]

        # Create sample (6 features total)
        sample = np.array([[animal_input, s1, s2, s3, s4, s5]])

        # Predict
        prediction = model.predict(sample)

        if prediction[0] == 1:
            st.error("⚠️ Dangerous Animal")
        else:
            st.success("✅ Not Dangerous")

    except Exception as e:
        st.warning("⚠️ Error occurred")
        st.text(str(e))