def assess_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    special_characters = "!@#$%^&*'(),.?\":{}|<>+=-_~"
    if any(char in special_characters for char in password):
        score += 1

    if score <= 2:
        return "Very Weak"
    elif score == 3:
        return "Weak"
    elif score == 4:
        return "Moderate"
    elif score == 5:
        return "Strong"
    else:
        return "Very Strong"


password = input("Enter a password to assess its strength: ")
strength = assess_password_strength(password)
print(f"Password Strength: {strength}")
