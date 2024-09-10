from customtkinter import *
from PIL import Image

app = CTk()
app.geometry("500x400")

set_appearance_mode("light")

btn = CTkButton(master=app, text="Click", corner_radius=32, fg_color="#FC6A03", hover_color="#FCAE1E",)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)


app.mainloop()

# Funcao para registar as equipas que pretende sortear
def adicionar_equipas():
    # Lê a quantidade de equipas
    numero_equipas = int(input("Diga o numero de equipas que deseja sortear: "))

    # Array para guardar as equipas
    equipas = []

    # Loop para introduzir o nome de cada equipa
    for i in range(numero_equipas):
        while True:
            equipa = input(f"Diga o nome da equipa {i + 1}: ")

            # Verifica se a equipa já foi registada
            if equipa in equipas:
                print("Essa equipa já foi registada. Tente novamente.")
            else:
                equipas.append(equipa)
                break

    # Retonar equipas
    return equipas


equipas_adicionadas = adicionar_equipas()
print("Lista de quipas adicionadas:", equipas_adicionadas)

# Funcao para calcular automaticamente o numero de jornadas possiveis
def calcular_jornadas(equipas):
    # Numero total de equipes
    numero_equipas = len(equipas)

    # Verifica se o numero de equipas e par
    if numero_equipas % 2 != 0:
        equipas.append("Folga")
        numero_equipas = numero_equipas + 1

    # Numero de jornadas
    numero_jornada = 1

    # Numero maximo de jornadas possiveis
    numero_jornadas = len(equipas) - 1

    # Numero de jogos por cada jornada
    numero_jogos = len(equipas) // 2

    verificar_casa_fora = input("Existem jogos em casa e fora contra a mesma equipa? (sim/nao): ")

    if verificar_casa_fora in ["não", "n" , "Não" , "NAO",  "nao" , "Nao" , "NÃO"]:
        print("\n PRIMEIRA VOLTA")
        for i in range(numero_jornadas):
            print(f"\t Jornada { i + 1 }")
            for j in range(numero_jogos):
                equipa1 = equipas[j]
                equipa2 = equipas[-(j + 1)]
                print(f"\t {equipa1} X {equipa2}")

            equipas = [equipas[0]] + [equipas[-1]] + equipas[1:-1]

    elif verificar_casa_fora in ["sim", "s" , "Sim" , "SIM"]:
        print("\n PRIMEIRA VOLTA")
        for i in range(numero_jornadas):
            print(f"\n Jornada {i + 1}")
            for j in range(numero_jogos):
                equipa1 = equipas[j]
                equipa2 = equipas[-(j + 1)]
                print(f"\t {equipa1} X {equipa2}")

            equipas = [equipas[0]] + [equipas[-1]] + equipas[1:-1]

        print("\n SEGUNDA VOLTA")
        for i in range(numero_jornadas):
            print(f"\n Jornada {i + 1 + numero_jornadas}:")
            for j in range(numero_jogos):
                equipa1 = equipas[-(j + 1)]
                equipa2 = equipas[j]
                print(f"\t {equipa1} X {equipa2}")

            equipas = [equipas[0]] + [equipas[-1]] + equipas[1:-1]


jornadas = calcular_jornadas(equipas_adicionadas)



