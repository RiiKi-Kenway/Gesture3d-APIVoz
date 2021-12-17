import speech_recognition as sr

# Importa as permissões para acessar arquivos do sistema operacional. "Pode ser desnecessário"
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
        rec.energy_threshold = 500
        # rec.energy_threshold = 50

        # Armazena o que foi dito na variável rec
        audio = rec.listen(mic)

    try:
        print("Analisando...")
        # Passa a variável para o algoritmo reconhecedor de padroes
        comando = rec.recognize_google(audio, language="PT-BR")
        print(f"Comando reconhecido: "+ comando + "\n")
        
    # Se não reconheceu o padrao de fala, exibe a mensagem
    except Exception as e:
    #   print(e)
        print("Não entendi, pode repetir?\n")
    #   return 'nada'
        return e
    return comando

# Estrtura de repetição
if __name__ == '__main__':
    while True:
        # Caso a palavra de invocação não exista na frase, recomeça o programa.
        comando = ouvir_microfone().lower()

        # Palavra de invocação
        if "cris" == "chris" == "crys" in comando:
            
            # # Teste para abrir programas.
            # if "navegador" in comando:
            #     os.system("start Firefox.exe")

            # elif "steam" in comando:
            #     os.system("start D:\steam\Steam.exe")

            # elif "word" in comando:
            #     os.system("start WINWORD.EXE")
            
            # Palavra de exorcismo
            if "parar" == "finalizar" == "finalze" in comando:
                print("Programa finalizado.")
                break
            else:
                # Após reconhecer a invocaçaõ, verifica se o arquivo de comandos existe e sobrescreve a ultima frase pela nova,
                # caso contráio, gera um novo arquivo.
                with open('comandos.txt', 'w') as saida:
                    print(comando, file=saida)
