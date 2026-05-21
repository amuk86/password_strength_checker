from user_input import user_password

password_strength_score = 0
special_characters ="!@#$%^&*"
numbers="1234567890"

def check_nr_of_characters(user_password):
    check_nr_of_characters=len(user_password)
    if check_nr_of_characters>12:
        password_strength_score+=1
        return True
    else:
        password_strength_score-=1
        print("Weak Password: Your password does not contain the minimum 12 characters")
        return False
    

def check_for_special_characters(user_password):
    for characters in user_password:
        if characters in special_characters:
            password_strength_score+=1
            return True
        else:
            password_strength_score-=1
            print("Weak Password: Your password does not contain the special characters '!@#$%^&*'")
            return False
    
def check_for_numbers(user_password):
    for number in user_password:
        if number in numbers:
            password_strength_score+=1
            return True
        else:
            password_strength_score-=1
            print("Weak Password: Your password must have atleast one number, '0123456789'.")
            return False

def check_password_score(user_input):
    if password_strength_score>2:
        accepted_password=user_input
        return True
    else:
        return False
