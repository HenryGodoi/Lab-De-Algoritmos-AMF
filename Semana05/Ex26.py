
print("--- Valor das fruteiras ---")
print("\nAté 5 Kg:")
print("Morango = 2,50 por Kg.")
print("Maçã = 1,80 por Kg.")

print("\nAcima de 5 Kg:")
print("Morango = 2,20 por Kg.")
print("Maçã = 1,50 por Kg.")

morango = float(input("Digite quantos Kg são: "))
maca = float(input("Digite quantos Kg são: "))

frutastotal = morango + maca

if morango <= 5:
    morangov = morango * 2.50
elif morango > 5:
    morangov = morango * 2.20
elif maca <= 5:
    macav = maca * 1.80
elif maca > 5:
    macav = maca * 1.50

valortotal = macav + morangov

if frutastotal > 8 or valortotal > 25:
    valorfinal = valortotal - (valortotal * 0.10)
    print(f"O valor a ser pago será: {valorfinal}")
else:
    print(f"O valor a ser pago será: {valortotal}")
