import streamlit as st
import google.generativeai as genai

# 1. Page Configuration
st.set_page_config(page_title="Adhira AI", page_icon="❤️")
st.title("Adhira: Your Learning Companion ❤️")

# 2. Sidebar API Key
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # Ye line check karegi ki aapki key par kaun sa model chal raha hai
        models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        
        if models:
            # Sabse naya model (Flash 1.5) pehle lene ki koshish karega
            selected_model = models[0] 
            model = genai.GenerativeModel(selected_model)
        else:
            st.error("Aapki API key ke liye koi model nahi mila. Nayi key banayein.")
            st.stop()
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

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
    st.info("👈 Sidebar mein API Key dalein!")
    
