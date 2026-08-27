class Endereco:
    
    def __init__(self,uf,cidade):
        self.__uf = uf
        self.__cidade = cidade
        
@property
def uf(self):
    return self.__uf

@uf.Setter
def uf(self,uf):
    self.__uf = uf
        
@property
def cidade(self):
    return self.__cidade    
    
@cidade.setter(self,cidade):
def cidade(self)    
    self.__cidade = cidade
    
 def obter_endereco(self):
        return f"{self.__uf}, {self.__cidade}"
        
    
    
class Pessoa:
    def __init__(self,nome):
            self.__nome = NotImplemented
            
@property
def nome(self):
    return self.__nome    

@nome.setter
def nome(self,nome):
    self.__nome = nome
    
def apresentar_endereco(self):
    print(f"Nome: {self.__nome}")
    print(f"Enderço: {self.__endereco()}")
        