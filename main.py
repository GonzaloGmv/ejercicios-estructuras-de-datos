from clases.ejr1 import *

if __name__ == '__main__':
    while True:
        ejr = input('Escriba el numero del ejercicio que desea ejecutar: ')
        try:
            ejr == '1' or ejr == '2' or ejr == '3'
        except:
            pass
        else:
            break
    if ejr == '1':
        mostrar_ok = Mostrar('"OK"') 
        mostrar_ko = Mostrar('"KO"') 
        alternativa = Si("2 + 2 == 4", mostrar_ok, mostrar_ko) 
        bloque_alternativa = Bloque() 
        bloque_alternativa.agregarInstruction(alternativa) 
        bucle = MientrasQue(True, bloque_alternativa) 
 