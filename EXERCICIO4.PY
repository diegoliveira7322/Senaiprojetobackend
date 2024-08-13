# armazenar os votos
votos = {'BOULOS INVADI TERRA VAI MATA': 0, 'faz o L': 0, 'aero frango': 0, 'patricio poeto marçal': 0}

# Ler os votos para cada candidato
for i in range(1, 5):
    voto = int(input(f"Digite o número do candidato que recebeu o voto ({i}/4): "))
    
    # Atualizar o número de votos baseado na entrada
    match voto:
        case 1:
            votos['BOULOS INVADI TERRA VAI MATA'] += 1
        case 2:
            votos['faz o L'] += 1
        case 3:
            votos['aero frango'] += 1
        case 4:
            votos['patricio poeto marçal'] += 1
        case _:
            print("Número de candidato inválido!")

# Mostrar o número de votos de cada candidato
for candidato, quantidade in votos.items():
    print(f"{candidato}: {quantidade} votos")