import streamlit as st
import random
import string
import pyperclip  # type: ignore # For copying the password to clipboard

# Custom CSS for Light Background Color (Light Blue Gradient)
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #c2e9fb, #a1c4fd); /* Light Blue Gradient */
        color: black; /* Dark text for better visibility */
    }
    .stApp {
        background: linear-gradient(135deg, #c2e9fb, #a1c4fd); /* Background for App */
        padding: 20px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    """
    Function to generate a random password based on user-selected criteria.
    :param length: Length of the password
    :param use_uppercase: Include uppercase letters (A-Z)
    :param use_lowercase: Include lowercase letters (a-z)
    :param use_digits: Include numbers (0-9)
    :param use_special: Include special characters (!@#$%^&*)
    :return: Generated password as a string
    """
    characters = ""

    # Add selected character types to the password
    if use_uppercase:
        characters += string.ascii_uppercase  # A-Z
    if use_lowercase:
        characters += string.ascii_lowercase  # a-z
    if use_digits:
        characters += string.digits  # 0-9
    if use_special:
        characters += string.punctuation  # Special characters (!@#$%^&*)

    # Default to letters if no option is selected
    if not characters:
        characters = string.ascii_letters  # A-Z, a-z

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

# Initialize password variable in session state
if 'password' not in st.session_state:
    st.session_state.password = ""

# Generate password when button is clicked
if st.button("🚀 Generate Password"):
    st.session_state.password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
    st.success(f"🛡️ **Generated Password:** `{st.session_state.password}`")

# Copy password to clipboard
if st.button("📋 Copy Password"):
    if st.session_state.password:
        pyperclip.copy(st.session_state.password)
        st.success("✅ Password copied to clipboard!")
    else:
        st.warning("⚠️ No password generated yet!")

# Footer
st.write("-------------------------------------------------")

# Centered footer text
st.markdown(
    "<h4 style='text-align: center;'>Made with ❤️ by Muhammad Nafees.</h4>",
    unsafe_allow_html=True
)
