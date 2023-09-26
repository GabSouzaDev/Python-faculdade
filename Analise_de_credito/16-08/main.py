import datetime
from random import randint


dataTratada = None #permite acessar fora da função
date = datetime.date.today() #pega a data de hoje
PERCENTUAL = 40 #constante, não pode ser alterada ao meio do programa.



tipo = int(input("Pessoa Física (1)\nPessoa Jurídica (2)\nColoque sua opção: "))

def calcularData():
    global tipo, date, data, dataTratada

    splDt = data.split('/') #corta a data e separa em indices

    dataTratada = datetime.date(int(splDt[2]), int(splDt[1]), int(splDt[0])) #organiza a data inserida pelo usuário em formato global
    calc = date-dataTratada #Calcula a diferença de dias

    if tipo == 1 and calc.days < 90 or tipo == 2 and calc.days < 450: #days é uma palavra reservada do próprio python para calcular aritméticamente as datas.
        print("Você não foi aprovado para este crédito!\n Volte em 3 meses para tentar uma nova aprovação")

        return False
    else:
        #Aprovado, hora de calcular a renda;
        
        return True


def calcularLimite():
    global splLst, renda
    splLst = renda.split(',') #corta os valores e separa em indice
    media = (float(splLst[0]) + float(splLst[1]) + float(splLst[2])) / 3 #calculando média da renda 
    #print(splLst)
    limite = (media * PERCENTUAL) / 100 #calculando crédito em cima dos 40%
    print("Parabéns, você foi aprovado no nosso sistema!\nSerá liberado um crédito de R${:.2f} na sua conta.".format(limite))

    return media, limite #retorna os valores de media e limite para ser acessado fora da função.
        

    

if(tipo == 1):
    nome = input("Nome Completo: ")
    cpf = input("CPF: ")
    data = input("Data de Admissão (DD/MM/AAAA): ")
    
    if calcularData(): #Se a função calcularData() retornar True, então execute:
        renda = input("informe seus 3 ultimos salários recebidos (separados por virgula): ")
        media, limite = calcularLimite() #aqui estamos atribuindo os valores retornados em calcularLimite() para ser acrescido no comprovante ao final.
    

                
elif(tipo == 2):
    razao = input("Nome Fantasia: ")
    cnpj = input("CNPJ: ")
    data = input("Data de criação da empresa (DD/MM/AAAA): ")

    if calcularData():
        renda = input("informe seus 3 ultimos faturamentos recebidos (separados por virgula): ")
        media, limite = calcularLimite()


comprovante = input("Gerar comprovante? (S/N): ")

cdCorrespondente = randint(78342345, 99999999) #Gera um código aleatório com 99,00000001% de ser exclusivo
cdAuth = randint(679034562, 999999999)
nvSolicitacao = date + datetime.timedelta(days=90) #Calcula a data de nova solicitação com base na data atual.
#nvSolicitacao = dataTratada + datetime.timedelta(days=90) #Calcula a data de nova solicitação com base na data de admissao/criacao.


if(comprovante == "S" or "s"):
    if(tipo == 1 and calcularData()):
        print("""----------Comprovante----------\n
              Credor: {}\n
              CPF: {}\n
              Data de Admissão: {}\n
              Média Salarial: R${:.2f}\n
              Análise aprovada? {}\n
              Percentual do limite: {}%\n
              Limite liberado: R${:.2f}\n
              Codigo Correspondente: {}\n
              Código de autenticação: {}""".format(nome, cpf, data, media, "Sim", PERCENTUAL, limite, cdCorrespondente, cdAuth))
    elif(tipo == 2 and calcularData()):
        print("""----------Comprovante----------\n,
              Credor: {}\n
              CNPJ: {}\n
              Data de Admissão: {}\n
              Média Salarial: R${:.2f}\n
              Análise aprovada? {}\n
              Percentual do limite: {}%\n
              Limite liberado: R${:.2f}\n
              Codigo Correspondente: {}\n
              Código de autenticação: {}""".format(razao, cnpj, data, media, "Sim", PERCENTUAL, limite, cdCorrespondente, cdAuth))
    else:
        print("""----------Comprovante----------\n,
              Credor: {}\n
              CPF/CNPJ: {}\n
              Análise aprovada? {}\n
              Data de Solicitação: {}\n
              Data para nova Solicitação: {}\n
              Codigo Correspondente: {}\n
              Código de autenticação: {}""".format(nome or razao, cpf or cnpj, "Não", date.strftime("%d/%m/%Y"), nvSolicitacao.strftime("%d/%m/%Y"), cdCorrespondente, cdAuth)) #strftime permite mudar o formato da data
else:
    print("Processo finalizado, tenha um bom dia!")
        
        
        
        

        

    
    

    
