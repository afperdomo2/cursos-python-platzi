def message_creator(text):
    messages = {
        "computadora": "Con mi computadora puedo programar usando Python",
        "celular": "En mi celular puedo aprender usando la app ed Platzi",
        "cable": "¡Hay un cable en mi bota!",
    }
    if text in messages:
        return messages[text]
    else:
        return "Artículo no encontrado"


text = "computadora"

response = message_creator(text)
print(response)
