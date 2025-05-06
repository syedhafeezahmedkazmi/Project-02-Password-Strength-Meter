def check_length(password):
    """Check if password is at least 8 characters long"""
    return len(password) >= 8

def check_uppercase(password):
    """Check if password contains uppercase letters"""
    return any(char.isupper() for char in password)

def check_lowercase(password):
    """Check if password contains lowercase letters"""
    return any(char.islower() for char in password)

def check_digit(password):
    """Check if password contains at least one digit"""
    return any(char.isdigit() for char in password)

def check_special_char(password):
    """Check if password contains at least one special character"""
    special_chars = "!@#$%^&*"
    return any(char in special_chars for char in password)

def calculate_strength(password):
    """Calculate password strength score based on criteria"""
    score = 0
    
    # Check each criterion and add to score if met
    if check_length(password):
        score += 1
    if check_uppercase(password):
        score += 1
    if check_lowercase(password):
        score += 1
    if check_digit(password):
        score += 1
    if check_special_char(password):
        score += 1
    
    return score

def provide_feedback(score, password):
    """Provide feedback based on password strength score"""
    if score <= 2:
        print("\n🔴 Weak Password")
        print("Suggestions to improve:")
        if not check_length(password):
            print("- Make it at least 8 characters long")
        if not check_uppercase(password):
            print("- Add at least one uppercase letter")
        if not check_lowercase(password):
            print("- Add at least one lowercase letter")
        if not check_digit(password):
            print("- Add at least one digit (0-9)")
        if not check_special_char(password):
            print("- Add at least one special character (!@#$%^&*)")
    elif score <= 4:
        print("\n🟡 Moderate Password")
        print("Almost there! Consider these improvements:")
        if not check_length(password):
            print("- Make it longer (at least 8 characters)")
        if not check_special_char(password):
            print("- Add a special character (!@#$%^&*)")
    else:
        print("\n🟢 Strong Password!")
        print("Great job! Your password meets all security criteria.")

def password_strength_meter():
    """Main function to run the password strength meter"""
    print("🔐 Password Strength Meter")
    print("-------------------------")
    print("Enter a password to check its strength:")
    print("(A strong password should be at least 8 characters long,")
    print("contain uppercase & lowercase letters, digits, and special characters)")
    
    while True:
        password = input("\nEnter your password (or 'quit' to exit): ")
        
        if password.lower() == 'quit':
            print("Exiting Password Strength Meter...")
            break
            
        score = calculate_strength(password)
        provide_feedback(score, password)

if __name__ == "__main__":
    password_strength_meter()