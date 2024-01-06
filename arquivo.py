from plyer import notification
from datetime import datetime
import requests

def alerta(nivel, base, etapa):
    
    if nivel == 1:
        titulo = "Alerta Baixo"
    elif nivel == 2:
        titulo = "Alerta Médio"
    elif nivel == 3:
        titulo = "Alerta Alto"
    
    mensagem = f"Falha no carregamento da base {base} na etapa {etapa}\nData: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    notification.notify(
        title = titulo,
        message = mensagem,
    )

url_bancos = "https://brasilapi.com.br/api/banks/v1"
try:
    response = requests.get(url_bancos)
    response.raise_for_status() 
    bancos_data = response.json()

    
    print("Dados dos Bancos:")
    for banco in bancos_data:
        print(f"Nome: {banco['fullName']}, Código: {banco['code']}, ISPB: {banco['ispb']}")

except Exception as e:
    alerta(3, "bancos", "extração")
    print(f"Erro na extração dos bancos: {e}")

   