import streamlit as st
import google.generativeai as genai

# --- CONFIGURATION ---
# Aapki API Key (Jo aapne di thi)
API_KEY = "AIzaSyD3mlCfbd9vU9xV97Q7CTN6fxwOd5I_8mQ"

try:
    genai.configure(api_key=API_KEY)
    
    # Hum 'gemini-1.5-flash' use karenge kyunki ye sabse fast hai
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction="Tumhara naam Adhira hai. Tum ek intelligent AI assistant ho jo RRB Group D aur ITI Fitter ki padhai mein madad karti ho."
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
            # Yahan hume asli error dikhega
            st.error(f"Asli Error ye hai: {e}")
            st.info("Agar 'API_KEY_INVALID' likha hai, toh Google AI Studio se nayi key banayein.")
            
