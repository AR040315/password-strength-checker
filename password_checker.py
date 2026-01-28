def check_password_strength(password):

    has_digit = False
    has_upper = False
    has_lower = False
    has_symbol = False

    for ch in password:
        if ch.isdigit():
            has_digit = True
        elif ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch in "!@#$%^&*":
            has_symbol = True

    length_ok = len(password) >= 8

    score = 0

    if length_ok:
        score += 1
    if has_digit:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_symbol:
        score += 1

    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Moderate"
    else:
        return "Weak"


password = input("Enter your password: ")
print("Password Strength:", check_password_strength(password))
