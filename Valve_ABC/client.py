from opcua import Client
class Start_Client:
#read data from file
    def ConFile(n):
        with open("OPC_Config.txt", "r") as f:
            config_ua=f.readlines()
            return config_ua[n]
    
    
    __c_ValueIA=0
    __c_ValueID=False
    __c_url=ConFile(0)   
    
    def c_set_value_AI(self,Value):
        self.__c_ValueIA=Value
        client=Client(self.__c_url)
        client.connect()
        ValueIA=client.get_node("ns=2;i=2")
        #print("Initial value:{}".format(var.get_value()))
        ValueIA.set_value(self.__c_ValueIA)
        client.disconnect()
        
    def c_set_value_DI(self,Value):
        self.__c_ValueIA=Value
        client=Client(self.__c_url)
        client.connect()
        ValueIA=client.get_node("ns=2;i=3")
        #print("Initial value:{}".format(var.get_value()))
        ValueIA.set_value(self.__c_ValueIA)
        client.disconnect()   