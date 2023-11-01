
def login_and_signup():
    print("____ Login and SignUp System ____",end="\n\n")
    print('''            _____ Sign Up _____                      ''',end='\n\n')
    User_Name = input("Enter User Name : ")
    User_Password = input("Enter Password : ")

    print('''            _____ Login _____                      ''',end='\n\n')

    U_Name = input("Enter User Name : ")
    U_Password = input("Enter Password : ")

    if U_Name==User_Name and U_Password == User_Password:
        print("Login Successfully.")
    else:
        print("Invalid Credentials!")

login_and_signup()