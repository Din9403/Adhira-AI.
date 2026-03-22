import streamlit as st
import google.generativeai as genai

# --- CONFIGURATION ---
# Yahan apni API Key dalein (Agar Streamlit Secrets use kar rahe hain toh baad mein batata hoon)
API_KEY = "YAHAN_APNI_API_KEY_PASTE_KAREIN"

genai.configure(api_key=API_KEY)

# Assistant ki settings (System Instruction)
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="Tumhara naam Adhira hai. Tum ek bahut hi intelligent aur friendly AI assistant ho. Tum user ki padhai, RRB Group D exam preparation aur ITI Fitter trade se jude sawalon mein madad karti ho. Tumhara lehza hamesha prerak (motivational) hona chahiye."
)

# --- APP UI (Mobile Friendly) ---
st.set_page_config(page_title="Adhira AI", page_icon="✨")
st.markdown("<h2 style='text-align: center;'>✨ Adhira AI Assistant</h2>", unsafe_allow_html=True)

# Chat history setup
if "messages" not in st.session_state:
    st.session_state.messages = []

# Purani chats dikhana
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Adhira se kuch puchiye..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Adhira ka response
    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error("Kuch technical issue lag raha hai. Check karein ki API Key sahi hai ya nahi.")
            
