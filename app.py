import streamlit as st
import google.generativeai as genai

# 1. Page Configuration
st.set_page_config(page_title="Adhira AI", page_icon="❤️")

# 2. Sidebar mein Adhira ki Photo aur Key
with st.sidebar:
    # Check karein ki file ka naam GitHub par '1000341253.jpg' hi hai
    st.image("1000341253.jpg", caption="Adhira - Your Learning Companion")
    st.title("Settings")
    api_key = st.text_input("Enter Gemini API Key", type="password")

st.title("Adhira: Your Learning Companion ❤️")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # Stable Model Selection
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # History Display
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Chat Input
        if prompt := st.chat_input("Adhira se sawal pucho..."):
            adhira_prompt = f"Tumhara naam Adhira hai. ITI Fitter aur RRB Group D expert ho. Hinglish mein jawab do. ❤️ Sawal: {prompt}"
            
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            response = model.generate_content(adhira_prompt)
            
            with st.chat_message("assistant"):
                st.markdown(response.text)
            
            st.session_state.messages.append({"role": "assistant", "content": response.text})

    except Exception as e:
        st.error(f"Adhira connect nahi ho pa rahi: {e}")
else:
    st.info("👈 Sidebar mein apni API Key dalein!")
    
