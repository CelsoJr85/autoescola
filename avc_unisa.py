from time import sleep

contagem_positivo = 0

# Perguntas
def pergunta_cinco():
    pergunta05 = input('Se o farol está vermelho, você deve parar o carro?(sim ou não) ')
    if pergunta05 == 'sim':
        global contagem_positivo
        contagem_positivo += 1
        if contagem_positivo >= 3:
            print('Parabéns! Você conhece as leis de trânsito!')
            sleep(2)
            print('-' * 75)
            print(f'Acertos: {contagem_positivo}, Erros: {contagem_positivo-5}')
            print('-' * 75)
            exit()
    else:
        print('Errou, pesquise o assunto!')
        sleep(2)
        print('-' * 75)
        print(f'Acertos: {contagem_positivo}, Erros: {5 - contagem_positivo}')
        print('-' * 75)
        exit()

def pergunta_quatro():
    pergunta04 = input('Se o farol está verde e há pedestre atravessando, você pode avançar?(sim ou não) ')
    if pergunta04 == 'não':
        global contagem_positivo
        contagem_positivo += 1
        print('Acertou! Vamos para a próxima pergunta')
        sleep(1)
        pergunta_cinco()
    else:
        print('Errou, pesquise o assunto!')
        sleep(1)
        pergunta_cinco()

def pergunta_tres():
    pergunta03 = input('Se o farol está verde e não há nenhum pedestre atravessando, você pode avançar?(sim ou não) ')
    if pergunta03 == 'sim':
        global contagem_positivo
        contagem_positivo += 1
        print('Acertou! Vamos para a próxima pergunta')
        sleep(1)
        pergunta_quatro()

    else:
        print('Errou, pesquise o assunto!')
        sleep(1)
        pergunta_quatro()

def pergunta_dois():
    pergunta02 = input('Se o farol está amarelo, você deve acelerar o carro para passar?(sim ou não) ')
    if pergunta02 == 'não':
        print('Acertou! Vamos para a próxima pergunta')
        global contagem_positivo
        contagem_positivo += 1
        pergunta_tres()
    else:
        print('Errou, pesquise o assunto!')
        sleep(1)
        pergunta_tres()

def pergunta_um():
    pergunta01 = input('Se o farol está vermelho, você pode avançar com o carro?(sim ou não) ')
    if pergunta01 == 'não':
        print('Acertou! Vamos para a próxima pergunta')
        global contagem_positivo
        contagem_positivo += 1
        sleep(1)
        pergunta_dois()
    else:
        print('Errou, pesquise o assunto!')
        sleep(1)
        pergunta_dois()


if __name__ == "__main__":
    # Titulo
    print('=' * 75)
    print("Bem vindo a Auto Escola.")
    print('-' * 75)
    sleep(2)
    pergunta_um()