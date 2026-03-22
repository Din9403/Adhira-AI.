import streamlit as st
import google.generativeai as genai

# --- CONFIGURATION ---
# Maine aapki API Key yahan add kar di hai
API_KEY = "AIzaSyD3mlCfbd9vU9xV97Q7CTN6fxwOd5I_8mQ"

try:
    genai.configure(api_key=API_KEY)
    
    # Adhira ki personality aur settings
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction="Tumhara naam Adhira hai. Tum ek intelligent AI assistant ho. Tum user ki padhai, RRB Group D exam aur ITI Fitter trade se jude sawalon mein madad karti ho. Tumhara jawab hamesha saaf, motivational aur dosti bhare lehze mein hona chahiye."
    )
except Exception as e:
    st.error("API connect karne mein dikkat aa rahi hai.")

# --- APP UI SETUP (Mobile Friendly) ---
st.set_page_config(page_title="Adhira AI", page_icon="✨")

# Interface ko sundar banane ke liye thoda CSS
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stChatMessage { border-radius: 20px; box-shadow: 0px 2px 5px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

st.title("✨ Adhira AI Assistant")
st.write("Namaste! Main Adhira hoon. Main aapki kaise madad kar sakti hoon?")

# Chat history ko maintain karne ke liye
if "messages" not in st.session_state:
    st.session_state.messages = []

# Purani baatein screen par dikhane ke liye
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User ka input lena
if prompt := st.chat_input("Yahan apna sawal likhein..."):
    # User message save karein
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Adhira ka response generate karna
    with st.chat_message("assistant"):
        try:
            # AI se uttar mangna
            response = model.generate_content(prompt)
            adhira_reply = response.text
            
            # Screen par dikhana aur history mein save karna
            st.markdown(adhira_reply)
            st.session_state.messages.append({"role": "assistant", "content": adhira_reply})
        except Exception as e:
            st.error(f"Error details: {e}")("Maaf kijiyega, main abhi jawab nahi de pa rahi hoon. Ek baar apni API key check karein.")
            
