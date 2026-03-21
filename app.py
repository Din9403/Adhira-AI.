import streamlit as st
import google.generativeai as genai

# Page Setup
st.set_page_config(page_title="Adhira AI", page_icon="❤️")
st.title("Adhira: Your Learning Companion ❤️")

# Sidebar
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    try:
        # Configuration
        genai.configure(api_key=api_key)
        
        # Sabse pehle naya model check karein, phir purana
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            # Test run to check if model works
            model.generate_content("test")
        except:
            model = genai.GenerativeModel('gemini-pro')
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display Chat History
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Chat Input
        if prompt := st.chat_input("Adhira se sawal pucho..."):
            # Hum prompt ke saath Adhira ki personality khud jod denge
            adhira_prompt = f"Tumhara naam Adhira hai. Tum ITI Fitter aur RRB Group D ki expert ho. Hinglish mein jawab do. Sawal: {prompt}"
            
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # Generate Response
            response = model.generate_content(adhira_prompt)
            
            with st.chat_message("assistant"):
                st.markdown(response.text)
            
            st.session_state.messages.append({"role": "assistant", "content": response.text})

    
