from datetime import datetime
#tipo = input("PF ou PJ?")

date = datetime.now()

data = [date.strftime("%d"), date.strftime("%m"), date.strftime("%Y")]

hDia = int(data[0]) * 24
hMes = int(data[1]) * 24
hAno = int(data[2]) * 8.760


print(hDia)
print(hMes)
print(hAno) 


if(tipo == "pf"):
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF: ") 
    data = input("Data de Admissão da empresa (DD/MM/AAAA): ")
    teste = []
    

    
    holerit = [] 
    i = 1
    qnt = 1
    while(i <=3):
        salario = float(input("Salário {}º mês: ".format(qnt)))
        holerit.append(salario)
        qnt +=1
        i +=1

    print(holerit)

elif(tipo == "pj"):
    nome = input("Digite o nome fantasia da empresa: ")
    cpf = input("Digite o CNPJ: ")
    data = input("Data de criação da empresa: (DD/MM/AAAA) ")
    faturamento = []
    i = 1
    qnt = 1
    while(i <=3):
        lucro = float(input("Faturamento {}º mês: ".format(qnt)))
        faturamento.append(lucro)
        qnt +=1
        i +=1

    print(faturamento)



