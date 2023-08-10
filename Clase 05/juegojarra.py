class JuegoJarra(object):
    def __init__(self):
        self.jarra1 = 0
        self.jarra2 = 0
    def juego(self):
        print("Bienvenido al juego de la jarra \nTenes 2 jarras, una de 3 litros y otra de 5")
        print("Debes llenar la jarra 5 litros con 4 litros")
        print("Tenes 5 opciónes: \n1)Llenar la jarra de 3 litros \n2)Llenar la jarra de 5 litros \n3)Vaciar la jarra de 3 litros \n4)Vaciar la jarra de 5 litros \n5)Verter el contenido de la jarra de 3 litros en la de 5 litros \n6)Verter el contenido de la jarra de 5 litros en la de 3 litros ")
        eleccion = ""
        while self.jarra2 != 4:
            eleccion = input ("Elijí por su numero la opción que prefieras, escribí 'STOP' para parar el juego")
            try:
                if eleccion == "STOP":
                    print("Paraste el juego")
                    break
                else:
                    if type(int(eleccion)) == int:
                        if int(eleccion)>6:
                            print("Debes dara un numero que equivalga al de una de las opciones dadas, o bien escribir 'STOP para terminar con el juego")
                        elif eleccion == "1":
                            if self.jarra1 < 3:
                                self.jarra1 =3
                                print(f"el contenido de la jarra 1 es {self.jarra1}, el de la segunda es {self.jarra2}, seleccione su siguiente opción")
                            else:
                                print("la jarra está llena, seleccione otra opción")
                        elif eleccion == "2":
                            if self.jarra2 < 5:
                                self.jarra2 = 5
                                print(f"el contenido de la jarra 1 es {self.jarra1}, el de la segunda es {self.jarra2}, seleccione su siguiente opción")
                            else:
                                print("la jarra está llena, seleccione otra opción")
                        elif eleccion == "3":
                            self.jarra1 = 0
                            print(f"el contenido de la jarra 1 es {self.jarra1}, el de la segunda es {self.jarra2}, seleccione su siguiente opción")
                        elif eleccion == "4":
                            self.jarra2 = 0
                            print(f"el contenido de la jarra 1 es {self.jarra1}, el de la segunda es {self.jarra2}, seleccione su siguiente opción")
                            
                        elif eleccion == "5":
                            self.jarra2 += self.jarra1
                            jarraprovicional2 = self.jarra2
                            if self.jarra2 > 5:
                                    self.jarra2 = 5
                                    self.jarra1 =  jarraprovicional2 - self.jarra2
                            else:
                                self.jarra1 =0
                            print(f"el contenido de la jarra 1 es {self.jarra1}, el de la segunda es {self.jarra2}, seleccione su siguiente opción")
                            
                        elif eleccion == "6":
                            jarraprovicional2 = self.jarra2
                            self.jarra1 += self.jarra2
                            diferencia = self.jarra1 - 3
                            if self.jarra1 > 3:

                                    self.jarra1 = 3
                                    self.jarra2 = diferencia
                            else:
                                self.jarra2 = 0                
                            print(f"el contenido de la jarra 1 es {self.jarra1}, el de la segunda es {self.jarra2}, seleccione su siguiente opción")
                        else:
                            print("Asegurate de dar un numero, y SOLAMENTE un numero, sin espacios")
                            print(f"el contenido de la jarra 1 es {self.jarra1}, el de la segunda es {self.jarra2}, seleccione su siguiente opción")
            except:
                    print("Asegurate de dar un numero, y SOLAMENTE un numero, sin espacios")  
        if self.jarra2 == 4:    
            print("GANASTE!!! lograste llenar la jarra de 5 litros con 4 litros!")
juegojarra = JuegoJarra()
juegojarra.juego()    