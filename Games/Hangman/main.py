import random


def string(x):
    new = ""
    for i in x:
        new += i
    return new


slowa = ["beagle", "corgi", "samoyed", "owczarek"]
slowko = random.choice(slowa)
haslo = ""
for i in slowko:
    haslo += "_"

print(haslo)

slowko = list(slowko)
haslo = list(haslo)
zycia = 5

while slowko != haslo and zycia > 0:

    x = input("Choose a letter:\n")
    if slowko.count(x) != 0:
        for k in range(len(slowko)):
            if x == slowko[k]:
                haslo[k] = x
        print(string(haslo))
    else:
        zycia -= 1
        print(f"Unfortunately no, you have {zycia} lives left")
        print(string(haslo))
print(f"Game over you have {zycia} lives\n the correct word is {string(slowko)}")
