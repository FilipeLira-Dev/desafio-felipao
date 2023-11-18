nome_heroi = input('Qual o nome do seu Herói? ')
nivel_heroi = int(input('Qual o nível do seu Herói? '))

if nivel_heroi <= 1000:
    nivel_heroi = 'Ferro'
elif nivel_heroi <= 2000:
    nivel_heroi = 'Bronze'
elif nivel_heroi <= 5000:
    nivel_heroi = 'Prata'
elif nivel_heroi <= 7000:
    nivel_heroi = 'Ouro'    
elif nivel_heroi <= 8000:
    nivel_heroi = 'Platina'
elif nivel_heroi <= 9000:
    nivel_heroi = 'Ascendente'
elif nivel_heroi <= 10000:
    nivel_heroi = 'Imortal'
else:
    nivel_heroi = 'Radiante'
    
print(f'O Herói de nome {nome_heroi} está no nível de {nivel_heroi}')