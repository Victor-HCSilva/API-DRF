import requests

media_requisicao = 0
j = 0
n = 4001 #numeros de requisições -> 4001 -> tempo (puro) 0.0175 segundos
all_response = []

try:
    for i in range(n): 
        if (i >= 1):
            try:
                response = requests.delete(f'http://127.0.0.1:8000/api/list/{i}/')  
                elapsed_time = response.elapsed.total_seconds()
                media_requisicao += elapsed_time
                all_response.append(response.json())
                j += 1
            except:
                j += 1

    media_geral = media_requisicao / j
    
    if(int(input('Ver respostas (sim 1, não 0) ?')) == 1 ):
       for i in all_response:
           print(i)
           print(f"\nTempo médio de requisições (GET): {media_geral:.4f} segundos")
    else:
        print(f"(DELETE) Tempo médio de requisições: {media_geral:.4f} segundos")

except Exception as e:
    print(f'\nOcorreu um erro. Detalhes: \n\n {e}')

