class Transporte:
    def __init__(self, tipo, capacidad, color, velocidad_maxima, combustible, peso, marca, modelo, num_ruedas, ventanas):
        self.tipo = tipo
        self.capacidad = capacidad
        self.color = color
        self.velocidad_maxima = velocidad_maxima
        self.combustible = combustible
        self.peso = peso
        self.marca = marca
        self.modelo = modelo
        self.num_ruedas = num_ruedas
        self.ventanas = ventanas
        self.encendido = False

    def encender(self):
        self.encendido = True
        return f"El {self.tipo} se ha encendido."

    def acelerar(self):
        return f"El {self.tipo} está aumentando su velocidad."

    def frenar(self):
        return f"El {self.tipo} ha frenado."

    def transportarPersonas(self):
        return f"El {self.tipo} está llevando a los pasajeros a su destino."

    def apagar(self):
        self.encendido = False
        return f"El {self.tipo} se ha apagado."


# Creando y probando el objeto de forma directa
mi_transporte = Transporte(
    tipo="Autobús",
    capacidad=40,
    color="Amarillo",
    velocidad_maxima=110,
    combustible="Diésel",
    peso="8 toneladas",
    marca="Mercedes-Benz",
    modelo="Ayco",
    num_ruedas=6,
    ventanas=14
)

print(mi_transporte.encender())
print(mi_transporte.transportarPersonas())
print(mi_transporte.acelerar())
print(mi_transporte.frenar())
print(mi_transporte.apagar())
