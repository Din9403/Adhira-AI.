import streamlit as st
import google.generativeai as genai

# --- CONFIGURATION ---
# Yahan apni NAYI API Key quotes (" ") ke andar dalein
API_KEY = "AIzaSyCeDjQy2a4jSjSNhHgUktx8_YApIKTArCQ"

try:
    genai.configure(api_key=API_KEY)
    
    # Hum model ko bina version suffix ke call karenge
    model = genai.GenerativeModel('gemini-1.5-flash')
    
except Exception as e:
    st.error(f"Setup Error: {e}")

# --- APP UI ---
st.set_page_config(page_title="Adhira AI", page_icon="✨")
st.title("✨ Adhira AI Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat history dikhana
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Adhira se kuch puchiye..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Response generate karna
            response = model.generate_content(prompt)
            if response.text:
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            else:
                st.write("Adhira soch rahi hai... dubara koshish karein.")
        except Exception as e:
            # Agar ab bhi error aaye toh ye exact detail dikhayega
            st.error(f"Technical Detail: {e}")
            
