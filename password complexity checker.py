import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Criteria checks
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Length check
    if not length_error:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Lowercase
    if not lowercase_error:
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    # Uppercase
    if not uppercase_error:
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    # Digits
    if not digit_error:
        score += 1
    else:
        feedback.append("Include at least one number.")

    # Special Characters
    if not special_char_error:
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*, etc).")

    # Final assessment
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

# Example usage
if __name__ == "__main__":
    password = input("Enter your password: ")
    strength, suggestions = check_password_strength(password)

    print(f"\nPassword strength: {strength}")
    if suggestions:
        print("Suggestions to improve your password:")
        for tip in suggestions:
            print(f"- {tip}")
