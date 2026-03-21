import streamlit as st
import google.generativeai as genai

# 1. Title
st.set_page_config(page_title="Adhira AI", page_icon="❤️")
st.title("Adhira: Your Learning Companion ❤️")

# 2. Key Input
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # Ye line sabse stable model uthayegi
        model = genai.GenerativeModel('gemini-pro') 
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("Sawal pucho..."):
            # Adhira ki personality
            full_prompt = f"Tumhara naam Adhira hai. ITI Fitter aur RRB Group D expert ho. Hinglish mein jawab do. Sawal: {prompt}"
            
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            response = model.generate_content(full_prompt)
            
            with st.chat_message("assistant"):
                st.markdown(response.text)
            
            st.session_state.messages.append({"role": "assistant", "content": response.text})

    except Exception as e:
        st.error(f"Connection Error: {e}")
else:
    st.info("👈 Sidebar mein API Key dalein!")
    
