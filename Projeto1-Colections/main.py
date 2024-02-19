#  COLEÇÕES

# TUPLA (É  uma coleção imutável)
# nomes = ('Goku', 'Vegeta', 'Trunks', 'Gohan')
# nomes[0] = 'Picolo' # Não dá pra mudar
# Slicing de dados:
# print(nomes)
# print(nomes[0])
# print(nomes[:2])
# print(nomes[1:3])
# print(nomes[-2])

# Listas [A mais popular e 300% mutavel]

# nomes = ['Goku', 'Vegeta', 'Trunks', 'Gohan']
# #add
# nomes.append('Picollo')
# #Update
# nomes[0] = 'Bulma'
# #Delete
# nomes.remove('Trunks') #Remove por valor
# del nomes[1] #Remove por indice
# #Select
# print(nomes)

#Conjunto {Do inglês set, não guarda ordem, não repete}

nomes = {'Goku', 'Vegeta', 'Trunks', 'Gohan'}
nomes.add('Bulma')
nomes.add('Goku')
print(nomes)
