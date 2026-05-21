class Mesa:
    def __init__(self, color, material, altura, largo, ancho, peso, forma, num_patas, resistencia, marca):
        self.color = color
        self.material = material
        self.altura = altura
        self.largo = largo
        self.ancho = ancho
        self.peso = peso
        self.forma = forma
        self.num_patas = num_patas
        self.resistencia = resistencia
        self.marca = marca
        self.esta_limpia = True
        self.esta_armada = True

    def sostenerObjetos(self, peso_objeto):
        if peso_objeto <= self.resistencia:
            return f"La mesa sostiene el objeto con éxito. Soporta {self.resistencia} kg y se le colocaron {peso_objeto} kg."
        return f"¡Cuidado! El objeto pesa {peso_objeto} kg y supera la resistencia máxima de {self.resistencia} kg."

    def moverse(self, lugar):
        return f"La mesa de {self.material} ha sido movida hacia: {lugar}."

    def limpiarse(self):
        self.esta_limpia = True
        return "La mesa ha sido limpiada con un paño húmedo. Estado: Limpia."

    def desarmarse(self):
        if self.esta_armada:
            self.esta_armada = False
            return "Se han retirado las opciones de soporte y las {self.num_patas} patas. La mesa está desarmada."
        return "La mesa ya se encuentra desarmada."

    def ajustarAltura(self, nueva_altura):
        self.altura = nueva_altura
        return f"La altura de la mesa se ha regulado. Nueva altura: {self.altura} cm."


mi_mesa = Mesa(
    color="Roble claro",
    material="Madera",
    altura=75,
    largo=120,
    ancho=80,
    peso=15.4,
    forma="Rectangular",
    num_patas=4,
    resistencia=50,
    marca="IKEA"
)

print(mi_mesa.sostenerObjetos(20))
print(mi_mesa.moverse("El comedor"))
print(mi_mesa.limpiarse())
print(mi_mesa.ajustarAltura(80))
print(mi_mesa.desarmarse())
