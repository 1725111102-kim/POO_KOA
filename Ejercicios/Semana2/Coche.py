class Coche:
    def __init__(self, marca, modelo, color, ano, velocidad_maxima, combustible, num_puertas, matricula, kilometraje, capacidad_pasajeros):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.ano = ano
        self.velocidad_maxima = velocidad_maxima
        self.combustible = combustible
        self.num_puertas = num_puertas
        self.matricula = matricula
        self.kilometraje = kilometraje
        self.capacidad_pasajeros = capacidad_pasajeros
        self.encendido = False

    def arrancar(self):
        self.encendido = True
        return f"El {self.marca} {self.modelo} ha arrancado."

    def acelerar(self):
        return f"El {self.marca} está aumentando su velocidad."

    def frenar(self):
        return f"El {self.marca} ha frenado y se ha detenido."

    def estacionarse(self):
        return f"El {self.marca} se ha acomodado y estacionado correctamente."

    def tocarClaxon(self):
        return "¡Bip, bip! El coche está tocando el claxon."


# Creando el objeto pasando únicamente los valores en el orden correcto
mi_coche = Coche("Subaru", "WRX", "Azul", 2025, "250 km/h", "Gasolina", 4, "WRX-2025", 0, 5)

# Probando los métodos
print(mi_coche.arrancar())
print(mi_coche.acelerar())
print(mi_coche.tocarClaxon())
print(mi_coche.frenar())
print(mi_coche.estacionarse())
