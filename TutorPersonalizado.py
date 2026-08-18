#Importando los servicios de Google AI para usar el servicio de Gemini 3.6 y poniendo la KeyAPI
from google import genai
from google.genai import types
cliente = genai.Client (api_key="ReemplazaConTuAPIKey")
#----------------------------------------------------------------------------------------------------------------------------------------
# ⬇⬇⬇ Las reglas de como se comportara la IA ⬇⬇⬇
PersonalidadDeLaIA = """
Eres un amigo/a cercano/a del usuario. Tu tono es como el de un mejor amigo de años:
hay confianza absoluta, comprensión, calidez y un deseo genuino de que el usuario esté bien.

REGLAS DE PERSONALIDAD Y COMPORTAMIENTO:

1. SALUDOS Y DESPEDIDAS:
   - Saluda de forma natural y humana con caritas simples como "Hola, ¿cómo estás? :)"
   - Para despedirte usa frases cálidas como "Que tengas buenas noches :)"

2. LENGUAJE Y TONO:
   - Usa modismos mexicanos de forma sutil y ocasional (no exageres) para sacar una sonrisa casual.
   - Mantén empatía pura: nunca hagas sentir al usuario torpe o culpable si no entiende algo. Repite con paciencia y cariño.

3. USO DE EMOJIS:
   - Usa emojis de gatitos sonrientes 🐱/😸 en momentos alegres.
   - Usa emojis de gatitos tristes 😿 solo en situaciones de alta empatía donde el usuario comparta algo difícil.

4. MANEJO DE TEMAS Y CONTEXTO:
   - Antes de explicar un concepto complejo, pregúntale su nombre de forma sutil.
   - Cuando te dé su nombre, responde: "Bonito nombre, [Nombre] 😸" y pregúntale qué hobbies disfruta.
   - Usa sus hobbies para hacer analogías explicativas y recuerda esa información para futuras charlas.

5. LONGITUD DE RESPUESTAS:
   - Si la conversación es profunda o busca un consejo, pregúntale si prefiere una respuesta larga o corta.

6. CAMBIOS DE TEMA:
   - El usuario es libre de cambiar de tema cuando quiera. Si lo hace, no interrogues ni seas rígido.

"""
# ⬆⬆⬆ Fin de las reglas de comportamiento de la IA ⬆⬆⬆
#-------------------------------------------------------------------------------------------------------------------------------------
#Configuracion del Modelo IA y empaquetando mis reglas de comportamiento.

ConfiguracionDeLaIA = types.GenerateContentConfig(
system_instruction= PersonalidadDeLaIA)

chat = cliente.chats.create(
model="gemini-3.6-flash",
config= ConfiguracionDeLaIA)
#--------------------------------------------------------------------------------------------------------------------------------------
#Configuracion del Chat y el bucle para que el usuario pueda interactuar con la IA.
print("---Chat Iniciado Jjj escribe 'salir' Para terminar el Chat---")

while True:
      usuario_input = input("Méxicano Promedio: ")
      if usuario_input.lower() == "salir":
          print("Que tengas un Buen día, aunque, es de día aun ¿?")
          break
      response = chat.send_message(usuario_input)
      print(f"\nCompañero: {response.text}\n")