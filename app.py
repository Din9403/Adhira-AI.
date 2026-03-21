import streamlit as st
import google.generativeai as genai
import os

# 1. Page Configuration
st.set_page_config(page_title="Adhira AI", page_icon="❤️")

# 2. Sidebar mein Photo dikhane ka Safe Tarika
with st.sidebar:
    st.title("Adhira Settings")
    
    # Photo dikhane ki koshish (Agar error aaye toh app crash nahi hogi)
    photo_path = "adhira.jpg" # <--- Jo naam GitHub par rakha hai wahi yahan likhein
    
    if os.path.exists(photo_path):
        try:
            st.image(photo_path, caption="Adhira - Your Learning Companion", use_container_width=True)
        except Exception:
            st.warning("Photo load karne mein dikkat ho rahi hai.")
    else:
        st.info("Photo file nahi mili. Naam check karein.")

    api_key = st.text_input("Enter Gemini API Key", type="password")

st.title("Adhira: Your Learning Companion ❤️")

# 3. Baaki ka Chat Code (Same rahega)
if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("Adhira se sawal pucho..."):
            adhira_prompt = f"Tumhara naam Adhira hai. ITI Fitter aur RRB Group D expert ho. Hinglish mein jawab do. Sawal: {prompt}"
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            response = model.generate_content(adhira_prompt)
            with st.chat_message("assistant"):
                st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})

    except Exception as e:
        st.error(f"Connection Error: {e}")
else:
    st.info("👈 Sidebar mein API Key dalein!")
    
