import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Set up Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")  # You can also try "gemini-1.5-pro"

st.set_page_config(page_title="Dream Analyzer", page_icon="💤")
st.title("Dream Analyzer + Sweet Dreams Tips")

st.write("Type your dream below and receive an insightful interpretation, followed by tips for better sleep.")

dream = st.text_area("Describe your dream here:", height=150)

if st.button("🔍 Analyze Dream"):
    if dream.strip() == "":
        st.warning("Please enter something.")
    else:
        with st.spinner("Analyzing your dream..."):
            try:
                # Dream interpretation
                dream_prompt = f"I had this dream: {dream}. Please interpret it like a psychologist using symbols, emotions, and subconscious patterns."
                dream_response = model.generate_content(dream_prompt)
                interpretation = dream_response.text

                # Tips for better sleep
                tips_prompt = "Suggest 5 short tips for better sleep and peaceful dreams."
                tips_response = model.generate_content(tips_prompt)
                tips = tips_response.text

                # Display
                st.subheader("🔮 Dream Interpretation:")
                st.write(interpretation)

                st.subheader("💤 Sweet Dream Tips:")
                st.markdown(tips)

            except Exception as e:
                st.error(f"Something went wrong: {e}")

st.markdown("---")
st.caption("Built by Sheetal with Streamlit + Gemini AI")
