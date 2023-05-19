import tkinter as tk
import random
from tkinter import messagebox
NUM_FILAS= 8
NUM_COLUMNAS= 8
INTENTOS_MAXIMOS= 32

class BuscarBarco:
    def __init__(self, root):
        self.root = root
        self.root.title("Buscar al Barco")
        self.intentos_restantes = INTENTOS_MAXIMOS
        
        self.tablero = [[0 for _ in range(NUM_COLUMNAS)] for _ in range(NUM_FILAS)]
        self.posicion_barco = None
        
        self.generar_posicion_barco()
        
        self.celdas_botones = []
        for fila in range(NUM_FILAS):
            fila_botones = []
            for columna in range(NUM_COLUMNAS):
                boton = tk.Button(root, width=3, command=lambda fila=fila, columna=columna: self.descubrir_celda(fila, columna))
                boton.grid(row=fila, column=columna, padx=2, pady=2)
                fila_botones.append(boton)
            self.celdas_botones.append(fila_botones)
        
        self.intentos_restantes_label = tk.Label(root, text=f"Intentos restantes: {self.intentos_restantes}", font=("Arial", 12))
        self.intentos_restantes_label.grid(row=NUM_FILAS, column=0, columnspan=NUM_COLUMNAS, pady=10)
        
    def generar_posicion_barco(self):
        self.posicion_barco = (random.randint(0, NUM_FILAS - 1), random.randint(0, NUM_COLUMNAS - 1))
    

    def descubrir_celda(self, fila, columna):
        if self.intentos_restantes <= 0:
            messagebox.showinfo("Buscar al Barco", "¡Se acabaron los intentos! ¡Perdiste!")
            self.reiniciar_juego()
            return
        
        if (fila, columna) == self.posicion_barco:
            self.celdas_botones[fila][columna].config(text="B", bg="blue", state=tk.DISABLED)
            messagebox.showinfo("Buscar al Barco", "¡Encontraste al barco! ¡Ganaste!")   
            self.reiniciar_juego()
        else:
            self.celdas_botones[fila][columna].config(text="X", bg="red", state=tk.DISABLED)
            self.intentos_restantes -= 1
            self.intentos_restantes_label.config(text=f"Intentos restantes: {self.intentos_restantes}")
    
    def reiniciar_juego(self):
        self.intentos_restantes = INTENTOS_MAXIMOS
        self.intentos_restantes_label.config(text=f"Intentos restantes: {self.intentos_restantes}")
        
        for fila in range(NUM_FILAS):
            for columna in range(NUM_COLUMNAS):
                self.celdas_botones[fila][columna].config(text="", bg="SystemButtonFace", state=tk.NORMAL)
        
        self.generar_posicion_barco()
        
    def generar_nueva_cita():
        if (fila, columna) == self.posicion_barco:
           cita = random.choice(citas)
           cita_actual.set(cita)
           color = random.choice(colores)
           cita_label.config(fg=color)
        else:
            print("ERROR FOR EJECUTER")
 

citas = [
    "El éxito es la suma de pequeños esfuerzos repetidos día tras día.",
    "Cree en ti mismo y estarás a medio camino.",
    "La única forma de hacer un gran trabajo es amar lo que haces.",
    "No importa lo lento que vayas, siempre y cuando no te detengas.",
    "Cada día es una nueva oportunidad para cambiar tu vida.",
    "Tus únicas limitaciones son las que te pones a ti mismo.",
    "El único fracaso real es aquel del que no aprendes nada.",
    "Tú eres más fuerte de lo que crees. ¡Lo lograrás!",
    "No te rindas, el principio siempre es lo más difícil.",
    "Tu cuerpo puede soportar casi cualquier cosa. ¡Es tu mente la que debes convencer!",
    "El éxito no es la clave de la felicidad. La felicidad es la clave del éxito. Si amas lo que haces, serás exitoso.",
    "La perseverancia es la clave para alcanzar tus sueños más grandes.",
    "Los pequeños cambios suman grandes resultados. No subestimes el poder de los pequeños pasos.",
    "Cuando sientas que quieres rendirte, recuerda por qué comenzaste.",
    "No esperes a tenerlo todo bajo control para empezar. Comienza y ve ajustando el rumbo en el camino.",
    "La única manera de hacer un gran trabajo es amar lo que haces.",
    "Cada día es una oportunidad para ser un poquito mejor que ayer.",
    "Tu actitud determina tu altitud. Mantén una actitud positiva y alcanzarás grandes alturas.",
    "La confianza en uno mismo es el primer paso hacia el éxito.",
    "No te compares con los demás. Tu único objetivo debe ser superarte a ti mismo.",
    "El camino hacia el éxito está lleno de obstáculos. Aprende a saltarlos y seguir adelante.",
    "El verdadero éxito es disfrutar del camino y no solo llegar a la meta.",
    "Las limitaciones son solo creencias que podemos superar con determinación y esfuerzo.",
    "El éxito no está en vencer a otros, sino en superarte a ti mismo.",
    "No permitas que tus miedos te impidan alcanzar tus metas y sueños.",
    "Cada día es una oportunidad para aprender algo nuevo y crecer como persona.",
    "El éxito no es el final, el fracaso no es fatal: lo que cuenta es el coraje para continuar.",
    "No importa cuántas veces caigas, lo importante es cuántas veces te levantas.",
    "El único fracaso verdadero es no intentarlo en absoluto.",
    "La determinación y la perseverancia son la clave para alcanzar cualquier objetivo.",
    "La felicidad no es la ausencia de problemas, sino la habilidad para manejarlos.",
    "No permitas que los obstáculos te desvíen de tus sueños. Supéralos y continúa tu camino hacia el éxito.",
    "El camino hacia el éxito puede ser duro, pero cada paso te acerca más a tu destino.",
    "No te rindas, las mejores cosas de la vida suelen suceder justo cuando estás a punto de rendirte.",
]
ventana = tk.Tk()
ventana.geometry("720x450")  
juego = BuscarBarco(ventana)
reiniciar_btn = tk.Button(ventana, text="Reiniciar", command=juego.reiniciar_juego)
reiniciar_btn.grid(row=NUM_FILAS+1, column=0, columnspan=NUM_COLUMNAS, pady=10)
colores = ["red", "blue", "green", "purple", "orange" , "green" , "yellow", "skyblue"]
cita_label.pack(pady=20)
cita_actual = tk.StringVar()
cita_label = tk.Label(ventana, textvariable=cita_actual, font=("Arial", 14), wraplength=350)
cita_label.pack(pady=20)
contador_label = tk.Label(ventana, textvariable=contador, font=("Arial", 18, "bold"))
contador_label.pack()
ventana.mainloop()



