from user import User
def menuPrincipal():
    print("#Bee.Hive#")
    print("Store| Labs | Thinks | Log in")
    print("_____________________________")
    print("Insert here, one of the members pages")
    print("Insert here, one of the members pages")
    print("Insert here, one of the members pages")
    
    while True:
        landingPageOption = input("type where do you wanna go:")
        if landingPageOption in ['store','Store']:
            storePages()
            break
        elif landingPageOption in ['labs','Labs']:
            labsPages()
            break
        elif landingPageOption in ['Thinks','thinks']:
            thinksPages()
            break
        elif landingPageOption in ['Login','login']:
            logIn()
        else:
            continue
        
def storePages():
    print("welcome to store pages")
def labsPages():
    print("welcome to the labs pages")
    
def thinksPages():
    print("welcome to the thinks pages")
    
def logIn():
    while True:
        option = input("LogIn or SignUp:")
        if option in ['SignUp', 'signup']:
            valid = False
            while valid == False:
                newUsername = input("Type your username:")
                newpassword = input("Type your password:")
                newUser = User(newUsername,newpassword)
                valid=newUser.dataStoring()
            break
        elif option in ['LogIn', 'login']: 
            valid = False
            while valid == False:
                username = input("username:")
                password = input("password:")
                user = User(username,password)
                valid=user.userExists()
            break
        
menuPrincipal()