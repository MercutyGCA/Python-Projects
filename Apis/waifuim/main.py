import requests as r
from datetime import datetime


# area das variaveis de escopo globais
nsfw = ''
comum_tags = ['maid', 'waifu', 'marin-kitagawa', 'mori-calliope', 'raiden-shogun', 'oppai', 'selfies', 'uniform']
nsfw_tags = ['ass', 'hentai', 'milf', 'oral', 'paizuri', 'ecchi', 'ero']

#Area de Funções 
def listagem(nsfw):
    if not nsfw:
        for key, tag in enumerate(comum_tags):
            print(f'{key}: {tag}')
    elif nsfw:
        for i in nsfw_tags:
            comum_tags.append(i)
        for key, tag in enumerate(comum_tags):
            print(f'{key}: {tag}')


def pegarImagem(url):
    link = r.api.get(str(url))
    if link.status_code != 200:
        print('Ocorreu um erro')
        link.close()
    elif link.status_code == 200:
        link = link.json()
        img = link['images'][0]['url']
        img = str(img)
        return img


def pegarFormato(url):
    link = r.api.get(str(url))
    if link.status_code != 200:
        print('Ocorreu um erro')
        link.close()
    elif link.status_code == 200:
        link = link.json()
        formato = link['images'][0]['extension']
        formato = str(formato)
        return formato


def salvarImgem(img, formato):
    data = datetime.now()
    data = data.strftime("%d-%m-%y")
    with open(f'waifu_{data}_{formato}', 'wb') as imagem:
        response = r.get(str(img), stream=True)

        if not response.ok:
            print('Ocorreu um erro')
        else:
            for dado in response.iter_content(5120):
                if not dado:
                    break
                imagem.write(dado)
            print('Imagem baixada :)')
            
# inico da aplicação
print('Deseja Gerar uma imagem comum ou nsfw?')
print('1-Comum\n2-NSFW\n')
op = int(input('Digite o numero da opção: '))
try:
    if op == 1 and type(op) == int:
        nsfw = False
        print('Deseja gerar uma imagem usando quantas TAGS? (O máximo de tags permitidas são 3)')
        op = int(input('Digite o n° de tags a serem usadas: '))
        if op == 1 and type(op) == int:
            listagem(nsfw)
            tag1 = int(input('Digite o indice da tag a ser usada: '))
            url = f'https://api.waifu.im/search/?included_tags{comum_tags[tag1]}&is_nsfw={nsfw}'
            url = str(url)
            img_path = pegarImagem(url)
            form_path = pegarFormato(url)
            salvarImgem(img_path, form_path)
        elif op == 2 and type(op) == int:
            listagem(nsfw)
            tag1 = int(input('Digite o indice da primeira tag a ser usada: '))
            tag2 = int(input('Digite o indice da segunda tag a ser usada: '))
            url = f'https://api.waifu.im/search/?included_tags{comum_tags[tag1]}&included_tags{comum_tags[tag2]}&is_nsfw={nsfw}'
            url = str(url)
            img_path = pegarImagem(url)
            form_path = pegarFormato(url)
            salvarImgem(img_path, form_path)
        elif op == 3 and type(op) == int:
            listagem(nsfw)
            tag1 = int(input('Digite o indice da primeira tag a ser usada: '))
            tag2 = int(input('Digite o indice da segunda tag a ser usada: '))
            tag3 = int(input('Digite o indice da terceira tag a ser usada: '))
            url = f'https://api.waifu.im/search/?included_tags{comum_tags[tag1]}&included_tags{comum_tags[tag2]}&included_tags{comum_tags[tag3]}&is_nsfw={nsfw}'
            url = str(url)
            img_path = pegarImagem(url)
            form_path = pegarFormato(url)
            salvarImgem(img_path, form_path)
        else:
            print('Digite um valor de 1 a 3')
except ValueError:
    print('Valor Digitado Ivanlido')

try:
    if op == 2 and type(op) == int:
        nsfw = True
        print('Deseja gerar uma imagem usando quantas TAGS? (O máximo de tags permitidas são 3)')
        op = int(input('Digite o n° de tags a serem usadas: '))
        if op == 1 and type(op) == int:
            listagem(nsfw)
            tag1 = int(input('Digite o indice da tag a ser usada: '))
            url = f'https://api.waifu.im/search/?included_tags{comum_tags[tag1]}&is_nsfw={nsfw}'
            url = str(url)
            img_path = pegarImagem(url)
            form_path = pegarFormato(url)
            salvarImgem(img_path, form_path)
        elif op == 2 and type(op) == int:
            listagem(nsfw)
            tag1 = int(input('Digite o indice da primeira tag a ser usada: '))
            tag2 = int(input('Digite o indice da segunda tag a ser usada: '))
            url = f'https://api.waifu.im/search/?included_tags{comum_tags[tag1]}&included_tags{comum_tags[tag2]}&is_nsfw={nsfw}'
            url = str(url)
            img_path = pegarImagem(url)
            form_path = pegarFormato(url)
            salvarImgem(img_path, form_path)
        elif op == 3 and type(op) == int:
            listagem(nsfw)
            tag1 = int(input('Digite o indice da primeira tag a ser usada: '))
            tag2 = int(input('Digite o indice da segunda tag a ser usada: '))
            tag3 = int(input('Digite o indice da terceira tag a ser usada: '))
            url = f'https://api.waifu.im/search/?included_tags{comum_tags[tag1]}&included_tags{comum_tags[tag2]}&included_tags{comum_tags[tag3]}&is_nsfw={nsfw}'
            url = str(url)
            img_path = pegarImagem(url)
            form_path = pegarFormato(url)
            salvarImgem(img_path, form_path)
        else:
            print('O valor digitado é invalido')
    elif type(op) != int:
        print('O valor digitado é invalido')
except ValueError:
    print('O valor digitado é invalido')