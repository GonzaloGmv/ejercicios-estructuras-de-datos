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