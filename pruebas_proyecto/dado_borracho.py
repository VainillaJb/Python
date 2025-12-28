import random
import os
import time
import webbrowser

class Interfaz:
    def __init__(self):
        self.dibujo = "🎲"

    def limpiar(self):
        # Limpia la terminal (Lectura 5: módulo os)
        os.system('cls' if os.name == 'nt' else 'clear')

    def animar(self):
        print("\nLanzando dado...")
        for i in range(3):
            print("🍺", end=" ", flush=True)
            time.sleep(0.4)
        print("\n")

class Dado:
    def __init__ (self, caras=6):
        self.caras = caras
    
    def lanzar(self):
        return random.randint(1, self.caras)

class DadoBorracho:

    def __init__(self):
        self.url = "https://v16-webapp-prime.tiktok.com/video/tos/maliva/tos-maliva-ve-0068c799-us/ocv5WEAzPBgYPwEnxViZQvMViRtPBcjVEV9IA/?a=1988&bti=ODszNWYuMDE6&ch=0&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C&cv=1&br=1018&bt=509&cs=2&ds=3&ft=I~da4od0D12Nv6juP.IxR8jSglJG-UjNSaopiX&mime_type=video_mp4&qs=14&rc=Zjw7ZzM4NzlkOWhpaTpkaEBpM2kzcGo5cjZ1dTMzaTczNEAyYWE0YGJjXjMxMF80Xl5jYSMzNTFrMmQ0b15gLS1kMTJzcw%3D%3D&btag=e000b8000&expire=1767023516&l=20251227235141CA23DC827CC3379D0596&ply_type=2&policy=2&signature=38f45e62905ad8badc5480b9b1dd9795&tk=tt_chain_token" 
        self.puntos = 0
        self.meta = 10
        self.modo = ""
        self.interfaz = Interfaz()
        self.dado = Dado()

    def verificador(self, num):
        if num == 1:
            if self.modo == "1": #MODO FACIL :D
                print("Vaya! -- acabas de sacar 1. Te quitare un shot/punto")
                self.puntos -= 1 
            else: #Modo Dificil
                print("JAJAJA TE MAREASTE -- 1 asi que reiniciamos la borrachera!")
                self.puntos = 0
        
        elif num == 6: #REGALITO REGALON
            print("SALUD! -- Sacastes 6. Sumas 2 shot/puntos")
            self.puntos += 2
        else:
            print("Suma 1 shot/punto. Animo Animo!")
            self.puntos += 1
        
        #EVITAR QUE EL PUNTAJE SEA NEGATIVO
        if self.puntos < 0 : self.puntos = 0

class RondaBorracha:
    def __init__(self):
        # Conectamos con la otra clase para usar sus puntos y reglas
        self.juego = DadoBorracho()

    def empezar(self):
        self.juego.interfaz.limpiar()
        print("=== MENU PRINCIPAL ===")

        # NOMBRE
        nombre = input("""
        El azar nos ha sentado en la misma mesa, pero el destino 
        se olvidó de las presentaciones. 
        ¿Con qué nombre debería recordarte cuando el dado deje de girar?
        -> """)

        print(f"\nOye {nombre}, ¿qué tan borracho está el dado hoy?")
        print("1. MODO FACIL - Se te quita 1 punto")
        print("2. MODO DIFICIL - Se reinicia a 0")
        self.juego.modo = input("ELIGE QUE MODO FIESTERO JUGAR (1 o 2): ")

        # BUCLE
        while self.juego.puntos < self.juego.meta:
            self.juego.interfaz.limpiar()
            input(f"JUGADOR: {nombre} - PUNTOS: {self.juego.puntos}/{self.juego.meta} | ENTER para lanzar...")
            
            self.juego.interfaz.animar()
            self.juego.interfaz.limpiar()
            tiro = self.juego.dado.lanzar()
            
            print(f"Resultado: {tiro}")
            self.juego.verificador(tiro)
            print("*" * 30)
            input("Preisona Enter para tirar de nuevo")

            if self.juego.puntos >= self.juego.meta:
                print(f"\n¡FELICIDADES {nombre.upper()}! Ganaste con {self.juego.puntos} puntos. 🏆")
                time.sleep (3)
                url_directa = self.juego.url
                os.system(f'start chrome --app="{url_directa}" --autoplay-policy=no-user-gesture-required')
                break

if __name__ == "__main__":
    partida = RondaBorracha()
    partida.empezar()