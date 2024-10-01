class Ejecutable:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.lineas = self.leer_archivo()