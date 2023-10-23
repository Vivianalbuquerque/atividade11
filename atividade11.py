distancia =float(input("qual foi a distância percorida em km ?"))
d_curta = 0.50
d_longa = 0.45
if distancia>=200:
    preço = distancia * d_longa
    print(f"O valor total gastado foi de {preço}")
elif distancia<200:
    preço = distancia * d_curta
    print(f"O valor total gastado foi de {preço}")