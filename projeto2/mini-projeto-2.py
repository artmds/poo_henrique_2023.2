class Pontos():
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def printPontos(self):
        print(f'\n Os pontos inseridos foram {self.a}, {self.b}, {self.c}')
        







def Main():
    pt1 = Pontos(4, 6, 8)
    pt1.printPontos()
    
    
    
    
    
if __name__ == "__main__":

    Main()
