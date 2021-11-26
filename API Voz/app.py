import speech_recognition as sr

import os

# voice command system for virtual reality
# boas vindas
print("Olá, *USUARIO*!\nMe chamo CRYS, Em que posso ajudar?\n")

# Função para ouvir e reconhecer a fala
def ouvir_microfone():
    # Habilita o microfone do usuário
    rec = sr.Recognizer()

    # Usando o microfone
    with sr.Microphone() as mic:
        # Chama um algoritmo para reducao de ruidos no som
        rec.adjust_for_ambient_noise(mic)

        # Frase para o usuario dizer algo. "Pode ser desnecessário"
        print("Aguardando comando...")
        rec.pause_threshold = 1
        rec.energy_threshold = 50

        # Armazena o que foi dito em uma variavel
        audio = rec.listen(mic)

    try:
        print("Analisando...")
        # Passa a variável para o algoritmo reconhecedor de padroes
        comando = rec.recognize_google(audio, language="PT-BR")
        print(f"Comando reconhecido: "+ comando + "\n")
        
    # Se não reconheceu o padrao de fala, exibe a mensagem
    except Exception as e:
        print(e)
        print("Não entendi, pode repetir?\n")
        return 'nada'
    return comando

# Estrtura de repetição
if __name__ == '__main__':
    while True:
        comando = ouvir_microfone().lower()

        # print(f"Comando reconhecido 2: " + comando + "\n")

        if "cris" in comando:
            # print("entrou na invocação\n")

            # # Teste para abrir programas.
            # if "navegador" in comando:
            #     os.system("start Firefox.exe")

            # elif "steam" in comando:
            #     os.system("start D:\steam\Steam.exe")

            # elif "word" in comando:
            #     os.system("start WINWORD.EXE")

            if "parar" in comando:
                print("Programa finalizado.")
                break
        else:
            # print("gerando o arquivo\n")
            with open('saida.txt', 'w') as saida:
                print(comando, file=saida)