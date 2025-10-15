### Password Validator

## --- Password Requirements: ---
# 1. length >= 8
# 2. at least a uppercase letter
# 3. at least a lowercase letter
# 4. at least a digit
# 5. at least a special carachter

## --- Password Classificaton: ---
# 1. WEAK: meets the first requirement but fails some others
# 2. MEDIUM: meets all requirements and is between 8-11 chars
# 3. STRONG: meets all requirements and is between 12-15 chars
# 4. VERY STRONG: meets all requirements and is between 16+ chars
# 5. INVALID: doesn't meet the length requirement


def validate_password(password: str) -> str:
    length = len(password)
    min_length_requirement = length >= 8
    uppercase_requirement = any(char.isupper() for char in password)
    lowercase_requirement = any(char.islower() for char in password)
    digit_requirement = any(char.isdigit() for char in password)
    special_char_requirement = any(not char.isalnum() for char in password)
    all_requirements = (
        uppercase_requirement
        and lowercase_requirement
        and digit_requirement
        and special_char_requirement
    )

    if not min_length_requirement:
        return "INVALID"
    elif min_length_requirement and (not all_requirements):
        return "WEAK"
    elif all_requirements and (8 <= length <= 11):
        return "MEDIUM"
    elif all_requirements and (12 <= length <= 15):
        return "STRONG"
    elif all_requirements and (length >= 16):
        return "VERY STRONG"


def main() -> None:
    password = input("Insert a password: ")
    feedback = validate_password(password.strip())

    print(f"Your password is: {feedback}")


if __name__ == "__main__":
    main()
