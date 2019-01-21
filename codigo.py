with open ('example.txt') as archivo:
	#print archivo.read()
	op = ''
	comienzo = 0
	contador = 1
	for x in archivo.read().split("\n"):
		if(x == '*****'):
			if(comienzo == 1):
				with open(str(contador)+ '.txt','w') as res:
					res.write(op)
					res.close()
					op=''
					contador+=1

			else:
				comienzo=1

		else:
			if(op==''):
				op=x
			else:
				op = op + '\n' + x	

	archivo.close()