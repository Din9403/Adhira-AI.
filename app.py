import streamlit as st
import google.generativeai as genai

# Page ki settings
st.set_page_config(page_title="Adhira AI", page_icon="❤️")
st.title("Adhira: Your Learning Companion ❤️")

# API Key setup (Ye hum baad mein secret mein dalenge)
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    
    # Adhira ki Personality
    instruction = "Tumhara naam Adhira hai. Tum ek warm aur caring learning companion ho. Hinglish mein baat karo. Tum ITI Fitter aur RRB Group D ki expert ho. Hamesha details mein samjhao aur ❤️ emojis use karo."
    
    model = genai.GenerativeModel(model_name="gemini-1.5-flash", system_instruction=instruction)
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Chat interface
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_input = st.chat_input("Adhira se baat karein...")

    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        response = model.generate_content(user_input)
        
        with st.chat_message("assistant"):
            st.markdown(response.text)
            st.session_state.chat_history.append({"role": "assistant", "content": response.text})
else:
    st.warning("Please enter your API Key in the sidebar to start! ✨")
  
