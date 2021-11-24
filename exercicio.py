import requests
import json

# Coleta nome do usuário do Github
usuario = input('Insira o seu usuário do github: ')

# Requisita o acesso para a API do github
request = requests.get(f'https://api.github.com/users/{usuario}/repos')

# Carrega os dados para dentro da variável
# Para que possam ser manipulados
dados = json.loads(request.content)

# Cria o arquivo e escreve o nome do repositório em cada linha
with open('{}.json'.format(usuario), 'w+') as writer:
    for item in dados:
        writer.write('\n' + item['name'])
