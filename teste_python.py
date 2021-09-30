# ----------------------------------------------------------
# Author: Fábio Barros
# 21/09/2021
# Desafio Python para vaga de desenvolvedor Backend
# ----------------------------------------------------------

import os
from time import sleep

def question1(target):
	try:
		baseList = [3, 5, 7, 9]
		print("Lista base: ", baseList)
		result = []
		if target.isnumeric():
			target = int(target)
			if target < baseList[0]: 
				raise Exception("Número não pode ser menor que o menor número da lista: %s" %(baseList[0]))

			for item1 in baseList:
				if len(result) == 0:
					for item2 in baseList:
						if (item1+item2) == target:
							result.append(baseList.index(item1))
							result.append(baseList.index(item2))
		print(result)
		else:
			raise Exception("Número inválido!")
		return result
	except:
		raise 

def question2(string):
	try:
		baseList = [['(', ')'], ['[', ']'], ['{', '}']] 
		length = len(string)

		result = (length % 2) == 0

		if result:
			x = int(length/2)
			firstPart = string[:x]
			lastPart = string[x:]
			
			# inverte a parte final da expressão
			# exemplo: {[]}
			# firstPart = '{['   lastPart = ']}'   
			# lastPart[::-1] = '}]'
			lastPart = lastPart[::-1] 

			result = True
			for first in firstPart:
				index = firstPart.index(first)
				for item in baseList:
					if first in item: # só muda result se o caracter for encontrado dentro da matriz
						result = result and first in item and lastPart[index] in item
		return result
	except:
		raise

def getBuyValue(baseList):
	result = -1
	while result == -1 and len(baseList) > 0:
		result = min(baseList)
		posMinValue = baseList.index(result)
		if posMinValue == (len(baseList)-1):
			baseList.remove(result)
			result = -1
	return result

def getSellValue(baseList, buyValue):
	result = -1
	x = baseList.index(buyValue) + 1
	while result == -1:
		result = max(baseList)
		posMaxValue = baseList.index(result)
		if posMaxValue < baseList.index(buyValue):
			baseList.remove(result)
			result = -1
	return result


def question3(string):
	try:
		if string == '': 
			string = '7,1,5,3,6,4'
			print("Nenhum valor informado. Utilizando valor default: %s" %(string))
		baseString = string.split(',')
		baseList = list(map((lambda x: int(x) if x.isnumeric() else x), baseString))
		print("Lista Base Original: %s" %(baseList))

		buyValue = getBuyValue(baseList)
		if buyValue != -1:
			sellValue = getSellValue(baseList, buyValue)
		else:
			raise Exception ("Não é possível efetuar operação de compra e venda para essa sequencia!")

		print("Lista Base Final: %s" %(baseList))
		return sellValue-buyValue
	except:
		raise

def question4():
	try:
		return "Não implementado!"
	except:
		raise


loop = True
while loop:
	os.system('clear')
	option = 0

	print("Selecione o número da questão desejada: ")
	print("")
	print("1 - Questão 1")
	print("2 - Questão 2")
	print("3 - Questão 3")
	print("4 - Questão 4")
	print("")
	print("5 - Sair")
	print("")

	validOptions = (1,2,3,4,5)
	option = input("Informe a opção desejada: ")
	try:
		if option.isnumeric(): 
			option = int(option)
			
			if option in validOptions:
				
				if option == 1:
					result = list(question1(input("Informe o valor alvo inteiro: ")))
					if result != []:
						print(result)
				
				elif option == 2:
					print(question2(input("Informe a sequencia de caraceteres : ")))

					
				elif option == 3:
					string = input("Digite uma sequencia de valores, separados por vírgula (exemplo: 1, 2, 3, 4): ")
					print(question3(string))
				
				elif option == 4:
					print(question4())
				
				elif option == 5:
					print("Muito obrigado pela oportunidade!")
					loop = False
				
				else:
					print("Opção inválida!")
			else:
				print("Opção inválida!")
		else:
			print("Opção inválida!")
	except Exception as err:
		print(err)

	finally:
		input("")

