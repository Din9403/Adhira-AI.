import streamlit as st
import google.generativeai as genai

# --- CONFIGURATION ---
API_KEY = "AIzaSyD3mlCfbd9vU9xV97Q7CTN6fxwOd5I_8mQ"

# Clear cache to avoid old errors
st.cache_resource.clear()

try:
    genai.configure(api_key=API_KEY)
    
    # Sabse stable model configuration
    model = genai.GenerativeModel('gemini-pro')
    
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
            # Direct generate content call
            response = model.generate_content(prompt)
            if response.text:
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            else:
                st.warning("Adhira soch rahi hai... dubara koshish karein.")
        except Exception as e:
            st.error(f"Technical Detail: {e}")
            st.info("Agar 404 aa raha hai, toh Google AI Studio mein ek nayi API Key generate karke dekhein.")
            
