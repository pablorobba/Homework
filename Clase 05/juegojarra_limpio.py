"""
versión limpia y con funciones del código anterior, repitiendo menos código

"""
class JuegoJarra(object):
    def __init__(self):
        self.jarra1 = 0
        self.jarra2 = 0
    def llenar_jarra1(self):
        self.jarra1 = 3
    def llenar_jarra2(self):
        self.jarra2 = 5
    def vaciar_jarra1(self):
        self.jarra1 = 0
    def vaciar_jarra2(self):
        self.jarra2 = 0
    def vertir_jarra1(self):
        self.jarra2 += self.jarra1
        jarraprovicional2 = self.jarra2
        if self.jarra2 > 5:
            self.jarra2 = 5
            self.jarra1 =  jarraprovicional2 - 5       #calcula la diferencia que queda en la jarra uno al vertir su contenido en la segunda jarra
        else:
            self.jarra1 = 0
    def vertir_jarra2(self):
        self.jarra1 += self.jarra2
        diferencia = self.jarra1 - 3
        if self.jarra1 > 3:
            self.jarra1 = 3
            self.jarra2 = diferencia
        else:
            self.jarra2 = 0
    def main (self):
        #se imprimen a continuación las instrucciones del juego
        print("Bienvenido al juego de la jarra \nTenes 2 jarras, una de 3 litros y otra de 5")
        print("Debes llenar la jarra 5 litros con 4 litros")
        print("Tenes 5 opciónes: \n1)Llenar la jarra de 3 litros \n2)Llenar la jarra de 5 litros \n3)Vaciar la jarra de 3 litros \n4)Vaciar la jarra de 5 litros \n5)Verter el contenido de la jarra de 3 litros en la de 5 litros \n6)Verter el contenido de la jarra de 5 litros en la de 3 litros ")
        eleccion = ""       #variable que almacena la elección que se realiza con el input
        while self.jarra2 != 4:     #ciclo que inicia el juego y vérifica cuando ganes o lo pares
            eleccion = input ("Elijí por su numero la opción que prefieras, escribí 'STOP' para parar el juego")    #pregunta en cada iteración
            try:
                if eleccion == "STOP":      
                    print("Paraste el juego")
                    break
                else:
                    if type(int(eleccion)) == int:
                        if int(eleccion)>6:
                            print("Debes dar un numero que equivalga al de una de las opciones dadas, o bien escribir 'STOP' para terminar con el juego")
                        elif eleccion == "1":
                            self.llenar_jarra1()
                        elif eleccion == "2":
                            self.llenar_jarra2()
                        elif eleccion == "3":
                            self.vaciar_jarra1()
                        elif eleccion == "4":
                            self.vaciar_jarra2()
                        elif eleccion == "5":
                            self.vertir_jarra1()
                        elif eleccion == "6":
                            self.vertir_jarra2()     
                        else:
                            print("Asegurate de dar un numero, y SOLAMENTE un numero, sin espacios, o bien escribe 'STOP' para terminar el juego") 
                        
                        print(f"el contenido de la jarra 1 es {self.jarra1}, el de la segunda es {self.jarra2}, seleccione su siguiente opción")    #mostrará el contenido de la jarra cada vez que realices una elección
            except:
                    print("Asegurate de dar un numero, y SOLAMENTE un numero, sin espacios, o bien escribe 'STOP' para terminar el juego")            
        if self.jarra2 == 4:    
            print("GANASTE!!! lograste llenar la jarra de 5 litros con 4 litros!")


variable_que_inicia_juego = JuegoJarra()

if __name__ == "__main__":
    variable_que_inicia_juego.main()