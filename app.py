import streamlit as st
import google.generativeai as genai

# --- CONFIGURATION ---
API_KEY = "AIzaSyD3mlCfbd9vU9xV97Q7CTN6fxwOd5I_8mQ"

try:
    # API Configure karna
    genai.configure(api_key=API_KEY)
    
    # Naya aur stable model 'gemini-1.5-pro' use kar rahe hain
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro"
    )
except Exception as e:
    st.error(f"Setup Error: {e}")

# --- APP UI ---
st.set_page_config(page_title="Adhira AI", page_icon="✨")
st.title("✨ Adhira AI Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Adhira se kuch puchiye..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Response generate karna
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            # Agar ab bhi error aaye toh ye line asli wajah batayegi
            st.error(f"Technical Detail: {e}")
            
