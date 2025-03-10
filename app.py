import streamlit as st
import random
import string
import pyperclip  # type: ignore

# Custom CSS
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #c2e9fb, #a1c4fd);
        padding: 20px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        characters = string.ascii_letters  # Default: only letters

    return ''.join(random.choice(characters) for _ in range(length))

# App Title
st.title("🔐 Password Generator")

# Password length selection
length = st.slider("📏 Select password length", min_value=8, max_value=20, value=12)

# Options for password complexity
use_uppercase = st.checkbox("🔠 Include Uppercase (A-Z)")
use_lowercase = st.checkbox("🔡 Include Lowercase (a-z)")
use_digits = st.checkbox("🔢 Include Numbers (0-9)")
use_special = st.checkbox("🔣 Include Special Characters (!@#$%^&*)")

# Initialize session state for password
if "password" not in st.session_state:
    st.session_state.password = ""

# Generate password when button is clicked
if st.button("🚀 Generate Password"):
    st.session_state.password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
    st.success(f"🛡️ **Generated Password:** `{st.session_state.password}`")

# Copy password to clipboard
if st.session_state.password and st.button("📋 Copy Password"):
    pyperclip.copy(st.session_state.password)
    st.success("✅ Password copied to clipboard!")

# Footer
st.markdown(
    "<h4 style='text-align: center;'>Made with ❤️ by Muhammad Nafees.</h4>",
    unsafe_allow_html=True
)
