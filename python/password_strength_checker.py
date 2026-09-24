def check_password_strength(password):
    try:
        if len(password) < 6:
            raise ValueError("Password must contain at least 6 characters.")

        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False

        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True
            else:
                has_special = True

        if has_upper and has_lower and has_digit and has_special:
            return "Strong Password"
        elif has_upper and has_lower and has_digit:
            return "Medium Password"
        else:
            return "Weak Password"

    except ValueError as e:
        return str(e)


# Main program
password = input("Enter your password: ")

result = check_password_strength(password)

print("Result:", result)