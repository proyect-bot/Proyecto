import csv
import time
import os

# --- Función para imprimir estilo chat ---
def chat(texto):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(0.02)
    print()

# --- Archivo CSV ---
archivo_csv = "respuestas_chatbot.csv"
archivo_racha = "racha.txt"  # para guardar la racha de días consecutivos

# --- Preguntas ---
preguntas = [
    ("¿Cuál es tu nombre y apellido?", None),
    ("¿Qué edad tienes?", ["11-13", "14-16", "17+"]),
    ("¿Cuál es tu género?", ["Masculino", "Femenino", "Prefiero no decirlo"]),
    ("¿En qué grado estás?", ["6", "7", "8", "9", "10", "11"]),
    ("¿Cuántas comidas principales comes al día?", ["1", "2", "3", "4 o más"]),
    ("¿Con qué frecuencia desayunas?", ["Nunca", "A veces", "Casi siempre", "Todos los días"]),
    ("¿Con qué frecuencia consumes frutas?", ["Nunca", "1-2 veces/semana", "3-4 veces/semana", "Todos los días"]),
    ("¿Con qué frecuencia consumes verduras?", ["Nunca", "1-2 veces/semana", "3-4 veces/semana", "Todos los días"]),
    ("¿Con qué frecuencia consumes bebidas azucaradas?", ["Nunca", "1-2 veces/semana", "3-4 veces/semana", "Todos los días"]),
    ("¿Qué sueles comer en el refrigerio del colegio?", ["Comida rápida", "Frutas", "Galletas/dulces", "Otros"]),
    ("¿Cuánta agua tomas al día?", ["Menos de un vaso", "1-3 vasos", "1-6 vasos", "Más de 6 vasos"]),
    ("¿Con qué frecuencia comes comida rápida?", ["Nunca", "1 vez/semana", "Varias veces/semana", "1 vez al mes"]),
    ("¿Qué tan seguido consumes paquetes?", ["Nunca", "1 vez/semana", "Varias veces/semana", "Todos los días"]),
    ("¿Consideras que conoces lo suficiente sobre alimentación saludable?", ["Sí", "No", "Más o menos"]),
    ("¿De dónde aprendes más sobre alimentación?", ["Familia", "Colegio", "Redes sociales", "Internet", "Otros"]),
    ("¿Qué entiendes por 'alimentación saludable'?", None),
    ("¿Qué te motiva a comer saludable?", ["Salud", "Apariencia física", "Deportes", "Presión familiar", "Otros"]),
    ("¿Qué dificultades tienes para mantener una alimentación saludable?", ["Falta de dinero", "Falta de tiempo", "Prefiero otros alimentos", "No sé qué comer", "Otros"]),
    ("¿Te interesaría usar un chatbot que te diera consejos de alimentación saludable?", ["Sí", "No", "Tal vez"]),
]

# --- Crear archivo CSV si no existe ---
with open(archivo_csv, "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    if f.tell() == 0:
        writer.writerow([p[0] for p in preguntas])

# --- Introducción ---
chat("👋 ¡Hola! Soy NutriBot, tu asistente de alimentación saludable.")
chat("Te haré unas preguntas rápidas y al final te daré una recomendación de dieta 🥦🍎.")
chat("¡Además podrás llevar tu racha diaria de hábitos! 🔥\n")

# --- Recolectar respuestas ---
respuestas = []

for i, (texto, opciones) in enumerate(preguntas, start=1):
    chat(f"{i}. {texto}")
    if opciones:
        for j, opcion in enumerate(opciones, start=1):
            print(f"   {j}. {opcion}")
        while True:
            try:
                eleccion = int(input("👉 Elige un número: "))
                if 1 <= eleccion <= len(opciones):
                    respuestas.append(opciones[eleccion - 1])
                    break
                else:
                    chat("❌ Esa opción no existe, intenta de nuevo.")
            except ValueError:
                chat("❌ Escribe un número válido.")
    else:
        respuesta = input("✍️ Tu respuesta: ")
        respuestas.append(respuesta)

# --- Guardar en CSV ---
with open(archivo_csv, "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(respuestas)

# --- Generar recomendación de dieta ---
chat("\n🍽️ Según tus respuestas, aquí tienes una recomendación básica:")

desayuno = "Avena con frutas y un vaso de agua"
almuerzo = "Arroz, pollo a la plancha, ensalada de verduras y agua"
cena = "Sopa de verduras + arepa integral + jugo natural"
snack = "Una fruta (manzana, banano) en el recreo"

if "Nunca" in respuestas or "A veces" in respuestas:
    desayuno = "⚠️ Intenta no saltarte el desayuno. Un batido de frutas y avena es una buena opción."
if "Galletas/dulces" in respuestas or "Comida rápida" in respuestas:
    snack = "⚠️ Mejor cambia tu snack por frutas o frutos secos."
if "Menos de un vaso" in respuestas or "1-3 vasos" in respuestas:
    chat("💧 Recuerda aumentar tu consumo de agua, tu cuerpo lo agradecerá.")

chat(f"- Desayuno recomendado: {desayuno}")
chat(f"- Almuerzo recomendado: {almuerzo}")
chat(f"- Cena recomendada: {cena}")
chat(f"- Snack saludable: {snack}")

# --- Sistema de racha ---
racha = 1
if os.path.exists(archivo_racha):
    with open(archivo_racha, "r") as f:
        try:
            racha = int(f.read().strip()) + 1
        except:
            racha = 1

with open(archivo_racha, "w") as f:
    f.write(str(racha))

chat(f"\n🔥 ¡Felicidades! Hoy completaste tu encuesta saludable. Llevas {racha} días de racha 🎉")
chat("Sigue así y verás cambios positivos en tu alimentación 💪.")
