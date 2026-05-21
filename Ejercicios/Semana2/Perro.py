class Perro:
    def __init__(self, color, raza, tamano, num_patas, peso, pelaje, orejas, temperamento, sexo, resistencia):
        self.color = color
        self.raza = raza
        self.tamano = tamano
        self.num_patas = num_patas
        self.peso = peso
        self.pelaje = pelaje
        self.orejas = orejas
        self.temperamento = temperamento
        self.sexo = sexo
        self.resistencia = resistencia

    def corre(self, distancia):
        self.resistencia -= 15
        return f"El perro corre {distancia} metros. Resistencia actual: {self.resistencia}"

    def come(self, porcion):
        self.peso += porcion * 0.1
        return f"El perro come su alimento. Nuevo peso: {self.peso:.2f} kg"

    def ladra(self):
        return f"El perro de temperamento {self.temperamento} está ladrando fuerte: ¡Guau, guau!"

    def duerme(self):
        self.resistencia = 100
        return "El perro se ha quedado dormido y recuperó toda su resistencia."

    def cuidaLaCasa(self):
        return f"El perro está alerta sobre sus {self.num_patas} patas, vigilando y cuidando la casa."


mi_perro = Perro(
    color="Café",
    raza="Pastor Alemán",
    tamano="Grande",
    num_patas=4,
    peso=32.5,
    pelaje="Largo y denso",
    orejas="Erguidas",
    temperamento="Protector",
    sexo="Macho",
    resistencia=85
)

print(mi_perro.ladra())
print(mi_perro.corre(50))
print(mi_perro.come(2))
print(mi_perro.cuidaLaCasa())
print(mi_perro.duerme())
