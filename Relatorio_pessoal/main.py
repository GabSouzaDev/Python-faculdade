#Escreva um programa que cria um relatório de usuário.
#Seu programa deve receber dados do usuário e armazenar em um novo arquivo com o nome do usuário.
#Esse arquivo deve ser salvo em uma pasta com a data do dia.
#Dados: nome, idade, profissão, frase do dia.

import datetime
from pathlib import Path
from random import randint
import time
import sys
import re

##Variaveis Globais
cont = True

date = datetime.date.today()

print(date.strftime("%d-%m-%Y"))

frases = ['Seja como um raio de sol intenso: espalhe luz, calor e faça as pessoas se perguntarem qual é a necessidade de você estar tão forte logo de manhã',
     'Faça sempre o seu melhor, mesmo que o seu melhor para hoje seja apenas tirar uma soneca.',
     'Que todos os nossos passos nos levem para onde a felicidade nos espera. Mesmo que seja até a sorveteria.',
     'Que a felicidade que você procura seja tão plena quanto um cachorrinho em uma piscina de bolinhas.',
     'O sucesso é como um pote de ketchup, às vezes você tem que bater um pouquinho para sair.',
     'A vida é como uma caixa de chocolates: você nunca sabe realmente se o que te espera é uma coisa boa ou muito amarga.',
     'Quando você tiver finalizado uma meta, não olhe para ela como a linha de chegada. Dobre a meta, triplique a meta, quadruplique a meta e depois ria da cara da meta.',
     'O segredo para o sucesso é a persistência, a determinação e uma grande quantidade de paciência e cafeína no sistema sanguíneo.',
     'Seja a pessoa que seu cachorro acredita que você é!',
     'O trabalho em equipe é essencial. Imagine o quanto Bob Esponja seria menos divertido se o Patrick não estivesse lá para atrapalhar.',
     'Se você acha que está tendo um dia ruim, lembre-se que alguém em algum lugar está preso em uma reunião chata que poderia ser resolvida através de um email curto.',
     'A vida é cheia de altos e baixos, especialmente quando você está preso em um elevador quebrado.',
     'Seja tão confiante a ponto de ter a certeza que o seu espelho está agradecido de te ver todas manhãs.',
     'Lembre-se de que cada dia é uma nova oportunidade para fazer coisas erradas novamente. Afinal, a vida seria muito chata se tudo fosse perfeito.',
     'Seja como um pinguim: mantenha a compostura, deslize elegantemente pela vida e evite dar de cara com paredes de vidro.',
     'Nunca deixe que alguém te diga que você não pode fazer algo. Mostre a eles como você pode transformar os seus erros em sarcasmo e utilizar o humor como mecanismo de defesa.',
     'Não importa quantas vezes você caia, desde que você se levante com estilo e ainda finalize a subida com uma pose incrível.',
     'Acredite nos seus sonhos, mesmo que eles envolvam unicórnios, elfos e fadas.',
     'Veja sempre o que há de positivo no mundo! Comece admirando uma pilha por um longo período de tempo.',
     'O fracasso não é o fim. Ele é apenas o alívio cômico antes do sucesso.',
     'Você não precisa de muito para construir um mundo melhor. Basta um computador e o The Sims instalado.',
     'Os sonhos são a melhor forma de termos uma direção na vida e um motivo para caminhar… ou voar. Não sei qual o tipo de sonho que você tem.',
     'Não tenha medo de ser diferente. Afinal, todo mundo acha interessante as pessoas que gostam de abacaxi na pizza.',
     'A vida é curta demais para se preocupar com o que os outros pensam. A menos que sejam os juízes de um show de talentos. Aí, talvez você deva se importar um pouquinho.',
     'Seja como uma estrela cadente: brilhe intensamente, deixe um rastro de esperança e faça todos desejarem que você volte mais vezes.',
     'Seja como uma abelha: trabalhe duro, espalhe a doçura e, se alguém te irritar, lembre-se de que você tem um ferrão preparado.',
     'Faça tudo com foco e atenção. Não existe “ctrl z” para a vida.',
     'Faça boas escolhas dos seus oponentes e desafios. Você pode não ser o Usain Bolt, mas com certeza, conseguirá vencer uma corrida contra uma tartaruga.',
     'Quando a vida der limões, não esqueça de pedir tequila e sal.',
     'Não deixe que o medo te impeça de seguir em frente. Afinal, as melhores histórias começam com: “segura a minha bebida e observe”.',
     'Não subestime o poder de um sorriso. Ele pode iluminar o seu dia e confundir as pessoas que não sabem o que você realmente está tramando.',
     'Assim como no Chat GPT, acredite nos seus sonhos, mas não dependa deles.',
     'Não existem batalhas impossíveis para quem está disposto a nunca desistir de tirar uma boa soneca.',
     'Em meio ao caos, respire fundo e olhe para fotos de gatinhos na internet.',
     'Algumas coisas ruins acontecem para aprendermos a ficar mais fortes, mais espertos ou mais desconfiados.',
     'Não desista de algo quando falarem que você não é capaz. Levante-se, mostre que você é capaz e ainda tire uma foto para postar no Instagram.',
     'Um dia você estará olhando para trás e pensando não apenas nas conquistas que você alcançou, mas também nas burradas que renderam boas risadas.',
     'Não coloque metas muito pesadas no seu caminho… a não ser que você seja crossfiteiro.',
     'Não tenha medo de sair da sua zona de conforto. Afinal, a vida é muito curta para passar todos os dias reassistindo “Todo Mundo Odeia o Chris” pela centésima vez.',
     'Seja tão corajoso quanto uma capivara atravessando uma rua movimentada.',
     'Ter sucesso é estar em paz com as nossas escolhas. Mesmo que a escolha do dia tenha sido ficar deitado tomando um sorvetinho em paz.',
     'A vida é como um trem: pessoas entram e saem, paisagens novas aparecem e, de vez em quando, uma criança vomita do seu lado.',
     'Seja como uma girafa: mantenha a cabeça erguida, mesmo quando o mundo parece conspirar para que você bata a cabeça.',
    ]



numFrase= randint(0,42)

frase = frases[numFrase]




def criarPasta():
    pasta = Path.cwd()
    novaPasta = pasta / nome
    print('Checando se a pasta já existe')

    loading = 50
    for i in range(loading):
        print("|",end="")
        time.sleep(0.02)

    if novaPasta.exists():
        print("\nNovo relatório gerado")
        
    else:
        novaPasta.mkdir()
        print('\nCriando uma nova pasta')

    print('Relatório Gerado!')
        

def criarArquivoPasta():
    pasta = Path(('./'+ nome))
    novoArquivo = pasta / (date.strftime("%d-%m-%Y") + '.txt')
    novoArquivo.write_text((f'Relatório Pessoal\n\n'
                            f'Nome: {nome}'
                            f'\nIdade: {idade} anos'
                            f'\nProfissão: {profissao}\n'
                            f'\n**** Frase do Dia ****'
                            f'\n{frase}'))


##def validacao:
    ##re.findall('[0123]')

while(cont):

    print("="*20, "Relatório Pessoal", "=" * 20)
    nome = str(input("Informe o seu nome: ")).capitalize()
    
    idade = int(input("Informe a sua idade: "))
    profissao = str(input("Informe a sua profissão: ")).capitalize()


    criarPasta()
    criarArquivoPasta()
    
    continuar = str(input("Deseja realizar outro relatório? (S/N): "))

    if continuar == "N":
        cont = False;
        sys.exit()
    



