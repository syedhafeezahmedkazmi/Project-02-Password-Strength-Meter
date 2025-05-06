import streamlit as st

def check_length(password):
    return len(password) >= 8

def check_uppercase(password):
    return any(char.isupper() for char in password)

def check_lowercase(password):
    return any(char.islower() for char in password)

def check_digit(password):
    return any(char.isdigit() for char in password)

def check_special_char(password):
    special_chars = "!@#$%^&*"
    return any(char in special_chars for char in password)

def calculate_strength(password):
    score = 0
    criteria = {
        "Length ≥ 8": check_length(password),
        "Uppercase": check_uppercase(password),
        "Lowercase": check_lowercase(password),
        "Digit": check_digit(password),
        "Special Char": check_special_char(password)
    }
    
    score = sum(criteria.values())
    return score, criteria

def main():
    st.set_page_config(page_title="Password Strength Meter", page_icon="🔐")
    
    st.title("🔐 Password Strength Meter")
    st.write("Check how strong your password is based on security criteria")
    
    password = st.text_input("Enter your password:", type="password")
    
    if password:
        score, criteria = calculate_strength(password)
        
        st.subheader("Results:")
        
        # Display progress bar
        strength_level = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
        st.progress(score/5)
        st.write(f"**Strength:** {strength_level[score-1] if score > 0 else 'Very Weak'}")
        
        # Display criteria checklist
        st.write("**Password Criteria:**")
        for name, met in criteria.items():
            status = "✅" if met else "❌"
            st.write(f"{status} {name}")
        
        # Provide feedback
        st.subheader("Recommendations:")
        if score == 5:
            st.success("Excellent! Your password meets all security requirements.")
        else:
            st.warning("To improve your password:")
            if not check_length(password):
                st.write("- Make it at least 8 characters long")
            if not check_uppercase(password):
                st.write("- Add at least one uppercase letter (A-Z)")
            if not check_lowercase(password):
                st.write("- Add at least one lowercase letter (a-z)")
            if not check_digit(password):
                st.write("- Add at least one digit (0-9)")
            if not check_special_char(password):
                st.write("- Add at least one special character (!@#$%^&*)")

if __name__ == "__main__":
    main()