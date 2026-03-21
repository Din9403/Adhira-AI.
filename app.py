import streamlit as st
import google.generativeai as genai
import os

# 1. Page Configuration
st.set_page_config(page_title="Adhira AI", page_icon="❤️")

# 2. Sidebar mein Photo aur Key
with st.sidebar:
    st.title("Settings")
    # Photo ka naam check karein (jo aapne GitHub par rakha hai)
    photo_name = "adhira.jpg" 
    
    if os.path.exists(photo_name):
        try:
            st.image(photo_name, caption="Adhira - Your Learning Companion")
        except:
            st.warning("Photo load nahi ho saki.")
    else:
        st.info(f"'{photo_name}' file nahi mili.")
        
    api_key = st.text_input("Enter Gemini API Key", type="password")

st.title("Adhira: Your Learning Companion ❤️")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # Sabse stable model name bina 'models/' prefix ke
        model = genai.GenerativeModel('gemini-pro') 
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display Chat History
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Chat Input
        if prompt := st.chat_input("Adhira se sawal pucho..."):
            # Adhira's personality prompt
            final_prompt = f"Tumhara naam Adhira hai. ITI Fitter aur RRB Group D expert ho. Hinglish mein jawab do. Sawal: {prompt}"
            
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # AI Response
            response = model.generate_content(final_prompt)
            
            with st.chat_message("assistant"):
                st.markdown(response.text)
            
            st.session_state.messages.append({"role": "assistant", "content": response.text})

    except Exception as e:
        st.error(f"Adhira connect nahi ho pa rahi: {e}")
        st.info("💡 Tip: Ek baar Google AI Studio se 'Nayi API Key' bana kar try karein.")
else:
    st.info("👈 Sidebar mein API Key dalein!")
    
