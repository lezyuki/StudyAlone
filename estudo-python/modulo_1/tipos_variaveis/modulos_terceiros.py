# pip install requests

print("\nImportação e uso de um módulo de terceiros")
import requests

url = "https://www.example.com"
response = requests.get(url)
print(f"Solicitacão HTTP para {url} retornou o status {response.status_code} ")