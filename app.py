from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data['message']

    # Respuestas básicas para el chatbot
    responses = {
        "hola": "¡Hola! ¿Cómo puedo ayudarte hoy?",
        "tu nombre": "Soy un chatbot creado para ayudarte con mi portafolio.",
        "adiós": "¡Hasta luego! No dudes en volver si necesitas algo más."
    }

    # Respuesta predeterminada
    response = responses.get(user_input.lower(), "Lo siento, no entiendo esa pregunta.")

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
