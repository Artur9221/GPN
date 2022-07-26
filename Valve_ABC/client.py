from opcua import Client
class Start_Client:
    __c_ValueIA=0
    __c_ValueID=False
    __c_url="opc.tcp://127.0.0.1:55000"   
    
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