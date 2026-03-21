import streamlit as st
import google.generativeai as genai
import os

# 1. Page Configuration
st.set_page_config(page_title="Adhira AI", page_icon="❤️")

# 2. Sidebar mein Photo aur Settings
with st.sidebar:
    st.title("Adhira Settings")
    
    # Photo display check
    photo_path = "adhira.jpg" 
    if os.path.exists(photo_path):
        try:
            st.image(photo_path, caption="Adhira - Your Learning Companion")
        except:
            st.warning("Photo load nahi ho saki.")
    else:
        st.info("Photo file 'adhira.jpg' nahi mili.")

    api_key = st.text_input("Enter Gemini API Key", type="password")

st.title("Adhira: Your Learning Companion ❤️")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # --- YE HAI ASLI SOLUTION ---
        # Hum saare models ki list nikalenge jo chat support karte hain
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        
        if available_models:
            # Jo sabse best model milega, use chun lenge
            # Zyadatar ye 'models/gemini-1.5-flash' ya 'models/gemini-pro' hoga
            selected_model = available_models[0] 
            model = genai.GenerativeModel(selected_model)
        else:
            st.error("Aapki key ke liye koi model nahi mila. Nayi key banayein.")
            st.stop()
        # ----------------------------

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
        st.error(f"Adhira connect nahi ho pa rahi: {e}")
else:
    st.info("👈 Sidebar mein API Key dalein!")
    
