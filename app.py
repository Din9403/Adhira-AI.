import streamlit as st
import google.generativeai as genai

# 1. Page Title aur UI Setup
st.set_page_config(page_title="Adhira AI", page_icon="❤️")
st.title("Adhira: Your Learning Companion ❤️")

# 2. Sidebar mein API Key lene ka box
st.sidebar.title("Configuration")
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

# 3. Agar Key dali gayi hai toh AI active karo
if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # Adhira ki Personality
        instruction = "Tumhara naam Adhira hai. ITI Fitter aur RRB Group D ki expert ho. Hinglish mein baat karo aur hamesha supportive raho. ❤️"
        
        # Model update: Yaha hum 'gemini-pro' ya updated flash version use karenge
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash-latest", # 'latest' lagane se 404 error hat jayega
            system_instruction=instruction
        )
        
        # Chat History maintain karna
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Purane messages dikhana
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Naya sawal puchna
        if prompt := st.chat_input("Adhira se sawal pucho..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # AI ka jawab nikalna (safety settings ke bina fast chalega)
            response = model.generate_content(prompt)
            full_response = response.text
            
            with st.chat_message("assistant"):
                st.markdown(full_response)
            
            st.session_state.messages.append({"role": "assistant", "content": full_response})

    except Exception as e:
        # Agar ab bhi error aaye toh ye exact problem batayega
        st.error(f"Oh no! Adhira ko connect karne mein dikkat ho rahi hai: {e}")
else:
    st.info("👈 Please enter your Gemini API Key in the sidebar to start talking with Adhira!")
    
