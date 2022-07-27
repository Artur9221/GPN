"Server"
"Function for reading data from txt"
def ConFile(n):#read data from file
    with open("OPC_Config.txt", "r") as f:
        config_ua=f.readlines()
        print("URL {}".format(config_ua[0]), "Time {}".format(config_ua[1]))
        return config_ua[n]
    
"Client"
"check on input value"
def type_flap(flap):
    if flap=="AI":
        return "AI"
    elif flap=="DI":
        return "DI"    
    else:          
        print("this type does not exist")

def flap_AI(num):
    if  0 <= num <= 100:
        return num
    else:
        print("Ведите цело число") 


def flap_DI(num):
    if  num==1:
        return True
    elif num==0:
        return False
    else:
        print("Введите число 0 или 1:") 

