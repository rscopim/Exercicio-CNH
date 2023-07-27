rodas = int (input("Qual a quantidade de rodas no veículo: "))
peso = int (input("Qual o peso do veículo: "))
pessoas = int (input("Quantidade de pessoas no veículo: "))

if (rodas <= 3):
    print("A sua categoria de CHN é: A")    
if (rodas >= 4) and (pessoas <= 8) and (peso <= 3500):
    print("A sua categoria de CHN é: B")
if (rodas >= 4) and (peso >= 3500 or peso <= 6000):
    print("A sua categoria de CHN é: C")
if (rodas >= 4) and (pessoas >= 8) and (peso >= 3500 or peso <= 6000):
    print("A sua categoria de CHN é: D") 

print("Agradecemos a consulta")