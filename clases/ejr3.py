class Naturaleza:
    def __init__(self):
        self.ALIMENTARIA = 5.5
        self.SERVICIO = 20

class Producto:
    def __init__(self, iva):
        self.iva = iva
    
    def facturar(self):
        self.iva = 100 + self.iva
        return self.iva

class FactoryFactura(Producto):
    def crear(self):
        neto = Producto(self.iva)
        return neto