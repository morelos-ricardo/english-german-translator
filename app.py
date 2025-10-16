from openai import OpenAI
import os
import streamlit as st

# Initialize client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("English → German Translator")

english_text = st.text_area("Enter English text here:")
formality = st.selectbox("Formality:", ["informal", "formal"])
number = st.selectbox("Number:", ["singular", "plural"])

if st.button("Translate"):
    if not english_text.strip():
        st.warning("Please enter some text to translate.")
    else:
        prompt = f"Translate the following English text to German, in {formality} form and {number} form:\n{english_text}"
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",   # use gpt-4o-mini (fast & cheap) or gpt-4o
                messages=[{"role": "user", "content": prompt}]
            )
            german_text = response.choices[0].message.content
            st.text_area("German Translation:", value=german_text, height=200)
        except Exception as e:
            st.error(f"Translation failed: {e}")
