import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def gra():
    pc = []
    ja = []
    pc.append(random.choice(cards))
    ja.append(random.choice(cards))
    ja.append(random.choice(cards))
    print(f"Dealer wylosował {pc}")
    print(f"Wylosowałeś {ja}")
    decyzja = input("Czy losować kolejną kartę? (tak/nie)\n")
    if decyzja == "tak":
        ja.append(random.choice(cards))

    pc.append(random.choice(cards))
    print(f"Dealer wylosowal kolejną kartę {pc}\n jego wynik to {sum(pc)}")

    if ja.count(11) != 0:
        if sum(ja) > 21:
            ja.remove(11)
            ja.append(1)

    print(f"Twoje karty to {ja}\n twój wynik to {sum(ja)}")

    if sum(ja) > 21:
        print("Przegrałeś starcze\n")
    elif sum(ja) > sum(pc):
        print("Wygrałeś kuglarzu\n")
    else:
        print("Przegrałeś starcze\n")
    rewanz = input("Możesz dalej tańczyć? (tak/nie)\n")
    if rewanz == "tak":
        gra()
    else:
        print("Koniec gry")


gra()
