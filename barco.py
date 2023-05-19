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
            self.celdas_botones[fila][columna].config(text="B", bg="red", state=tk.DISABLED)
            messagebox.showinfo("Buscar al Barco", "¡Encontraste al barco! ¡Ganaste!")
            self.reiniciar_juego()
        else:
            self.celdas_botones[fila][columna].config(text="X", bg="gray", state=tk.DISABLED)
            self.intentos_restantes -= 1
            self.intentos_restantes_label.config(text=f"Intentos restantes: {self.intentos_restantes}")
    
    def reiniciar_juego(self):
        self.intentos_restantes = INTENTOS_MAXIMOS
        self.intentos_restantes_label.config(text=f"Intentos restantes: {self.intentos_restantes}")
        
        for fila in range(NUM_FILAS):
            for columna in range(NUM_COLUMNAS):
                self.celdas_botones[fila][columna].config(text="", bg="SystemButtonFace", state=tk.NORMAL)
        
        self.generar_posicion_barco()

ventana = tk.Tk()
juego = BuscarBarco(ventana)
reiniciar_btn = tk.Button(ventana, text="Reiniciar", command=juego.reiniciar_juego)
reiniciar_btn.grid(row=NUM_FILAS+1, column=0, columnspan=NUM_COLUMNAS, pady=10)
ventana.mainloop()
