from abc import ABC, abstractmethod
class Flap(ABC):
    __m_ValueIA=0
    __m_ValueID=False
#общий метод, который будут использовать все наслденики этого класса
    def Flap(self):
        print("valve parent")
#абстрактный метод, который будет необходимо переопределять для каждого подкласса
    @abstractmethod
    def set_value(self,Value):
        pass
    @abstractmethod
    def get_value(self):
        pass

class Flap_AI(Flap):
    def set_value(self,Value):
        self.__m_ValueIA=Value
    
    def get_value(self): 
        return self.__m_ValueIA   

class Flap_DI(Flap):    
    def set_value(self,Value):
        self.__m_ValueID=Value  
    def get_value(self): 
        return self.__m_ValueID  