def check_password(password):
    if len(password) < 8:
        return False
    
    contains_letter = any(char.isalpha() for char in password)
    contains_number = any(char.isdigit() for char in password)

    if contains_letter and contains_number:
        return True
    else:
        return False

password = input("Please enter a password : ")

if check_password(password):
    print("Your password is valid. ")
else:
    print("Your password must contain at least 8 characters, and a mix of letters and numbers. ")
