import streamlit as st
import google.generativeai as genai
import requests
import time
import os

# 1. Page Config
st.set_page_config(page_title="Adhira Talking AI", page_icon="❤️")

# 2. Sidebar Settings (Yahan dono Keys aayengi)
with st.sidebar:
    st.title("Adhira Settings")
    if os.path.exists("adhira.jpg"):
        st.image("adhira.jpg", caption="Adhira - Your Learning Companion")
    
    # --- YE DO LINES ZAROORI HAIN ---
    gemini_key = st.text_input("Enter Gemini API Key", type="password")
    did_key = st.text_input("Enter D-ID API Key (Z25...)", type="password")
    # -------------------------------
    
    st.info("D-ID credits limited hote hain, dhyan se use karein!")

st.title("Adhira: Talking AI Companion ❤️")

# 3. Baaki ka Video aur Chat Logic (Pehle wala hi)
def generate_talk(text, did_api_key):
    url = "https://api.d-id.com/talks"
    headers = {
        "Authorization": f"Basic {did_api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "script": {
            "type": "text",
            "input": text,
            "provider": {"type": "microsoft", "voice_id": "hi-IN-SwaraNeural"} 
        },
        "source_url": "https://raw.githubusercontent.com/Din9403/Adhira-AI./main/adhira.jpg",
        "config": {"fluid": True}
    }
    res = requests.post(url, json=payload, headers=headers)
    return res.json().get("id") if res.status_code == 201 else None

def get_video_url(talk_id, did_api_key):
    url = f"https://api.d-id.com/talks/{talk_id}"
    headers = {"Authorization": f"Basic {did_api_key}"}
    while True:
        res = requests.get(url, headers=headers).json()
        if res.get("status") == "done": return res.get("result_url")
        if res.get("status") == "error": return None
        time.sleep(2)

if gemini_key and did_key:
    try:
        genai.configure(api_key=gemini_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        if "messages" not in st.session_state: st.session_state.messages = []

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]): st.markdown(msg["content"])

        if prompt := st.chat_input("Adhira se sawal pucho..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"): st.markdown(prompt)

            adhira_prompt = f"Tumhara naam Adhira hai. ITI Fitter expert ho. Hinglish mein sirf 1-2 lines mein jawab do. Sawal: {prompt}"
            response = model.generate_content(adhira_prompt)
            answer = response.text
            
            with st.chat_message("assistant"):
                st.markdown(answer)
                with st.spinner("Adhira bolne ki tayaari kar rahi hai..."):
                    talk_id = generate_talk(answer, did_key)
                    if talk_id:
                        v_url = get_video_url(talk_id, did_key)
                        if v_url: st.video(v_url)
            
            st.session_state.messages.append({"role": "assistant", "content": answer})
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("👈 Sidebar mein Gemini aur D-ID dono Keys dalein!")
    
