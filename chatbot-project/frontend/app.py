import streamlit as st
import requests

API_URL = "http://localhost:8000/chat"  # Ensure this matches the backend route

st.title("Chatbot using Qwen Model")
st.markdown("Enter a prompt and receive a response.")

prompt = st.text_input("Your Prompt:")
image_url = st.text_input("Optional Image URL:")

if st.button("Send"):
    if prompt.strip():
        with st.spinner("Fetching response..."):
            try:
                response = requests.post(
                    API_URL,
                    json={"prompt": prompt, "image_url": image_url or None},
                    timeout=10  # Add a timeout of 10 seconds
                )
                if response.status_code != 200:
                    st.error(f"Backend error: {response.status_code} - {response.text}")
                else:
                    data = response.json()
                    reply = data.get("choices", [{}])[0].get("content", "No response")
                    st.markdown(f"**Response:** {reply}")
            except requests.exceptions.Timeout:
                st.error("The request timed out. Please try again.")
            except requests.exceptions.RequestException as e:
                st.error(f"Network error: {e}")
            except Exception as e:
                st.error(f"Unexpected error: {e}")
