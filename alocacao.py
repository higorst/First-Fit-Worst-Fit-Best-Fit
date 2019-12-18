def ff(npa, npo, pa, po):
	print("\nFIRST-FIT")
	print("No. Processo - Tamanho Processo - No. Particao - Tamanho Particao - Sobra")

	i = 1
	processo_usado = []
	particao_usado = []
	for processo in po: # necessario percorrer todos os processos para alocar
		j = 1
		for particao in pa: # percorrer as particoes ate encontrar uma que caiba			
			if (processo <= particao and 
				processo not in processo_usado and 
				particao not in particao_usado): # verificar se particao aceita processo

				print("   ", end="")
				print("",i, 
					  "                ", processo, 
					  "            ", j, 
					  "            ", particao, 
					  "         ", (particao - processo))
				particao_usado.append(particao)
				processo_usado.append(processo)
			j = j + 1 # para saber o numero da particao
		i = i + 1 # para saber o numero do processo

	i = 1
	# verificar processos em espera
	for processo in po:
		if (processo not in processo_usado): # verificar se processo nao foi aceito
			print("   ", end="")
			print("", i, "                 Em espera")
		i = i + 1 # para saber o numero do processo

	print()

def bf(npa, npo, pa, po):
	print("\nBEST-FIT")
	print("No. Processo - Tamanho Processo - No. Particao - Tamanho Particao - Sobra")

	# para cada processo **
	# primeiro: verificar qual a menor particao
	#			desde que comporte o processo
	# segundo: realizar a aceitacao do processo

	i = 1
	processo_usado = []
	particao_usado = []
	for processo in po: # necessario percorrer todos os processos para alocar
		j = 1

		# qual a menor particao que aceita o processo?
		menor_particao = max(pa)
		for part_m in pa:
			if menor_particao > part_m and processo <= part_m and part_m not in particao_usado:
				menor_particao = part_m

		for particao in pa: # percorrer as particoes ate a menor escolhida
			if particao == menor_particao and processo not in processo_usado and menor_particao not in particao_usado:

				print("   ", end="")
				print("",i, 
					  "                ", processo, 
					  "            ", j, 
					  "            ", particao, 
					  "         ", (particao - processo))
				particao_usado.append(particao)
				processo_usado.append(processo)
			j = j + 1 # para saber o numero da particao
		i = i + 1 # para saber o numero do processo

	i = 1
	# verificar processos em espera
	for processo in po:
		if (processo not in processo_usado): # verificar se processo nao foi aceito
			print("   ", end="")
			print("", i, "                 Em espera")
		i = i + 1 # para saber o numero do processo

	print()

def wf(npa, npo, pa, po):
	print("\nWORST-FIT")
	print("No. Processo - Tamanho Processo - No. Particao - Tamanho Particao - Sobra")

	# para cada processo **
	# primeiro: identificar particao maior nao usada
	# segundo: realizar a aceitacao do processo

	i = 1
	processo_usado = []
	particao_usado = []
	for processo in po: # necessario percorrer todos os processos para alocar
		j = 1
		n_aceitou = True # flag para identificar processo em espera
		# qual a maior particao que aceita o processo?
		menor_particao = min(pa)
		for part_m in pa:
			if menor_particao < part_m and processo <= part_m and part_m not in particao_usado:
				menor_particao = part_m

		for particao in pa: # percorrer as particoes ate a menor escolhida
			if particao == menor_particao and processo <= particao and processo not in processo_usado and menor_particao not in particao_usado:

				n_aceitou = False
				print("   ", end="")
				print("",i, 
					  "                ", processo, 
					  "            ", j, 
					  "            ", particao, 
					  "         ", (particao - processo))
				particao_usado.append(particao)
				processo_usado.append(processo)
			j = j + 1 # para saber o numero da particao
		if n_aceitou:
			print("   ", end="")
			print("", i, "                 Em espera")
		i = i + 1 # para saber o numero do processo

	print()


npa = 0		# numero de particoes
npo = 0		# numero de processos
pa = [] 	# vetor com informacoes do tamanho de cada particao
po = [] 	# vetor com informacoes do tamanho de cada processo

print("\n\tMetodo de Alocacao")

print("\nDefina o numero de particoes:", end=" ")
npa = int(input())

print("Defina o numero de processos:", end=" ")
npo = int(input())

print("\nDefina o tamanho de cada particao")

for i in range(npa):
	print("Particao", i + 1, end=" = ")
	pa.append(int(input()))

print("\nDefina o tamanho de cada processo:")

for i in range(npo):
	print("Processo", i + 1, end=" = ")
	po.append(int(input()))

ff(npa, npo, pa, po)
bf(npa, npo, pa, po)
wf(npa, npo, pa, po)