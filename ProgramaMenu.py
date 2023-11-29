from datetime import datetime, timedelta
import random
import time

def gerenciar_medicamentos():
    # Guardando dados
    nome_remedio = input("Informe o nome do remédio: ")
    horario_usuario = datetime.strptime(input("Digite o horário que tomou ou irá tomar o remédio (HH:MM): "), "%H:%M")
    meia_noite = datetime.strptime("00:00", "%H:%M")
    tomar = int(input("Digite de quantas em quantas horas voce deve tomar o remedio: "))

    print(f"\nPróximos horários para tomar o {nome_remedio}:")

    # Exibir horas a partir do horário informado
    horario_atual = horario_usuario
    while horario_atual < meia_noite + timedelta(days=1):
        print(horario_atual.strftime("%H:%M"))
        horario_atual += timedelta(hours=tomar)

def consulta_medica():
    num_carteirinha = int(input("Informe o número da sua carteirinha: "))

    print("\nAguarde que algum médico irá te atender em breve...")
    time.sleep(4)

def contato():
    print("Integrantes:\nBruno Hermano - RM553799\nChrisman Campos - RM554026\nLeonardo Macedo - RM552753\n")

def criar_conta():
    # Guardando dados
    nome = input("Informe seu nome completo: ")
    cpf = int(input("Informe seu cpf: "))
    rg = int(input("Informe seu RG: "))
    data_nasc = input("Informe sua data de nascimento: ")
    cidade = input("Informe sua cidade: ")
    endereco = input("Informe seu endereço completo: ")

    # Gerar o número de cadastro
    print("O número da sua carteirinha é: ", random.randint(100, 99999))

sair = 1
while (sair != 0):
    escolha = int(input("\nBem Vindo(a) a BCL Med!\n\nEscolha uma opção do menu:\n1-Gerenciamento de medicamentos\n2-Consulta médica\n3-Contato\n4-Criar conta\nEscolha:"))
    match escolha:
        case 1:
            gerenciar_medicamentos()
        case 2:
            consulta_medica()
        case 3:
            contato()
        case 4:
            criar_conta()
        case _:
            print("Opção invalida")
    sair = int(input("Deseja fazer outra interação? (0-Não 1-Sim): "))