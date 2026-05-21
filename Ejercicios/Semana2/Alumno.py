class Alumno:
    def __init__(self, nombre, edad, matricula, carrera, semestre, promedio, correo_electronico, telefono, direccion, escuela):
        self.nombre = nombre
        self.edad = edad
        self.matricula = matricula
        self.carrera = carrera
        self.semestre = semestre
        self.promedio = promedio
        self.correo_electronico = correo_electronico
        self.telefono = telefono
        self.direccion = direccion
        self.escuela = escuela

    def estudiar(self):
        return f"{self.nombre} está estudiando para sus próximas evaluaciones."

    def presentarExamen(self):
        return f"{self.nombre} ha presentado su examen de la carrera de {self.carrera}."

    def entregarTareas(self):
        return f"Las tareas del semestre {self.semestre} han sido enviadas al profesor."

    def asistirAClases(self):
        return f"{self.nombre} asistió a todas sus clases programadas en la {self.escuela}."

    def inscribirse(self):
        return f"El proceso de inscripción fue exitoso. Matrícula activa: {self.matricula}."


# Creando el objeto pasando únicamente los valores en el orden correcto
mi_alumno = Alumno("Sofía Pérez", 20, "ALU-2026-89", "Ingeniería en Sistemas", 4, 9.4, "sofia.perez@universidad.edu", "5551234567", "Av. Universidad #123", "Instituto Tecnológico")

# Probando los métodos
print(mi_alumno.inscribirse())
print(mi_alumno.asistirAClases())
print(mi_alumno.estudiar())
print(mi_alumno.presentarExamen())
print(mi_alumno.entregarTareas())
