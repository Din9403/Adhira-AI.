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
        genai.configure(api_key=api_key)
        
        # Personality Setup
        instruction = "Tumhara naam Adhira hai. Tum ek warm aur caring learning companion ho. ITI Fitter aur RRB Group D ki expert ho. Hinglish mein baat karo aur ❤️ emojis use karo."
        
        # Yahan hum sabse stable model 'gemini-pro' use kar rahe hain
        model = genai.GenerativeModel(
            model_name="gemini-pro", 
            system_instruction=instruction
        )
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display Chat History
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Chat Input
        if prompt := st.chat_input("Adhira se sawal pucho..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # Generate Content
            response = model.generate_content(prompt)
            
            with st.chat_message("assistant"):
                st.markdown(response.text)
            
            st.session_state.messages.append({"role": "assistant", "content": response.text})

    except Exception as e:
        st.error(f"Adhira connect nahi ho pa rahi: {e}")
        st.info("💡 Tip: Ek baar apni API key dobara generate karke dekhein.")
else:
    st.info("👈 Please enter your Gemini API Key in the sidebar to start!")
    
