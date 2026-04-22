def check_list_in_string(string, check_list, must):
    if must == True:
        for element in check_list:
            if string.count(element) != 0:
                return True
        return False
    else:
        for element in check_list:
            if string.count(element) != 0:
                return False
        return True
    return -1


def get_and_validate_password():
    password_is_valid = False
    must_have = ["!", "$"]
    cant_have = ["password"]
    while not password_is_valid:
        password = input("New password: ")
        if 10 <= len(password) <= 20:
            print("Password has the right length OK!")
            if check_list_in_string(password, must_have, True):
                print("Password has a $ or a ! OK!")
                if check_list_in_string(password, cant_have, False):
                    print("Password is OK!")
                    password_is_valid = True
                else:
                    print("Password can not contain the string \"password\"")
            else:
                print("Password must either have a \"$\" or a \"!\"")
        else:
            print("Password not the right length (between 10 - 20 characters, try again")
    return password


def main():
    valid_password = get_and_validate_password()
    print("The chosen password is", valid_password)
    #  print(check_list_in_string("Hello World!", ["!@", "$", "password"]))


if __name__ == "__main__":
    main()

