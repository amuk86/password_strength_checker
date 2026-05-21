from input_handler import check_nr_of_characters, check_for_special_characters, check_for_numbers, check_password_score
from user_input import user_password
if check_nr_of_characters(user_password) and check_for_special_characters(user_password) and check_for_numbers(user_password):
    if check_password_score(user_password):
        print("Your password is strong and has been accepted.")
    else:
        print("Your password is weak and has not been accepted.")
        