import re
import random
import string
import streamlit as st

# Commonly blacklisted passwords
BLACKLIST = ["password123", "12345678", "qwerty", "letmein", "abc123"]

# Password strength criteria
SPECIAL_CHARACTERS = "!@#$%^&*"

# Function to check password strength
def check_password_strength(password):
    if password in BLACKLIST:
        return "Weak", "This password is too common. Choose a more unique password."

    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one digit (0-9).")

    if any(char in SPECIAL_CHARACTERS for char in password):
        score += 1
    else:
        feedback.append(f"Include at least one special character ({SPECIAL_CHARACTERS}).")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    if strength == "Strong":
        return strength, "Your password is strong and secure!"
    return strength, feedback

# Password generator
def generate_strong_password(length=12):
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(SPECIAL_CHARACTERS)
    ]
    all_chars = string.ascii_letters + string.digits + SPECIAL_CHARACTERS
    password += [random.choice(all_chars) for _ in range(length - 4)]
    random.shuffle(password)
    return ''.join(password)

# Streamlit GUI
st.title("Password Strength Checker")

password = st.text_input("Enter your password", type="password")

if password:
    strength, feedback = check_password_strength(password)
    st.write(f"Your password is {strength}")
    if isinstance(feedback, list):
        for msg in feedback:
            st.warning(msg)
    else:
        st.success(feedback)

if st.button("Suggest a Strong Password"):
    strong_password = generate_strong_password()
    st.info(f"Suggested Strong Password: {strong_password}")
