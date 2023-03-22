import requests as r
from datetime import datetime


def intervalo(valor):
    if valor < 0 or valor > 250:
        print('Digite um valor dentro dos limites informados')
        return False
    else:
        return True


while True:
    print('+--------------------------------------+')
    print('|   *** TABELA DE RGB DAS CORES ***    |')
    print('+---------+----------------------------+')
    print('|    R    |    Valor aceito: 0 a 250   |')
    print('|    G    |    Valor aceito: 0 a 250   |')
    print('|    B    |    Valor aceito: 0 a 250   |')
    print('+---------+----------------------------+\n')
    try:
        red = int(input('Digite o valor de vermelho: '))
        if not intervalo(red):
            break
        green = int(input('Digite o valor de verde: '))
        if not intervalo(green):
            break
        blue = int(input('Digite o valor de azul: '))
        if not intervalo(blue):
            break
    except ValueError:
        print('O valor informado não é aceito, digite um número inteiro')
        break

    print('\n+--------------------------------------+')
    print('|   *** TABELA DE TILES E BORDA ***    |')
    print('+--------------------------+-----------+')
    print('|       N° DE Tiles        |  1 a 50   |')
    print('| Tamanho dos Tiles em px  |  1 a 20   |')
    print('|  Largura da Borda e px   |  0 a 15   |')
    print('+--------------------------+-----------+\n')

    try:
        tiles = int(input('Digite a quantidade de Tiles: '))
        if tiles < 1 or tiles > 50:
            print('Digite um valor dentro dos limites informados')
            break

        tile_size = int(input('Digite o tamanho dos Tiles: '))
        if tile_size < 1 or tile_size > 20:
            print('Digite um valor dentro dos limites informados')
            break
        border_width = int(input('Digite a largura da borda: '))
        if border_width < 0 or border_width > 15:
            print('Digite um valor dentro dos limites informados')
            break
    except ValueError:
        print('O valor informado não é aceito, digite um número inteiro')
        break

    print('\n+--------------------------------------+')
    print('|  *** TABELA DE MODOS DE GERAÇÃO ***  |')
    print('+--------------+-----------------------+')
    print('| 1-Brightness | Mais tons da sua cor  |')
    print('| 2-Around     |      Mais colorido    |')
    print('+--------------+-----------------------+\n')

    try:
        mode = int(input('Digite o n° da opção do modo desejado: '))
        if mode == 1:
            mode = 'Brightness'
        elif mode == 2:
            mode = 'Around'
        else:
            print('Digite uma opção válida')
            continue
    except ValueError:
        print('O valor informado não é aceito, digite um número inteiro')
        break

    url = r.api.get(f'https://php-noise.com/noise.php?r=${red}&g=${green}&b=${blue}&tiles=${tiles}&tileSize=${tile_size}&borderWidth=${border_width}&mode=${mode}&json')
    if url.status_code != 200:
        print('Ocorreu um erro na geração da imagem, código de erro:', url.status_code)
        break
    url = url.json()
    img = url['uri']

    data = datetime.now()
    data = data.strftime("%H-%M-%S-%f")
    with open(f'background_{data}_.png', 'wb') as imagem:
        response = r.get(str(img), stream=True)

        if not response.ok:
            print('Ocorreu um erro')
        else:
            for dado in response.iter_content(5120):
                if not dado:
                    break
                imagem.write(dado)
            print('Imagem baixada :)')
            break