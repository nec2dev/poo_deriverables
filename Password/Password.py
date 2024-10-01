class Password:
  def __init__(self, longitud = 8, password = None):
    self.longitud = longitud
    # self.password = self.generar_password()
    self.password = "1d2/3r4f56RR*R"

  def __str__(self):
    return f"Contraseña: {self.password} Longitud: {self.longitud}"
  
  def generar_password(self):
    # Iterar la cantidad de longitud
    # En cada vuelta generar un caracter random 
    # agregarlo al password del objeto de tipo Password
    pass
  
  def get_longitud(self):
     return self.longitud
  
  def get_password(self):
     return self.password
  
  def es_fuerte(self):
     
     cont_mayusculas = 0
     cont_minusculas = 0
     cont_numeros = 0

     for caracter in self.password:
        if caracter.isupper():
            cont_mayusculas += 1
        elif caracter.islower():
            cont_minusculas += 1
        elif caracter.isnumeric():
           cont_numeros += 1
        
    #  return f"cont_mayusculas: {cont_mayusculas}\ncont_minusculas: {cont_minusculas}\ncont_numeros: {cont_numeros}\n"

     if (cont_mayusculas > 2 and cont_minusculas >= 2 and cont_numeros > 5 ):
        return True
     else:
        return False

# Test de la clase
contranea01 = Password(9, "Er3412Q90") 
contranea02 = Password(15)
contranea03 = Password()

print(contranea01)
print(contranea02)
print(contranea03)

fortaleza_de_contranae1 = contranea01.es_fuerte()
print(fortaleza_de_contranae1)

