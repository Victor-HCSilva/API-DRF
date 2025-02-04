import requests
import psutil
import os
import time

def requisicao_com_monitoramento(url):
    n = 4001
    process = psutil.Process(os.getpid())

    # Memória usada antes da requisição
    memoria_antes = process.memory_info().rss  # RSS: Resident Set Size (memória física usada pelo processo)

    inicio = time.time()
    for i in range(n):
        try:
            
            response = requests.get(url)
            response.raise_for_status()  # Lança exceção para erros HTTP (status code >= 400)
            # Processar response.content (importante para grandes respostas)
            #  O código abaixo mostra o conteúdo mas, dependendo do tamanho,
            #  pode consumir muita memória. Use com moderação.
            # conteudo = response.content 
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            return

    fim = time.time()

    # Memória usada depois da requisição
    memoria_depois = process.memory_info().rss

    # Diferença no uso de memória
    uso_memoria = memoria_depois - memoria_antes

    print(f"Tempo de requisição: {fim - inicio:.4f} segundos")
    print(f"Uso de memória: {uso_memoria / (1024 * 1024):.2f} MB")  # Converter para MB
    # Opcional: Print do status code
    print(f"Status code: {response.status_code}")

# Exemplo de uso

if __name__=='__main__':
    url = "http://127.0.0.1:8000/api/list/" # Substitua pela URL que você quer testar
    requisicao_com_monitoramento(url)