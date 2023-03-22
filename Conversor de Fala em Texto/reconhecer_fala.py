# README - Guilherme Coelho Araujo

# Bliblioteca de Busca no Google
from googlesearch import search

# Biblioteca de Reconhecimento e Tradução por voz
import speech_recognition as sr

# Variavel Global que guarda a função de gravação e reconhecimento
rec = sr.Recognizer()

# Define o microfone que ira captar a voz
with sr.Microphone(2) as mic:
    # Retira o ruido
    rec.adjust_for_ambient_noise(mic)

    # Aviso que já pode falar
    print('Pode falar que eu vou gravar...')

    # Guarda o Audio
    audio = rec.listen(mic)

    # Traduz pra português
    texto = rec.recognize_google(audio, language="pt-BR")

# Texto a ser pesquisado
query = texto

# Realiza uma busca com o texto
result = list(
    search(
        query,
        lang='pt-br',
        num_results=5
    )
)

# Mostra a fala do reconhecimento de voz
print(f'Pesquisa: {texto}\n')

print("resultados da busca:\n")
# Faz um foreach pela lista resultados
for links in result:
    # Mostar o resultado da pesquisa por voz
    print(links)
