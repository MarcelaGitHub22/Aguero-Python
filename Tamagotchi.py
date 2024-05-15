class Tamagotchi:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel_energia = 100
        self.nivel_hambre = 0
        self.nivel_felicidad = 50
        self.humor = "indiferente"
        self.esta_vivo = True

    def estado(self):
        print(f"Nombre: {self.nombre}")
        print(f"Energía: {self.nivel_energia}")
        print(f"Hambre: {self.nivel_hambre}")
        print(f"Felicidad: {self.nivel_felicidad}")
        print(f"Humor: {self.humor}")

    def alimentar(self):
        self.nivel_hambre -= 10
        self.nivel_energia -= 15

    def jugar(self):
        self.nivel_felicidad += 20
        self.nivel_energia -= 18
        self.nivel_hambre += 10
    def dormir(self):
        self.nivel_energia += 40
        self.nivel_hambre += 5

    def verificar_estado(self):
        if self.nivel_energia <= 0 or self.nivel_hambre >= 20:
            self.esta_vivo = False
        else:
            self.esta_vivo = True

# Ejemplo de uso
nombre = input("Ingresa tu nombre: ")
persona = Tamagotchi(nombre)

while True:
    accion = input("¿Qué deseas hacer? (comer/jugar/dormir/salir): ")
    if accion == "comer":
        persona.alimentar()
    elif accion == "jugar":
        persona.jugar()
    elif accion == "dormir":
       persona.dormir()
    elif accion == "salir":
        break;
    if persona.estado():
        print(f"{persona.nombre} esta viva")
    else:
        print(f"{persona.nombre} Murió")