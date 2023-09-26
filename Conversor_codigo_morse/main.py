#Ex02 - O código Morse é um esquema de codificação que usa traços e pontos para
#representar números e letras. Neste exercício, você escreverá um programa que
#usa um dicionário para armazenar o mapaeamento de letras e números para o
#código Morse. Use um ponto para representar um ponto e um hífen para representar
#um traço. O mapeamento de letras e números para traços e pontos é mostrado na
#Tabela.
#Seu programa deve ler uma mensagem do usuário. Em seguida, deve traduzir para
#código Morse, deixando um espaço entre cada sequência de traços e pontos. Seu
#programa deve ignorar quaisquer caracteres que não sejam letras ou números.
#O código Morse para Hello, World! É mostrado abaixo:
#.... . .-.. .-.. --- .-- --- .-. .-.. -..

import os



print("===" * 20, "\nTradutor de Código Morse")
print("===" * 20)


morse = {  #dicionario morse
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "- -.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--..",
    "0" : "-----",
    "1" : ".----",
    "2" : "..---",
    "3" : "...--",
    "4" : "....-",
    "5" : ".....",
    "6" : "-....",
    "7" : "--...",
    "8" : "---..",
    "9" : "----.",
    "!" : "!",
    "@" : "@",
    "#" : "#",
    "$" : "$",
    "%" : "%",
    "&" : "&",
    "*" : "*",
    "(" : "(",
    ")" : ")",
    "-" : "-",
    "=" : "=",
    "+" : "+",
    "[" : "[",
    "]" : "]",
    "{" : "{",
    "}" : "}",
    "," : ",",
    "." : ".",
    ";" : ";",
    ":" : ":",
    "/" : "/",
    "?" : "?",
    "\\": "\\",
    ">" : ">",
    "<" : "<",
    "|" : "|",
    " " : " "
    }

continuar = True 


while continuar:
    frase = [] #vai pegar letra por letra da entrada;
    frase_morse = [] #vai comparar letra por letra por meio do dicionario morse
    
    entrada = input(str("Digite alguma frase: ")).upper() #Vai transformar todas as letras em maiusculo


    for i in entrada: #para cada letra na entrada adicione na lista frase
        frase.append(i)

        for k, v in morse.items(): 

            if k == i: #Se a chave for igual a letra da lista frase, adicione o valor da chave na lista frase_morse
                frase_morse.append(v)


    frase = ' '.join(frase_morse) #Limpe a lista frase e junte os valores da lista frase_morse

    print(f"{entrada.capitalize()} traduzido(a) para Código Morse: \n{frase}") #mostre o resultado da junção da lista frase

    if input("Deseja traduzir alguma outra frase? (S/N): ").upper() == "N":
        continuar = False


print("Sistema finalizado")
        
            
    



