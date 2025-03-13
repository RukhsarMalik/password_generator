import streamlit as st
import random
import string


def generate_password(length, use_digits, use_special_chars):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = not any(char.isdigit() for char in password)
    uppercase_error = not any(char.isupper() for char in password)
    lowercase_error = not any(char.islower() for char in password)
    special_char_error = not any(char in string.punctuation for char in password)

    errors = [length_error, digit_error, uppercase_error, lowercase_error, special_char_error]
    strength = "Weak" if any(errors) else "Strong"

    return strength, errors

st.title("🔐 Password Generator & Checker")

st.header("Generate a Password")
length = st.slider("Select password length", min_value=8, max_value=15, value=12)
use_digits = st.checkbox("Include digits (0-9)")
use_special_chars = st.checkbox("Include special characters (!@#$%^&*)")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special_chars)
    st.success(f"Your generated password: `{password}`")

st.header("Check Password Strength")
password_to_check = st.text_input("Enter a password to check")
if st.button("Check Strength"):
    if password_to_check:
        strength, errors = check_password_strength(password_to_check)
        st.info(f"Password strength: {strength}")
        if any(errors):
            st.warning("Your password has the following issues:")
            if errors[0]:
                st.write("- Password should be at least 8 characters long")
            if errors[1]:
                st.write("- Password should include at least one digit")
            if errors[2]:
                st.write("- Password should include at least one uppercase letter")
            if errors[3]:
                st.write("- Password should include at least one lowercase letter")
            if errors[4]:
                st.write("- Password should include at least one special character")
        else:
            st.success("Your password looks strong! 🛡️")
    else:
        st.error("Please enter a password to check.")

st.caption("Ensure your password is strong and secure! 🛡️")