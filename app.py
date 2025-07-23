import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.inception_resnet_v2 import preprocess_input
from PIL import Image
import numpy as np

# Title and description
st.set_page_config(page_title="Dental Classifier", layout="centered")
st.title("🦷 Dental Images Classifier")
st.write("Upload a dental image and get a predicted class.")

# Load model once
@st.cache_resource
def load_trained_model():
    model = load_model("pretrained_model.keras")
    return model

model = load_trained_model()
class_names = ['CaS', 'CoS', 'Gum', 'MC', 'OC', 'OLP', 'OT']

# Upload UI
uploaded_file = st.file_uploader("Choose a dental image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess
    img = image.resize((224, 224))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Predict
    predictions = model.predict(img_array)
    predicted_index = np.argmax(predictions[0])
    predicted_class = class_names[predicted_index]
    confidence = predictions[0][predicted_index] * 100

    # Output
    st.markdown(f"### 🧠 Prediction: **{predicted_class}** ({confidence:.2f}% confidence)")
    st.bar_chart(predictions[0])
