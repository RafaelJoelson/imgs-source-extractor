import os
import requests

#gerenciador de download de imagens de sites.
# URL base das imagens (sem o número)
#target
base_url = 'https://online.anyflip.com/jkrru/vusu/files/mobile/'

# Diretório onde as imagens serão salvas
download_dir = 'downloaded_images'

# Cria o diretório se não existir
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Intervalo de números das imagens
start_num = 106
end_num = 258

for i in range(start_num, end_num + 1):
    # Gera o URL completo para cada imagem
    img_url = f'{base_url}{i}.jpg'
    
    # Nome do arquivo
    file_name = os.path.join(download_dir, f'{i}.jpg')
    
    # Faz o download da imagem
    response = requests.get(img_url)
    if response.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(response.content)
        print(f'{file_name} salvo com sucesso!')
    else:
        print(f'Falha ao baixar {img_url}')
