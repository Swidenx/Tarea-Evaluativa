import tkinter as tk
import random

def iniciar_juego():
    contador.set(0)
    generar_nueva_cita()

def generar_nueva_cita():
    cita = random.choice(citas)
    cita_actual.set(cita)
    color = random.choice(colores)
    cita_label.config(fg=color)

def incrementar_contador():
    contador.set(contador.get() + 1)
    generar_nueva_cita()


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

colores = ["red", "blue", "green", "purple", "orange"]
ventana = tk.Tk()
ventana.title("Juego Motivacional")
ventana.geometry("900x720")  
contador = tk.IntVar()
contador.set(0)

cita_actual = tk.StringVar()
cita_label = tk.Label(ventana, textvariable=cita_actual, font=("Arial", 14), wraplength=300)
cita_label.pack(pady=20)
contador_label = tk.Label(ventana, textvariable=contador, font=("Arial", 18, "bold"))
contador_label.pack()
incrementar_btn = tk.Button(ventana, text="Siguiente", command=incrementar_contador, font=("Arial", 12))
incrementar_btn.pack(pady=10)
reiniciar_btn = tk.Button(ventana, text="Reiniciar", command=iniciar_juego, font=("Arial", 12))
reiniciar_btn.pack(pady=10)
iniciar_juego()
ventana.mainloop()
