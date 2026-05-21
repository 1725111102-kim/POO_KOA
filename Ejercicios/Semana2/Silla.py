class Silla:
    def __init__(self, color, material, altura, peso, tipo, num_patas, respaldo, comodidad, resistencia, marca):
        self.color = color
        self.material = material
        self.altura = altura
        self.peso = peso
        self.tipo = tipo
        self.num_patas = num_patas
        self.respaldo = respaldo  # Ej. "Ergonómico", "Fijo", "Alto"
        self.comodidad = comodidad  # Ej. "Alta", "Media", "Baja"
        self.resistencia = resistencia  # En kilogramos
        self.marca = marca
        self.esta_ocupada = False
        self.inclinacion_actual = 0  # En grados

    def sentarse(self):
        if not self.esta_ocupada:
            self.esta_ocupada = True
            return "Alguien se ha sentado en la silla. Estado: Ocupada."
        return "La silla ya está ocupada por alguien más."

    def moverse(self, destino):
        return f"La silla de tipo '{self.tipo}' ha sido trasladada a: {destino}."

    def reclinarse(self, grados):
        if self.respaldo != "Fijo":
            self.inclinacion_actual = grados
            return f"El respaldo se inclinó {grados}°. Ángulo actual: {self.inclinacion_actual}°."
        return "No se puede reclinar; este modelo tiene un respaldo fijo."

    def girar(self, grados_giro):
        return f"La silla giró {grados_giro}° sobre su eje."

    def ajustarAltura(self, nueva_altura):
        self.altura = nueva_altura
        return f"La altura del asiento se ha modificado. Nueva altura: {self.altura} cm."


mi_silla = Silla(
    color="Negro",
    material="Malla sintética y metal",
    altura=95,
    peso=12.8,
    tipo="Oficina / Gamer",
    num_patas=5,
    respaldo="Ergonómico",
    comodidad="Alta",
    resistencia=120,
    marca="Herman Miller"
)

print(mi_silla.sentarse())
print(mi_silla.moverse("La sala de juntas"))
print(mi_silla.ajustarAltura(102))
print(mi_silla.reclinacion_actual)  # Muestra inclinación base (0)
print(mi_silla.reclinarse(15))
print(mi_silla.girar(180))
