Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import re
... 
... def check_password_strength(password):
...     length_error = len(password) < 8
...     digit_error = re.search(r"\d", password) is None
...     uppercase_error = re.search(r"[A-Z]", password) is None
...     lowercase_error = re.search(r"[a-z]", password) is None
...     symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None
... 
...     total_errors = sum([length_error, digit_error, uppercase_error, lowercase_error, symbol_error])
... 
...     if total_errors == 0:
...         return "Strong"
...     elif total_errors <= 2:
...         return "Moderate"
...     else:
...         return "Weak"
... 
... if __name__ == "__main__":
...     password = input("Enter your password: ")
...     strength = check_password_strength(password)
...     print(f"Password Strength: {strength}")
