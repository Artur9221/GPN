from opcua import Server
import datetime
import time

#read data from file
with open("OPC_Config.txt", "r") as f:
    config_ua=f.readlines()
    url=config_ua[0] #adress    
    Stime=int(config_ua[1])
    
server=Server()
#Url="opc.tcp://127.0.0.1:55000"
server.set_endpoint(url)
name ="OPCUA_SIMULATION_SERVER"
addspace=server.register_namespace(name) 
node=server.get_objects_node()
Param=node.add_object(addspace,"Parameters")
ValueAI=Param.add_variable(addspace, "SignalAI",0)
ValueDI=Param.add_variable(addspace, "SignalDI",0)
Time=Param.add_variable(addspace, "Time",0)

ValueAI.set_writable()
ValueDI.set_writable()
Time.set_writable()

server.start()

print("Server started at {}".format(url))
while True:
    AI=ValueAI.get_value()
    DI=ValueDI.get_value()
    TIME=datetime.datetime.now()
    print("ValueIA is {}".format(AI),":","ValueID is {}".format(bool(DI)),":", TIME)
    Time.set_value(TIME)
    time.sleep(Stime)