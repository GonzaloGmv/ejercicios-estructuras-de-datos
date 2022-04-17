class ejer2:
    def __init__(self, primera, segunda):
        self.linea1 = primera
        self.linea2 = segunda
    
    def mayusculas(self):
        self.linea1 = self.linea1.upper()
        self.linea2 = self.linea2.upper()
    
    def escribir(self, fichero):
        self.mayusculas()
        f = open(fichero, 'a+')
        f.write(self.linea1)
        f.write('\n')
        f.write(self.linea2)
        f.close()