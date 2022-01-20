def mostraLinha():
    print('-----------------------------------------------------------------')

def juntoSemAcento():
    print('\nO porque junto e sem acento é usado para respostas/explicação.\n\n Exemplo:\n')
    print('Bruno fez isso porque já estava cansado de tanta humilhação!\n')

def separadoSemAcento():
    print('\nO por que separado e sem acento é usado para perguntas.\n\n Exemplo:\n')
    print('Por que o Sol brilha?\n')

def juntoComAcento():
    print('\nO porquê junto e com acento é usado em caso de razão e substituir um substantivo.\n\n Exemplo:\n')    
    print('O governador precisa explicar o porquê de suas ações.\n')

def separadoComAcento():
    print('\nO por quê separado e com acento é usado no final de frases.\n\n Exemplo:\n')
    print('\nEla sabe por quê.\n')

def extPrograma():
    print('Programa finalizado.')    

def quiz():
    mostraLinha()
    print('Este quiz consiste em você completar as frases usando os poequês.')
    mostraLinha()
    print('Amassa, campeão!\n')

    x=str(input('______ não voltamos para a casa?\n'))
    if x == 'Por que':
        print('Certa resposta!\n')
    else:
        print('Resposta errada :( .\n')  

    z=str(input('______ agora não temos tempo.\n'))
    if z == 'Porque':
        print('Certa resposta!\n')
    else:
        print('Resposta errada : ( .\n')    

    y=str(input('Você não gosta dessa matéria, ______?\n'))
    if y == 'Por quê':
        print('Certa resposta!\n')
    else:
        print('Resposta errada : ( .\n')   

    w=str(input('Gostaria de saber o ______ dele não falar mais comigo.\n'))
    if w == 'Porquê':
        print('Certa resposta!\n')
    else:
        print('Resposta errada : ( .\n') 

x=str(input('Digite seu nome:\n'))
print('\nOlá, {}. Vamos aprender o uso dos porquês!!\n'.format(x))
p = 0
while p < 6 or p > 1:
    p=int(input('Escolha um porquê e saiba como usar.\n 1_ Porque;\n 2_ Por que; \n 3_ Porquê;\n 4_ Por quê;\n 5_ Quiz.\n 6_ Sair\n\n'))

    if p > 6 or p < 1:
        mostraLinha()
        print('Opção não encontrada. Digite um número entre 1 e 5.')
        mostraLinha()
        print('\n')
    elif p == 1:
        juntoSemAcento()
    elif p == 2:
        separadoSemAcento()
    elif p == 3:
        juntoComAcento() 
    elif p == 4:
        separadoComAcento()
    elif p == 5:
        quiz()
    elif p == 6:
        extPrograma()
        break
   



                
                

