
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
            break
        else:
            continue
        
def storePages():
    print("welcome to store pages")
def labsPages():
    print("welcome to the labs pages")
    
def thinksPages():
    print("welcome to the thinks pages")
    
def logIn():
    print("welcome to log in")



menuPrincipal()