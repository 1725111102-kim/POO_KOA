class PikachuRpg:
    def __init__(self, nombre, tipo_electrico, nivel, vida, energia, velocidad, ataque, defensa, experiencia, habilidad_especial):
        self.nombre = nombre
        self.tipo_electrico = tipo_electrico  # Ej. True si es eléctrico puro, o el tipo secundario
        self.nivel = nivel
        self.vida = vida
        self.energia = energia
        self.velocidad = velocidad
        self.ataque = ataque
        self.defensa = defensa
        self.experiencia = experiencia
        self.habilidad_especial = habilidad_especial

    def atacar(self):
        return f"{self.nombre} realiza un ataque físico básico causando daño."

    def lanzarElectricidad(self):
        self.energia -= 15
        return f"¡{self.nombre} usa un ataque de tipo {self.tipo_electrico}! Energía restante: {self.energia}."

    def esquivarAtaques(self):
        return f"¡Gracias a su velocidad de {self.velocidad}, {self.nombre} esquivó el ataque enemigo!"

    def subirDeLevel(self):
        self.nivel += 1
        self.ataque += 5
        self.defensa += 3
        return f"¡{self.nombre} subió al nivel {self.nivel}! Sus estadísticas aumentaron."

    def evolucionar(self):
        self.nombre = "Raichu"
        return f"¡Felicidades! Tu Pikachu ha evolucionado a {self.nombre}."


# Creando el objeto pasando únicamente los valores en el orden correcto
mi_pikachu = PikachuRpg("Pikachu de Ash", "Eléctrico", 25, 120, 80, 90, 55, 40, 2500, "Electricidad Estática")

# Probando los métodos
print(mi_pikachu.atacar())
print(mi_pikachu.lanzarElectricidad())
print(mi_pikachu.esquivarAtaques())
print(mi_pikachu.subirDeLevel())
print(mi_pikachu.evolucionar())
