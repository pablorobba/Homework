import random
class Juego (object):
    def __init__(self):
       self.__lista = []
    def crear_lista(self):
        self.__lista = [i for i in range(1,21)]
    def pop(self):
        return self.__lista.pop()
    def desordenar (self):
        return random.shuffle(self.__lista)         
    def play(self):   
        self.crear_lista()
        self.desordenar()
        cantidad_eliminados = int(input("ingresa el numero de elementos a eliminar"))      
        eliminados_lista = []                       #creación de lista de numeros eliminados, para sumarlos luego
        for _ in range(cantidad_eliminados):            
            eliminados = self.pop()
            eliminados_lista.append(eliminados)       
        suma = sum(eliminados_lista)
        print(self.__lista)
        print(f"los numeros eliminados fueron: {eliminados_lista}")
        
        if suma < 50:
            print(f"el total de los eliminados sumados es {suma}, que es menos que 50, por lo tanto GANASTE!")
            v = suma 
            contador = 0                    #contador que contará los elementos que se necesitan para llegar a 50
            puntaje = 10                    # que luego se le restarán al puntaje
            for e in self.__lista:          #ciclo que se usa para añadir numeros al contador
                v += e 
                contador += 1
                if v >= 50:               
                    break                   
            puntaje -= contador
            print(f"y tu puntaje fue de {puntaje + 1}")         #se le suma uno al puntaje porque el ciclo para y suma la ultima vuelta para llegar a 50
        else:
            print(f"el total de los eliminados sumados es {suma}, que es más que 50, perdiste ")
            
juego = Juego()
juego.play()