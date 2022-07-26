from flap import Flap_AI, Flap_DI
from client import Start_Client

flap_AI=Flap_AI()
flap_DI=Flap_DI()
client=Start_Client()


while True:
    type_flap=input("Выберете тип клапана (AI,DI):")
    
    if type_flap=="AI":
        while True:
            try:
                num = int(input("Открыть клапан:"))
                if  0 <= num <= 100:
                    print("Клапан открыт на:", num, "%")
                    flap_AI.set_value(num)
                    client.c_set_value_AI(num)
                    break
            except Exception:
                print("Ведите цело число") 
             
             
                
    if type_flap=="DI":
        while True:
            try:
                flag = int(input("Открыть/Закрыть клапан - (True(1)/False(0)): "))
                if  (flag==1):
                    print("Клапан-Открыт: True")
                    flap_DI.set_value(flag)
                    client.c_set_value_DI(flag)
                    break
                if  (flag==0):
                    print("Клапан-Закрыт: False")
                    flap_DI.set_value(flag)
                    client.c_set_value_DI(flag)
                    break
                else:
                    print("Введите число 0 или 1: ")
            except Exception:
                print("Ведите цело число 0 или 1:") 
                
    if type_flap!="AI" and  type_flap!="DI":
        print("Данного типа не существует") 
    
    
