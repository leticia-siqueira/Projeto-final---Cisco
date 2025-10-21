from random import randrange


def painel(quadro):
	print("+-------" * 3,"+", sep="")
	for linha in range(3):
		print("|       " * 3,"|", sep="")
		for coluna in range(3):
			print("|   " + str(quadro[linha][coluna]) + "   ", end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")


def enter_move(quadro):
	ok = False	
	while not ok:
		movimento = input("Digite seu movimento: ") 
		ok = len(movimento) == 1 and movimento >= '1' and movimento <= '9' 
		if not ok:
			print("Má jogada, repita sua entrada!") 
			continue
		movimento = int(movimento) - 1 	
		linha = movimento // 3 	
		coluna = movimento % 3		
		sinal = quadro[linha][coluna]	
		ok = sinal not in ['O','X'] 
		if not ok:	
			print("Campo já ocupado, repita sua entrada!")
			continue
	quadro[linha][coluna] = 'O' 	


def campo_livre(quadro):
	livre = []	
	for linha in range(3): 
		for coluna in range(3): 
			if quadro[linha][coluna] not in ['O','X']: 
				livre.append((linha,coluna)) 
	return livre


def vitoria(quadro,jogada):
	if jogada == "X":	
		quem = 'eu'	
	elif jogada == "O": 
		quem = 'voce'	
	else:
		quem = None	
	diagonal1 = diagonal2 = True  
	for rc in range(3):
		if quadro[rc][0] == jogada and quadro[rc][1] == jogada and quadro[rc][2] == jogada:	
			return quem
		if quadro[0][rc] == jogada and quadro[1][rc] == jogada and quadro[2][rc] == jogada: 
			return quem
		if quadro[rc][rc] != jogada: 
			diagonal1 = False
		if quadro[2 - rc][2 - rc] != jogada: 
			diagonal2 = False
	if diagonal1 or diagonal2:
		return quem
	return None


def desenhar(quadro):
	livre = campo_livre(quadro) 
	cnt = len(livre)
	if cnt > 0:	
		this = randrange(cnt)
		linha, coluna = livre[this]
		quadro[linha][coluna] = 'X'


quadro = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] 
quadro[1][1] = 'X' 
livre = campo_livre(quadro)
humano = True 
while len(livre):
	painel(quadro)
	if humano:
		enter_move(quadro)
		vencer = vitoria(quadro,'O')
	else:	
		desenhar(quadro)
		vencer = vitoria(quadro,'X')
	if vencer != None:
		break
	humano = not humano		
	livre = campo_livre(quadro)

painel(quadro)
if vencer == 'voce':
	print("Você venceu!")
elif vencer == 'eu':
	print("Eu ganhei!")
else:
	print("Empate!")