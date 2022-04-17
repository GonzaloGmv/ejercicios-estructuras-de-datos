# ejercicios-estructuras-de-datos

El link al repositorio es: [ github](https://github.com/GonzaloGmv/ejercicios-estructuras-de-datos)

# Ejercicio 1

El código de este ejercicio es:
```
class Bloque: 
    # Un bloque es un conjunto de instrucciones ejecutadas 
    # unas detrás de otras. 
    def __init__(self): 
        # Por defecto, un bloque no contiene ninguna instrucción. 
        self.instrucciones = [] 
 
    def agregarInstruction(self, instruccion): 
        self.instrucciones.append(instruccion) 
 
class Si: 
    # Representa una instrucción 'if'. 'condicion' es una cadena 
    # de caracteres que contiene la evaluación de la condición, 
    # 'entonces' es el bloque de instrucciones ejecutadas si la condición 
    # se verifica, 'si_no' es el bloque de instrucciones ejecutadas 
    # si no se verifica. 
 
    def __init__(self, condicion, entonces, si_no): 
        self.condicion = condicion 
        self.entonces = entonces 
        self.si_no = si_no 
 
class MientrasQue: 
    # Representa una instrucción 'while'. 
    # 'condicion' es una cadena que contiene el valor evaluado 
    # para decidir si el bucle continúa o no, 
    # 'bloque' es la secuencia de instrucciones ejecutadas en bucle. 
    def __init__(self, condicion, bloque): 
        self.condicion = condicion 
        self.bloque = bloque 
 
class Mostrar: 
    # Una instrucción para mostrar un mensaje 
    # en salida estándar. 
    def __init__(self, mensaje): 
        self.mensaje = mensaje 
```

# Ejercicio 2

El código de este ejercicio es:
```
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
```

# Ejercicio 3

El código de este ejercicio es:
```
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
```

# Main

El código del main es el siguiente:
```
from clases.ejr1 import *
from clases.ejr2 import *
from clases.ejr3 import *

def ejecutar():
        ejr = input('Escriba el numero del ejercicio que desea ejecutar: ')

        if ejr == '1':
            mostrar_ok = Mostrar('"OK"') 
            mostrar_ko = Mostrar('"KO"') 
            alternativa = Si("2 + 2 == 4", mostrar_ok, mostrar_ko) 
            bloque_alternativa = Bloque() 
            bloque_alternativa.agregarInstruction(alternativa) 
            bucle = MientrasQue(True, bloque_alternativa)
    
        elif ejr == '2':
            ejercicio = ejer2(input('Escriba la primera linea: '), input('Escriba la segunda linea: '))
            ejercicio.escribir(input('Escriba el nombre del archivo que quiere crear: '))
        
        elif ejr == '3':
            naturaleza = Naturaleza()

            producto = Producto(naturaleza.ALIMENTARIA) # IVA 5,5% 
            precio_neto = FactoryFactura.crear(producto).facturar() 
            print(precio_neto)
            
            producto = Producto(naturaleza.SERVICIO) # IVA 20% 
            precio_neto = FactoryFactura.crear(producto).facturar() 
            print(precio_neto)
        
        else:
            ejr = ejecutar()

if __name__ == '__main__':
    ejecutar()
```   
