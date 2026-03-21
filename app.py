import streamlit as st
import google.generativeai as genai

# 1. Page Title
st.set_set_page_config(page_title="Adhira AI", page_icon="❤️")
st.title("Adhira: Your Learning Companion ❤️")

# 2. Sidebar API Key
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # Sabse zaroori badlav: Ye code khud check karega ki kaunsa model available hai
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        
        if available_models:
            # Jo bhi pehla model mile (flash ya pro), use utha lo
            selected_model = available_models[0]
            model = genai.GenerativeModel(selected_model)
        else:
            st.error("Aapki API key ke liye koi model nahi mila.")
            st.stop()
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("Adhira se sawal pucho..."):
            # Adhira ki personality
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
else:
    st.info("👈 Sidebar mein API Key dalein!")
    
