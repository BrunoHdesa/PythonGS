from datetime import datetime, timedelta

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

gerenciar_medicamentos()
