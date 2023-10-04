class Pontos():
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def printPontos(self):
        print(f'\nOs pontos inseridos foram {self.x}, {self.y}, {self.z}')
        
        
class Circulo(Pontos):
    def __init__(self, x, y, raio):
        self.x = x
        self.y = y
        self.raio = raio
    
    def printaCirculo(self):
        print(f'\nInformações do Círculo: Origem em X:{self.x}, Y:{self.y}, Raio: {self.raio}')
    
    def calculaArea(self):
        print ('A área do seu Círculo é: ',3.14 * self.raio  / 2)
        






def Main():
    pt1 = Pontos(4, 6, 8)
    pt1.printPontos()
    
    circulo1 = Circulo(4, 8, 24)
    circulo1.printaCirculo()
    circulo1.calculaArea()
    
    
    
if __name__ == "__main__":
    Main()
