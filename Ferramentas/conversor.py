from pytube import YouTube
from pytube.cli import on_progress
import moviepy.editor as mp
import re
import os


def mp4():
    path = "C:/Users/USER/Desktop/Videos"
    link = input("Digite o Link: ")
    yt = YouTube(link, on_progress_callback=on_progress)

    print(f'Titulo {yt.title}')
    print('Baixando...')

    ys = yt.streams.get_highest_resolution()
    ys.download(path)


def mp3():
    link = input("Digite o Link: ")
    path = "C:/Users/USER/Desktop/Musicas"
    yt = YouTube(link, on_progress_callback=on_progress)

    print(f'Titulo {yt.title}')
    print("Baixando")
    ys = yt.streams.filter(only_audio=True).first().download(path)
    print("Download Completo")

    print("Covertendo para MP3")
    for file in os.listdir(path):
        if re.search('mp4', file):
            mp4_path = os.path.join(path, file)
            mp3_path = os.path.join(path, os.path.splitext(file)[0] + '.mp3')
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)
        print('Sucesso')


while True:
    print('Deseja Baixar para\n1-MP4\n2-MP3')

    try:
        op = int(input('=> '))
        if op == 1:
            mp4()
            print('')
        elif op == 2:
            mp3()
            print('')
    except ValueError:
        print('\n*** Valor Invalid, Digite 1 ou 2 ***\n')
        continue
