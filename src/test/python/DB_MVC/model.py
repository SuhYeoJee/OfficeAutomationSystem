from db_interface import DBInterface
from igzg.utils import getConfig
from pprint import pprint

class Model:
    def __init__(self):
        self.dbi = DBInterface(*getConfig(['username','password','database','port']))

    def dbi_test(self):
        res = self.dbi.execute_query("SELECT DISTINCT * FROM `powder` ; ")
        pprint(res)

def model_test():
    m = Model()
    m.dbi_test()
    

if __name__ == "__main__":
    model_test()