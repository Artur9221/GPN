import unittest
import Testmain

class TestF(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_config(self):
        self.assertEqual(Testmain.ConFile(1),"2") #Time is two
        self.assertEqual(Testmain.ConFile(0),"opc.tcp://127.0.0.1:55000\n") 

   
    def test_flap(self):
        self.assertEqual(Testmain.type_flap("AI"), "AI")
        self.assertEqual(Testmain.type_flap("DI"), "DI")
        
    def test_flap_AI_DI(self):
        self.assertEqual(Testmain.flap_AI(50), 50)
        self.assertEqual(Testmain.flap_DI(1), True)        
    