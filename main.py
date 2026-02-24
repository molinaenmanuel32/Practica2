import requests

respuesta = requests.get("https://api.github.com")

print("Código de estado:", respuesta.status_code)
print("Todo funcionando correctamente ✅")