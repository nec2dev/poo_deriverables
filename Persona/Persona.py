from random import randint

class Persona: 
    def __init__(self, nombre=None, edad=None, DNI=0, sexo=None, peso=0.0, altura=0.0, color_pelo="pelado"):
        self.__nombre = nombre
        self.__edad = edad
        self.__DNI = DNI or self.__generaDNI(self)
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura
        self.__color_pelo = color_pelo
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def set_edad(self, edad):
        self.__edad = edad
    
    def set_DNI(self, DNI):
        self.__DNI = DNI
    
    def set_sexo(self, sexo):
        self.__sexo = sexo
    
    def set_peso(self, peso):
        self.__peso = peso
    
    def set_altura(self, altura):
        self.__altura = altura
    
    def set_color_pelo(self, color_pelo):
        self.__color_pelo = color_pelo

    def calcularIMC():
        print("Calcular IMC")
    
    def esMayorDeEdad():
        print("Es mayor de edad")

    def __str__(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}, DNI: {self.__DNI}, Sexo: {self.__sexo}, Peso: {self.__peso}kg, Altura: {self.__altura}m, Color de pelo: {self.__color_pelo}"
    
    def __generaDNI():
        print("Generar DNI")
    
persona01 = Persona() # instanciado con el constructor por defecto
persona01.set_nombre("Nahuel")
persona01.set_edad(45)
persona01.set_DNI(27380680)
persona01.set_sexo("M")
persona01.set_peso(70)
persona01.set_altura(163)
persona01.set_color_pelo("Castaño")


persona02 = Persona(nombre = "Nahuel", edad = 45, sexo = "M") # instanciado con el constructor por defecto


nombre_input = input("Nombre: ")
edad_input = input("Edad: ")
dni_input = input("DNI: ")
sexo_input = input("Sexo: ")
peso_input = input("Peso: ")
alt_input = input("Altura: ")
color_input = input("Color de pelo: ")
persona03 = Persona(nombre_input, edad_input, dni_input, sexo_input, peso_input, alt_input, color_input)

print(persona01)
print(persona02)
print(persona03)

