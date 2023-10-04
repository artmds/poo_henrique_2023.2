class Pontos():
    
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z
    
    def printPontos(self):
        print(f'\nOs pontos inseridos foram {self._x}, {self._y}, {self._z}')
        
#Classe Circulo
class Circulo(Pontos):
    def __init__(self, raio):
        self._raio = raio
    
    def printaCirculo(self):
        print(f'\nInformações do Círculo: Raio: {self._raio}')
    
    def calculaArea(self):
        print ('A área do seu Círculo é: ',3.14 * self._raio  / 2)
        
#Classe Quadrado
class Quadrado(Pontos):
    def __init__(self, lado):
        self._lado = lado
    
    
    def printaQuadrado(self):
        print(f'\nSeu quadrado possui possui lado:{self._lado}')
        
        
    def calculaAreaQuadrado(self):
        print ('A área do seu quadrado é: ', self._lado ** 2)


class Triangulo(Pontos):
    def __init__(self, b, h):
        self._b = b
        self._h = h
    
    def printaTriangulo(self):
        print(f'\nSeu Triângulo possui base:{self._b} e altura:{self._h}')
    
    def calculaAreaTriangulo(self):
        print("A área do seu triângulo é de:", self._b * self._h / 2)


class Retangulo(Pontos):
    def __init__(self, b, h):
        self._b = b
        self._h = h
    
    def printaRetangulo(self):
        print(f'\nSeu Retângulo possui base:{self._b} e altura:{self._h}')
    
    def calculaAreaRetangulo(self):
        print("A área do seu reângulo é de:", self._b * self._h)


def Main():
    
    print("\nOlá, seja bem vindo! :)\n")
    
    pt1 = Pontos(4, 6, 8)
    pt1.printPontos()
    
    print("-------------\n")
    
    circulo1 = Circulo(24)
    circulo1.printaCirculo()
    circulo1.calculaArea()
    
    print("-------------\n")
    
    quadrado1 = Quadrado(4)
    quadrado1.printaQuadrado()
    quadrado1.calculaAreaQuadrado()
    
    print("-------------\n")
    
    triangulo1 = Triangulo(5, 5)
    triangulo1.printaTriangulo()
    triangulo1.calculaAreaTriangulo()
    
    print("-------------\n")

    retangulo1 = Retangulo(5, 2)
    retangulo1.printaRetangulo()
    retangulo1.calculaAreaRetangulo()
    
    print("-------------\n")

if __name__ == "__main__":
    Main()
