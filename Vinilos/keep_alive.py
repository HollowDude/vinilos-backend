# keep_alive.py
import requests
import time

def keep_alive():
    url = 'https://vinilos-backend-2cwk.onrender.com/keep_alive/'  # URL de tu vista
    while True:
        try:
            response = requests.get(url)
            print(f'Manteniendo activo: {response.status_code}')
        except Exception as e:
            print(f'Error al mantener activo: {e}')
        time.sleep(800)  # Espera 15 minutos

if __name__ == '__main__':
    keep_alive()
