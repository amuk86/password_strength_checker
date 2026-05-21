from user_input import user_password

password_strength_score = 0
special_characters = "!@#$%^&*"
numbers = "1234567890"


def check_nr_of_characters(user_password):
    global password_strength_score

    if len(user_password) >= 12:
        password_strength_score += 1
        return True
    else:
        print("Weak Password: Your password must contain at least 12 characters.")
        return False


def check_for_special_characters(user_password):
    global password_strength_score

    for character in user_password:
        if character in special_characters:
            password_strength_score += 1
            return True

    print("Weak Password: Your password must contain a special character (!@#$%^&*).")
    return False


def check_for_numbers(user_password):
    global password_strength_score

    for character in user_password:
        if character in numbers:
            password_strength_score += 1
            return True

    print("Weak Password: Your password must contain at least one number.")
    return False


def check_password_score(user_password):
    if password_strength_score >= 3:
        accepted_password = user_password
        print("Strong Password")
        return True
    else:
        print("Password not strong enough")
        return False


