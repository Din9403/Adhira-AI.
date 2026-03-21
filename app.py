import streamlit as st
import google.generativeai as genai

# Page Layout
st.set_page_config(page_title="Adhira AI", page_icon="❤️")
st.title("Adhira: Your Learning Companion ❤️")

# Sidebar
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # Adhira's Identity
        instruction = "Tumhara naam Adhira hai. Tum ek warm aur supportive learning companion ho. Tum ITI Fitter aur RRB Group D ki expert ho. Hinglish mein baat karo aur ❤️ emojis use karo."
        
        # Yahan hum sabse purana aur stable model name use kar rahe hain jo har jagah chalta hai
        model = genai.GenerativeModel(
            model_name="models/gemini-1.5-flash", # 'models/' prefix lagane se error nahi aayega
            system_instruction=instruction
        )
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("Adhira se sawal pucho..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # AI Response
            response = model.generate_content(prompt)
            
            with st.chat_message("assistant"):
                st.markdown(response.text)
            
            st.session_state.messages.append({"role": "assistant", "content": response.text})

    except Exception as e:
        # Agar ab bhi error aaye, toh hum alternative model try karenge
        st.error(f"Technical Error: {e}")
        st.info("💡 Tip: Agar 404 error aaye, toh apni API key dobara check karein ya thodi der baad try karein.")
else:
    st.info("👈 Please enter your Gemini API Key in the sidebar!")
  
