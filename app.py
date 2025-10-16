import os
import openai
import streamlit as st

openai.api_key = os.environ["OPENAI_API_KEY"]


# ====== Configure your OpenAI API key ======
# For Streamlit Cloud, we will store it as a secret
# openai.api_key = "YOUR_API_KEY"  # Don't hardcode in cloud apps

st.title("English → German Translator")

# Input
english_text = st.text_area("Enter English text here:")

# Options
formality = st.selectbox("Formality:", ["informal", "formal"])
number = st.selectbox("Number:", ["singular", "plural"])

# Translate button
if st.button("Translate"):
    if not english_text.strip():
        st.warning("Please enter some text to translate.")
    else:
        prompt = f"Translate the following English text to German, in {formality} form and {number} form:\n{english_text}"
        try:
            response = openai.ChatCompletion.create(
                model="gpt-5-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            german_text = response.choices[0].message.content
            st.text_area("German Translation:", value=german_text, height=200)
        except Exception as e:
            st.error(f"Translation failed: {e}")


