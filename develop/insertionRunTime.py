import requests
import json

media_requisicao = 0
j = 0 #quantidade total de reuisições realizadas
k = 0; #quantidade de erros
n = 4000 #quantidade de inserções -> 4000 -> medio (puro) de 0.0177 segundos
s = 0 #Quantidaded de respostas 201

for i in range(n): 
    ex = [
        {
            "tarefa": "Tomar banho",
            "categoria": 6,
            "concluido": False,
        }
    ]

    url = 'http://127.0.0.1:8000/api/list/'
    headers = {
        'Content-Type': 'application/json'
    }
    
    data = ex[0]
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        elapsed_time = response.elapsed.total_seconds()
        media_requisicao += elapsed_time
        j += 1

    except Exception as e:
        print(f'Erro na inserção: {e}')
        break

    if response.status_code == 201:  # Created
        s += 1
    else:
        k += 1

if j >= 1:
    media_geral = media_requisicao / j
    print(f'Numeros de sucessos: {s}')
    print(f'Numeros de falhas: {k}')
    print(f"Tempo médio de requisição (POST) numero de {n} inserções: {media_geral:.4f} segundos")  # Até 0.5000 é aceitável
else:
    print('Media inválida, Quant. de requisições: ',k)
    print("Têm certeza que a url está (no ar) correta?")