import requests

media_requisicao = 0
j = 0
n = 10 #numeros de requisições
all_response = []

try:
    for i in range(1000): 
        response = requests.get('http://127.0.0.1:8000/api/list/')  
        elapsed_time = response.elapsed.total_seconds()
        media_requisicao += elapsed_time
        all_response.append(response.json())
        j += 1

    media_geral = media_requisicao / j
    
    if(int(input('Ver respostas (sim 1, não 0) ?')) == 1 ):
       for i in all_response:
           print(i)
           print(f"\nTempo médio de requisições (GET): {media_geral:.4f} segundos")
    else:
        print(f"(GET) Tempo médio de requisições: {media_geral:.4f} segundos")

except Exception as e:
    print(f'\nOcorreu um erro. Detalhes: \n\n {e}')

