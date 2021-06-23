import pickle 
import smtplib
from datetime import datetime
from pytz import timezone
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Verificando os arquivos ___________________________________________________

def verificarArquivoReceitas():
	receitas = {}
	try:
		arqReceitas = open("receitas.dat", "rb")
		receitas = pickle.load(arqReceitas)
		arqReceitas.close()
	except IOError:
		print("Erro ao abrir o arquivo")
		print("Base de dados está vazia!")
		
	return receitas

def verificarArquivoDespesas():
	despesas = {}	
	try:
		arqDespesas = open("despesas.dat", "rb")
		despesas = pickle.load(arqDespesas)
		arqDespesas.close()
	except IOError:
		print("Erro ao abrir o arquivo")
		print("Base de dados está vazia!")
	
	return despesas

def verificarArquivoPagamentos():
	pagamentos = {}
	try:
		arqPagamentos = open("pagamentos.dat", "rb")
		pagamentos = pickle.load(arqPagamentos)
		arqPagamentos.close()
	except IOError:
		print("Erro ao abrir o arquivo")
		print("Base de dados está vazia!")
	
	return pagamentos
	
def verificarArquivoCarteira():
	carteira = {}
	try:
		arqCarteira = open("carteira.dat", "rb")
		carteira = pickle.load(arqCarteira)
		arqCarteira.close()
	except IOError:
		print("Erro ao abrir o arquivo")
		print("Base de dados está vazia!")
	
	return carteira

def verificarArquivoContas():
	contas = {}
	try:
		arqContas = open("contas.dat",'rb')
		contas = pickle.load(arqContas)
		arqContas.close()
	except:
		print("Erro ao abrir o arquivo")
		print("Base de dados está vazia!")
		
	return contas

def verificarArquivoSaques():
	saques = {}
	try:
		arqSaques = open("saques.dat", "rb")
		saques = pickle.load(arqSaques)
		arqSaques.close()
	except IOError:
		print("Erro ao abrir o arquivo")
		print("Base de dados está vazia!")
		
	return saques

def verificarArquivoDepositos():
	depositos = {}
	try:
		arqDepositos = open("depositos.dat", "rb")
		depositos = pickle.load(arqDepositos)
		arqDepositos.close()
	except IOError:
		print("Erro ao abrir o arquivo")
		print("Base de dados está vazia!")
		
	return depositos

def verificarArquivoTransferencias():
	transferencias = {}
	try:
		arqTransferencias = open("transferencias.dat", "rb")
		transferencias = pickle.load(arqTransferencias)
		arqTransferencias.close()
	except IOError:
		print("Erro ao abrir o arquivo")
		print("Base de dados está vazia!")

	return transferencias
	
receitas = verificarArquivoReceitas()
despesas = verificarArquivoDespesas()
pagamentos = verificarArquivoPagamentos()
carteira = verificarArquivoCarteira()
contas = verificarArquivoContas()
saques = verificarArquivoSaques()
depositos = verificarArquivoDepositos()
transferencias = verificarArquivoTransferencias()


def gravarArquivoReceitas():
	arqReceitas = open("receitas.dat", "wb")
	pickle.dump(receitas, arqReceitas)
	arqReceitas.close()

def gravarArquivoDespesas():
	arqDespesas = open("despesas.dat", "wb")
	pickle.dump(despesas, arqDespesas)
	arqDespesas.close()

def gravarArquivoCarteira():
	arqCarteira = open("carteira.dat", "wb")
	pickle.dump(carteira, arqCarteira)
	arqCarteira.close()

def gravarArquivoContas():
	arqContas = open("contas.dat", "wb")
	pickle.dump(contas, arqContas)
	arqContas.close()		

def gravarArquivoSaques():
	arqSaques = open("saques.dat", "wb")
	pickle.dump(saques, arqSaques)
	arqSaques.close()	

def gravarArquivoDepositos():
	arqDepositos = open("depositos.dat", "wb")
	pickle.dump(depositos, arqDepositos)
	arqDepositos.close()	

def gravarArquivoTransferencias():
	arqTransferencias = open("transferencias.dat", "wb")
	pickle.dump(transferencias, arqTransferencias)
	arqTransferencias.close()	 

def gravarArquivoPagamentos():
	arqPagamentos = open("pagamentos.dat", "wb")
	pickle.dump(pagamentos, arqPagamentos)
	arqPagamentos.close()	 

def menu():
	print("-------------------- PyFinance -----------------------")
	print("|                        |                           |")
	print("|  1. Adicionar receita  | 14. Gerenciar Carteira    |")
	print("|  2. Buscar receita     | 15. Adicionar conta banc. |")
	print("|  3. Excluir receita    | 16. Buscar conta banc.    |")
	print("|  4. Editar receita     | 17. Excluir conta banc.   |")
	print("|  5. Listar receitas    | 18. Editar conta banc.    |")
	print("|  6. Adicionar despesa  | 19. Listar contas banc.   |")
	print("|  7. Buscar despesa     | 20. Realizar Saque        |")
	print("|  8. Excluir despesa    | 21. Realizar Depósito     |")
	print("|  9. Editar despesa     | 22. Realizar Transfer.    |")
	print("| 10. Listar despesas    | 23. Emitir Saldo          |")
	print("| 11. Pagar despesa      | 24. Emitir Extrato        |")
	print("| 12. Relatório mensal   | 0. Encerrar Programa      |")
	print("| 13. Relatório Anual    |                           |")
	print("|                        |                           |")
	print("------------------------------------------------------\n")
	resp = input("Informe sua opção: ")

	return resp

def gerarData():
		data = datetime.now()
		fuso_horario = timezone("America/Sao_Paulo")
		data_a = data.astimezone(fuso_horario)
		data_f = data_a.strftime("%d/%m/%Y %H:%M:%S")

		return data_f

def nomeMes(mes):

	if mes == "01":
		mes1 = "Janeiro"

	elif mes == "02":
		mes1 = "Fevereiro"

	elif mes == "03":
		mes1 = "Março"

	elif mes == "04":
		mes1 = "Abril"

	elif mes == "05":
		mes1 = "Maio"

	elif mes == "06":
		mes1 = "Junho"

	elif mes == "07":
		mes1 = "Julho"

	elif mes == "08":
		mes1 = "Agosto"

	elif mes == "09":
		mes1 = "Setembro"

	elif mes == "10":
		mes1 = "Outubro"

	elif mes == "11":
		mes1 = "Novembro"

	elif mes == "12":
		mes1 = "Dezembro"

	else:
		mes1 = "Inválido"
		print("\nMês inválido.\n")
	
	mes1 = mes1.upper()

	return mes1


# Funcoes da Receita ______________________________________________________________________ 

def addReceita():
	achou = False
	print("\nMódulo - Adicionar Receita Financeira\n")
	print(" ATENÇÃO: -----------------------------")
	print("|                                     |")
	print("| Não insira vírgulas no campo valor, |")
	print("| apenas insira um ponto antes dos    |")
	print("| centavos.                           |")
	print("|                                     |")
	print("---------------------------------------\n")

	descricao = input("Informe a descrição da receita : ")
	descricao = descricao.upper()
	valor = float(input("Informe o valor da receita     : "))
	data_f = gerarData()

	for key, value in receitas.items():
		if data_f == key:
			achou = True
			
	if achou == True:
			print("A receita informada ja está registrada!")
	else:
		receitas[data_f] = [descricao, valor]  
		print("\nReceita Financeira adicionada.")
		print("Horário de cadastro: %s"%data_f)
		print()
	
def buscarReceita():
	print("\nMódulo - Buscar Receita Financeira\n")
	print("a) Digite 'a' para buscar pela data")
	print("b) Digite 'b' para buscar pela descrição\n")

	busca = input("Informe o tipo de busca: ")

	if busca.lower() == "a":
		print("\nModulo - Buscar pela data\n")
		print(" ATENÇÃO ----------------------------------")
		print("|                                         |")
		print("| Caso não saiba a data completa, informe |")
		print("| pelo menos uma parte dela.              |")
		print("|                                         |")
		print("| Formato da data: dd/mm/aaaa HH:MM:SS.   |")
		print("|                                         |")
		print("-------------------------------------------\n")
		data_f = input("Informe a data de cadastro da receita: ")
		achou = False
		print()
		print()
		
		print("-" * 59)
		print("%-20s | %-20s | %-15s"%("DATA:","DESCRIÇÃO:","VALOR:"))
		print("-" * 21,"-" * 21,"-" * 15)

		for key,value in receitas.items():
			if data_f in key:
				print("%-20s | %-20s | %-15s"%(key,receitas[key][0],"R$ " + str(receitas[key][1])))		
				achou = True

		print("-" * 59)

		if achou == False:
			print("\nNão há registro de receitas com a data informada.\n")
		
		print()
		print()
	
	elif busca.lower() == "b":
		print("\nMódulo - Buscar pela descrição\n")
		print(" ATENÇÃO ----------------------------------")
		print("|                                         |")
		print("| Caso não saiba a descrição completa,    |")
		print("| informe pelo menos o início.            |")
		print("|                                         |")
		print("-------------------------------------------\n")
		descricao = input("Informe a descrição da receita à buscar: ")
		descricao = descricao.upper()
		achou = False
		print()
		print()

		print("-" * 59)
		print("%-20s | %-20s | %-15s"%("DATA:","DESCRIÇÃO:","VALOR:"))
		print("-" * 21,"-" * 21,"-" * 15)

		for key, value in receitas.items():
			if (receitas[key][0]).startswith(descricao):
				print("%-20s | %-20s | %-15s"%(key,receitas[key][0],"R$ " + str(receitas[key][1])))	
				achou = True

		print("-" * 59)

		if achou == False:
			print("Não há registro de receitas com a descrição informada.\n")
		
		print()
		print()
	
	else:
		print("\nVocê informou um valor inválido para esta operação.\n")

def excluirReceita():
	print("\nMódulo - Excluir Receita Financeira\n")
	print(" ATENÇÃO: -------------------------------")
	print("|                                       |")
	print("| Para excluir uma receita você deve    |")
	print("| informar a data completa de cadastro  |")
	print("| da receita.                           |")
	print("|                                       |")
	print("| Formato da data: dd/mm/aaaa HH:MM:SS. |")
	print("|                                       |")
	print("-----------------------------------------\n")
	data_f = input("Informe a data de cadastro da receita: ")
	print()
	print()
	
	if data_f in receitas:
		print(" RECEITA FINANCEIRA LOCALIZADA!")
		print("-" * 63)
		print(" %-20s | %-20s | %-20s"%("DATA:","DESCRIÇÃO:","VALOR:"))
		print("-" * 22,"-" * 22,"-" * 17)
		print(" %-20s | %-20s | %-20s"%(data_f,receitas[data_f][0],"R$ " + str(receitas[data_f][1])))
		print("-" * 63)
		print()
		print()

		confirma = input("Confirma a exclusão desta receita (S/N) ? ")
		print()

		if confirma.upper() == "S":
			del receitas[data_f]
			print("Receita Financeira excluída.\n")

		elif confirma.upper() == "N":
			print("Operação cancelada.\n")

		else:
			print("Você informou um valor inválido para esta operação.\n")

	else:
		print("Não há registro de receitas com a data informada.\n")

def editarReceita():
	print("\nMódulo - Editar Receita Financeira\n")
	print(" ATENÇÃO: -------------------------------")
	print("|                                       |")
	print("| Para editar uma receita você deve     |")
	print("| informar a data completa de cadastro  |")
	print("| da receita.                           |")
	print("|                                       |")
	print("| Formato da data: dd/mm/aaaa HH:MM:SS. |")
	print("|                                       |")
	print("-----------------------------------------\n")
	data_f = input("Informe a data de cadastro da receita: ")
	print()
	print()
	
	if data_f in receitas:

		print(" RECEITA FINANCEIRA LOCALIZADA!")
		print("-" * 63)
		print(" %-20s | %-20s | %-20s"%("DATA:","DESCRIÇÃO:","VALOR:"))
		print("-" * 22,"-" * 22,"-" * 17)
		print(" %-20s | %-20s | %-20s"%(data_f,receitas[data_f][0],"R$ " + str(receitas[data_f][1])))
		print("-" * 63)
		print()
		print()
		
		decisao = input("Deseja alterar todos os valores da receita (S/N) ? ")
		print()

		if decisao.upper() == "S":
			print(" ATENÇÃO: -----------------------------")
			print("|                                     |")
			print("| Não insira vírgulas no campo valor, |")
			print("| apenas insira um ponto antes dos    |")
			print("| centavos.                           |")
			print("|                                     |")
			print("---------------------------------------\n")

			descricao = input("Informe a nova descrição da receita : ")
			descricao = descricao.upper()
			valor = float(input("Informe o novo valor da receita     : "))
			print()

			receitas[data_f] = [descricao, valor]
			print("Receita financeira alterada.\n")

		elif decisao.upper() == "N":
			print("a) Digite 'a' para alterar a descrição.")
			print("b) Digite 'b' para alterar o valor.\n")

			opcao = input("Informe sua opção: ")
			print()

			if opcao.lower() == "a":
				descricao = input("Informe a nova descrição da receita : ")
				descricao = descricao.upper()

				receitas[data_f][0] = descricao
				print("\nA descrição da receita foi alterada.\n")

			elif opcao.lower() == "b":
				print(" ATENÇÃO: -----------------------------")
				print("|                                     |")
				print("| Não insira vírgulas no campo valor, |")
				print("| apenas insira um ponto antes dos    |")
				print("| centavos.                           |")
				print("|                                     |")
				print("---------------------------------------\n")

				valor = float(input("Informe o novo valor da receita : "))
				print()

				receitas[data_f][1] = valor
				print("O valor da receita foi alterado.\n")

			else:
				print("\nVocê informou um valor inválido para esta operação.\n")

		else:
			print("\nVocê informou um valor inválido para esta operação.\n")

	else:
		print("\nNão há registro de receitas com a data informada.\n")  

def listarReceitas():
	print("\nMódulo - Listar Receitas\n")
	print("a) Digite 'a' para listar todas as receitas.")
	print("b) Digite 'b' para listar as receitas por dia.")
	print("c) Digite 'c' para listar as receitas por mês.")
	print("d) Digite 'd' para listar as receitas por ano.\n")

	opcao = input("Informe sua opção: ")
	print()

	if opcao.lower() == "a":
		if len(receitas) > 0:

			print()
			print(" " * 21 , "MINHAS RECEITAS:")
			print("-" * 61)
			print("%-20s | %-20s | %-20s"%("DATA:","DESCRIÇÃO:","VALOR:"))
			print('-' * 21, '-' * 22, '-' * 16)

			for key,value in receitas.items():
				print("%-20s | %-20s | %-20s"%(key,receitas[key][0],"R$ " + str(receitas[key][1])))

			print("-" * 61)
			print()
			print()

		else:
			print("\nNão há cadastro de receitas financeiras.\n")
	
	elif opcao.lower() == "b":
		dia = input("Informe o dia de cadastro da receita: ")
		mes = input("Informe o mês de cadastro da receita: ")
		ano = input("Informe o ano de cadastro da receita: ")
		data = dia + "/" + mes + "/" + ano
		achou = False
		totalReceitas = 0

		if len(receitas) > 0:

			print()
			print()
			print(" " * 21, "MINHAS RECEITAS:")
			print("-" * 61)
			print("%-20s | %-20s | %-20s"%("DATA:","DESCRIÇÃO:","VALOR:"))
			print('-' * 21, '-' * 22, '-' * 16)

			for key,value in receitas.items():
				if data == key[0:10]:
					print("%-20s | %-20s | %-20s"%(key,receitas[key][0],"R$ " + str(receitas[key][1])))
					totalReceitas += float(receitas[key][1])
					achou = True

			print("-" * 61)
			
			mes1 = nomeMes(mes)

			if achou == False:
				print("\nNão há registro de receitas para o dia %s.\n"%(data))

			else:
				print("\nPERÍODO: %s de %s de %s."%(dia,mes1,ano))
				print("TOTAL RECEITAS DIÁRIAS: R$ %.2f\n\n"%totalReceitas)

		else:
			print("\nNão há cadastro de receitas financeiras.\n")
	
	elif opcao.lower() == "c":
		mes = input("Informe o mês de cadastro da receita: ")
		ano = input("Informe o ano de cadastro da receita: ")
		data = mes + "/" + ano
		achou = False
		totalReceitas = 0

		if len(receitas) > 0:

			print()
			print()
			print(" " * 21, "MINHAS RECEITAS:")
			print("-" * 61)
			print("%-20s | %-20s | %-20s"%("DATA:","DESCRIÇÃO:","VALOR:"))
			print('-' * 21, '-' * 22, '-' * 16)

			for key,value in receitas.items():
				if data == key[3:10]:
					print("%-20s | %-20s | %-20s"%(key,receitas[key][0],"R$ " + str(receitas[key][1])))
					totalReceitas += float(receitas[key][1])
					achou = True

			print("-" * 61)
			mes1 = nomeMes(mes)
			
			if achou == False:
				print("\nNão há registro de receitas para o mês de %s de %s.\n"%(mes1,ano))

			else:
				print("\nPERÍODO: %s de %s."%(mes1,ano))
				print("TOTAL RECEITAS MENSAIS: R$ %.2f\n\n"%totalReceitas)

		else:
			print("\nNão há cadastro de receitas financeiras.\n")
	
	elif opcao.lower() == "d":
		ano = input("Informe o ano de cadastro da receita: ")
		data = ano
		achou = False
		totalReceitas = 0

		if len(receitas) > 0:

			print()
			print()
			print(" " * 21, "MINHAS RECEITAS:")
			print("-" * 61)
			print("%-20s | %-20s | %-20s"%("DATA:","DESCRIÇÃO:","VALOR:"))
			print('-' * 21, '-' * 22, '-' * 16)

			for key,value in receitas.items():
				if data == key[6:10]:
					print("%-20s | %-20s | %-20s"%(key,receitas[key][0],"R$ " + str(receitas[key][1])))
					totalReceitas += float(receitas[key][1])
					achou = True
			
			print("-" * 61)

			if achou == False:
				print("\nNão há registro de receitas para o ano de %s.\n"%ano)
			
			else:
				print("\nPERÍODO: Ano de %s."%ano)
				print("TOTAL RECEITAS ANUAIS: R$ %.2f\n\n"%totalReceitas)

		else:
			print("\nNão há cadastro de receitas financeiras.\n")
	
	else:
		print("Você informou um valor inválido para esta operação.\n")

#Funcoes das despesas _______________________________________________________________________

def adicionarDespesa():
	data_f = gerarData()

	print("\nMódulo - Adicionar Despesa\n")
	print(" ATENÇÃO: ----------------------")
	print("|                              |")
	print("| Não insira vírgulas no campo |")
	print("| valor, apenas adicione um    |")
	print("| ponto antes dos centavos.    |")
	print("|                              |")
	print("| Informe uma das opções a     |")
	print("| seguir no campo categoria:   |")
	print("|                              |")
	print("|  - Habitação                 |")
	print("|  - Alimentação               |")
	print("|  - Saúde                     |")
	print("|  - Pessoal                   |")
	print("|  - Transporte                |")
	print("|  - Lazer                     |")
	print("|                              |")
	print("--------------------------------\n")

	categoria = input("Informe a categoria da despesa : ")
	categoria = categoria.upper()

	if (categoria == "HABITAÇÃO") or (categoria == "ALIMENTAÇÃO") or (categoria == "SAÚDE") or (categoria == "PESSOAL") or (categoria == "TRANSPORTE") or (categoria == "LAZER"):

		descricao = input("Informe a descrição da despesa : ")
		descricao = descricao.upper()
		valor = float(input("Informe o valor da despesa     : "))
		situacao = input("A despesa esta paga (S/N)      ? ")

		if situacao.upper() == "S":
			despesas[data_f] = [categoria,descricao,valor,True]
			print("\nDespesa Financeira adicionada.")
			print("Horário de cadastro: %s\n"%data_f)

		elif situacao.upper() == "N":
			despesas[data_f] = [categoria,descricao,valor,False]
			print("\nDespesa Financeira adicionada.")
			print("Horário de cadastro: %s\n"%data_f)
		
		else:
			print("\nVocê informou um valor inválido para esta operação.\n")

	else:
		print("\nVocê informou uma opção de categoria inválida.\n")

def buscarDespesa():
	print("\nMódulo - Buscar Despesa\n")
	print("a) Digite 'a' para buscar pela data.")
	print("b) Digite 'b' para buscar pela descrição.\n")

	busca = input("Informe o tipo de busca: ")

	if busca.lower() == "a":
		print("\nModulo - Buscar pela data\n")
		print(" ATENÇÃO: ---------------------------------")
		print("|                                         |")
		print("| Caso não saiba a data completa, informe |")
		print("| pelo menos uma parte dela.              |")
		print("|                                         |")
		print("| Formato da data: dd/mm/aaaa HH:MM:SS.   |")
		print("|                                         |")
		print("-------------------------------------------\n")
		data_f = input("Informe a data de cadastro da despesa: ")
		achou = False
		print()
		print()

		print("-" * 96)
		print("%-20s | %-15s | %-20s | %-15s | %-15s"%("DATA:","CATEGORIA:","DESCRIÇÃO:","VALOR:","SITUAÇÃO:"))
		print("-" * 21,"-" * 17,"-" * 22, "-" * 17, "-" * 15)

		for key,value in despesas.items():
			if data_f in key:
				if despesas[key][3] == True:
					print("%-20s | %-15s | %-20s | %-15s | %-15s"%(key,despesas[key][0],despesas[key][1],"R$ " + str(despesas[key][2]),"Paga"))	
					achou = True
				elif despesas[key][3] == False:
					print("%-20s | %-15s | %-20s | %-15s | %-15s"%(key,despesas[key][0],despesas[key][1],"R$ " + str(despesas[key][2]),"Em aberto"))	
					achou = True

		print("-" * 96)

		if achou == False:
			print("\nNão há registro de despesas com a data informada.")
			
		print()
		print()
	
	elif busca.lower() == "b":
		print("\nMódulo - Buscar pela descrição\n")
		print(" ATENÇÃO: ---------------------------------")
		print("|                                         |")
		print("| Caso não saiba a descrição completa,    |")
		print("| pelo menos o início dela.               |")
		print("|                                         |")
		print("-------------------------------------------\n")
		descricao = input("Informe à descrição da despesa à buscar: ")
		descricao = descricao.upper()
		achou = False
		print()
		print()

		print("-" * 96)
		print("%-20s | %-15s | %-20s | %-15s | %-15s"%("DATA:","CATEGORIA:","DESCRIÇÃO:","VALOR:","SITUAÇÃO:"))
		print("-" * 21,"-" * 17,"-" * 22, "-" * 17, "-" * 15)

		for key, value in despesas.items():
			if despesas[key][1].startswith(descricao):
				if despesas[key][3] == True:
					print("%-20s | %-15s | %-20s | %-15s | %-15s"%(key,despesas[key][0],despesas[key][1],"R$" + str(despesas[key][2]),"Paga"))	
					achou = True

				elif despesas[key][3] == False:
					print("%-20s | %-15s | %-20s | %-15s | %-15s"%(key,despesas[key][0],despesas[key][1],"R$" + str(despesas[key][2]),"Em aberto"))	
					achou = True

		print("-" * 96)

		if achou == False:
			print("\nNão há registro de despesas com a descrição informada.\n")
		
		print()
		print()
	
	else:
		print("\nVocê informou um valor inválido para esta operação.\n")

def excluirDespesa():
	print("\nMódulo - Excluir Despesa\n")
	print(" ATENÇÃO: -------------------------------")
	print("|                                       |")
	print("| Para excluir uma despesa você deve    |")
	print("| informar a data completa de cadastro  |")
	print("| da despesa.                           |")
	print("|                                       |")
	print("| Formato da data: dd/mm/aaaa HH:MM:SS. |")
	print("|                                       |")
	print("-----------------------------------------\n")
	data_f = input("Informe a data de cadastro da despesa: ")
	print()
	print()
	
	if data_f in despesas:

		if despesas[data_f][3] == True:
			print("DESPESA FINANCEIRA LOCALIZADA!")
			print("-" * 96)
			print("%-20s | %-15s | %-20s | %-15s | %-15s"%("DATA:","CATEGORIA:","DESCRIÇÃO:","VALOR:","SITUAÇÃO:"))
			print("-" * 21,"-" * 17,"-" * 22, "-" * 17, "-" * 15)
			print("%-20s | %-15s | %-20s | %-15s | %-15s"%(data_f,despesas[data_f][0],despesas[data_f][1],"R$" + str(despesas[data_f][2]),"Paga"))	
			print("-" * 96)
			print()
			print()

		elif despesas[data_f][3] == False:
			print("DESPESA FINANCEIRA LOCALIZADA!")
			print("-" * 96)
			print("%-20s | %-15s | %-20s | %-15s | %-15s"%("DATA:","CATEGORIA:","DESCRIÇÃO:","VALOR:","SITUAÇÃO:"))
			print("-" * 21,"-" * 17,"-" * 22, "-" * 17, "-" * 15)
			print("%-20s | %-15s | %-20s | %-15s | %-15s"%(data_f,despesas[data_f][0],despesas[data_f][1],"R$ " + str(despesas[data_f][2]),"Em aberto"))	
			print("-" * 96)
			print()
			print()

		confirma = input("Confirma a exclusão desta despesa (S/N) ? ")

		if confirma.upper() == "S":
			del despesas[data_f]
			print("\nDespesa Financeira excluída.\n")

		elif confirma.upper() == "N":
			print("\nOperação cancelada.\n")

		else:
			print("\nVocê informou um valor inválido para esta operação.\n")

	else:
		print("Não há registro de despesas com a data informada.\n")

def editarDespesa():
	print("\nMódulo - Editar Despesa Financeira\n")
	print(" ATENÇÃO: -------------------------------")
	print("|                                       |")
	print("| Para editar uma despesa você deve     |")
	print("| informar a data completa de cadastro  |")
	print("| da despesa.                           |")
	print("|                                       |")
	print("| Formato da data: dd/mm/aaaa HH:MM:SS. |")
	print("|                                       |")
	print("-----------------------------------------\n")
	data_f = input("Informe a data completa de cadastro da despesa: ")
	print()
	print()
	
	if data_f in despesas:

		if despesas[data_f][3] == True:
			print("DESPESA FINANCEIRA LOCALIZADA!")
			print("-" * 96)
			print("%-20s | %-15s | %-20s | %-15s | %-15s"%("DATA:","CATEGORIA:","DESCRIÇÃO:","VALOR:","SITUAÇÃO:"))
			print("-" * 21,"-" * 17,"-" * 22, "-" * 17, "-" * 15)
			print("%-20s | %-15s | %-20s | %-15s | %-15s"%(data_f,despesas[data_f][0],despesas[data_f][1],"R$ " + str(despesas[data_f][2]),"Paga"))	
			print("-" * 96)
			print()
			print()

		elif despesas[data_f][3] == False:
			print("DESPESA FINANCEIRA LOCALIZADA!")
			print("-" * 96)
			print("%-20s | %-15s | %-20s | %-15s | %-15s"%("DATA:","CATEGORIA:","DESCRIÇÃO:","VALOR:","SITUAÇÃO:"))
			print("-" * 21,"-" * 17,"-" * 22, "-" * 17, "-" * 15)
			print("%-20s | %-15s | %-20s | %-15s | %-15s"%(data_f,despesas[data_f][0],despesas[data_f][1],"R$ " + str(despesas[data_f][2]),"Em aberto"))	
			print("-" * 96)
			print()
			print()
		
		decisao = input("Deseja alterar todos os valores da despesa (S/N) ? ")
		print()

		if decisao.upper() == "S":
			print(" ATENÇÃO: ----------------------")
			print("|                              |")
			print("| Lembre-se: informe uma das   |")
			print("| opções a seguir no campo     |")
			print("| categoria.                   |")
			print("|                              |")
			print("|  - Habitação                 |")
			print("|  - Alimentação               |")
			print("|  - Saúde                     |")
			print("|  - Pessoal                   |")
			print("|  - Transporte                |")
			print("|  - Lazer                     |")
			print("|                              |")
			print("--------------------------------\n")

			categoria = input("Informe a nova categoria da despesa: ")
			categoria = categoria.upper()

			if (categoria == "HABITAÇÃO") or (categoria == "ALIMENTAÇÃO") or (categoria == "SAÚDE") or (categoria == "PESSOAL") or (categoria == "TRANSPORTE") or (categoria == "LAZER"):

				descricao = input("Informe a nova descrição da despesa: ")
				descricao = descricao.upper()
				valor = float(input("Informe o novo valor da despesa    : "))
				situacao = input("A despesa esta paga (S/N)          ? ") 

				if situacao.upper() == "S":
					despesas[data_f] = [categoria,descricao,valor,True]
					print("\nDespesa Financeira alterada.\n")
					
				elif situacao.upper() == "N":		
					despesas[data_f] = [categoria,descricao,valor,False]
					print("\nDespesa Financeira alterada com sucesso.\n")
					
				else:
					print("\nVocê informou um valor inválido para está operação.\n")
		
			else:
				print("\nVocê informou uma opção de categoria inválida.\n")

		elif decisao.upper() == "N":
			print("a) Digite 'a' para alterar a categoria.")
			print("b) Digite 'b' para alterar a descrição.")
			print("c) Digite 'c' para alterar o valor.")
			print("d) Digite 'd' para alterar a situação.\n")

			opcao = input("Informe sua opção: ")
			print()

			if opcao.lower() == "a":
				print(" ATENÇÃO: ----------------------")
				print("|                              |")
				print("| Lembre-se: informe uma das   |")
				print("| opções a seguir no campo     |")
				print("| categoria.                   |")
				print("|                              |")
				print("|  - Habitação                 |")
				print("|  - Alimentação               |")
				print("|  - Saúde                     |")
				print("|  - Pessoal                   |")
				print("|  - Transporte                |")
				print("|  - Lazer                     |")
				print("|                              |")
				print("--------------------------------\n")

				categoria = input("Informe a nova categoria da despesa: ")
				categoria = categoria.upper()

				despesas[data_f][0] = categoria
				print("\nA categoria da despesa foi alterada.\n")
			
			elif opcao.lower() == "b":
				descricao = input("Informe a nova descrição da despesa: ")
				descricao = descricao.upper()

				despesas[data_f][1] = descricao
				print("\nA descrição da despesa foi alterada.\n")

			elif opcao.lower() == "c":
				print(" ATENÇÃO: -----------------------------")
				print("|                                     |")
				print("| Não insira vírgulas no campo valor, |")
				print("| apenas insira um ponto antes dos    |")
				print("| centavos.                           |")
				print("|                                     |")
				print("---------------------------------------\n")
				valor = input("Informe o novo valor da despesa: ")

				despesas[data_f][2] = valor
				print("\nO valor da despesa foi alterado.\n")

			elif opcao.lower() == "d":
				if despesas[data_f][3] == True:
					despesas[data_f][3] = False
					print("\nA situação da despesa foi alterada.\n")
				else:
					despesas[data_f][3] =  True
					print("A situação da despesa foi alterada.\n")
			
			else:
				print("Você informou um valor inválido para esta operação.\n")
				
		else:
			print("\nVocê informou um valor inválido para esta operação.\n")

	else:
		print("Não há registro de despesas com a data informada.\n")

def listarDespesas():

	print("\nMódulo - Listar Despesas\n")
	print("a) Digite 'a' para listar todas as despesas.")
	print("b) Digite 'b' para listar as despesas por dia.")
	print("c) Digite 'c' para listar as despesas por mês.")
	print("d) Digite 'd' para listar as despesas por ano.")
	print("e) Digite 'e' para listar as despesas por categoria.\n")
	opcao = input("Informe sua opção: ")
	print()

	if opcao.lower() == "a":
		if len(despesas) > 0:
			
			print()
			print(" " * 39 ,"MINHAS DESPESAS:")
			print("-" * 96)
			print("%-20s | %-15s | %-20s | %-15s | %-15s"%("DATA:","CATEGORIA:","DESCRIÇÃO:","VALOR:","SITUAÇÃO:"))
			print("-" * 21,"-" * 17,"-" * 22, "-" * 17, "-" * 15)

			for key,value in despesas.items():
				if despesas[key][3] == True:
					print("%-20s | %-15s | %-20s | %-15s | %-15s"%(key,despesas[key][0],despesas[key][1],"R$ " + str(despesas[key][2]),"Paga"))	

				elif despesas[key][3] == False:
					print("%-20s | %-15s | %-20s | %-15s | %-15s"%(key,despesas[key][0],despesas[key][1],"R$ " + str(despesas[key][2]),"Em aberto"))

			print("-" * 96)
			print()
			print()

		else:
			print("\nNão há cadastro de despesas financeiras.\n")
	
	elif opcao.lower() == "b":
		if len(despesas) > 0:
			dia = input("Informe o dia de cadastro da despesa: ")
			mes = input("Informe o mês de cadastro da despesa: ")
			ano = input("Informe o ano de cadastro da despesa: ")
			data = dia + "/" + mes + "/" + ano
			achou = False
			totalDespesas = 0

			print()
			print(" " * 39, "MINHAS DESPESAS:")
			print("-" * 96)
			print("%-20s | %-15s | %-20s | %-15s | %-15s"%("DATA:","CATEGORIA:","DESCRIÇÃO:","VALOR:","SITUAÇÃO:"))
			print("-" * 21,"-" * 17,"-" * 22, "-" * 17, "-" * 15)

			for key,value in despesas.items():
				if data == key[0:10]:
					if despesas[key][3] == True:
						print("%-20s | %-15s | %-20s | %-15s | %-15s"%(key,despesas[key][0],despesas[key][1],"R$ " + str(despesas[key][2]),"Paga"))	
						totalDespesas += float(despesas[key][2])
						achou = True

					elif despesas[key][3] == False:
						print("%-20s | %-15s | %-20s | %-15s | %-15s"%(key,despesas[key][0],despesas[key][1],"R$ " + str(despesas[key][2]),"Em aberto"))	
						totalDespesas += float(despesas[key][2])
						achou = True

			print("-" * 96)

			mes1 = nomeMes(mes)

			if achou == False:
				print("\nNão há registro de despesas para o dia %s.\n"%data)
			
			else:
				print("\nPERÍODO: %s de %s de %s."%(dia,mes1,ano))
				print("TOTAL DESPESAS DIÁRIAS: R$ %.2f\n\n"%totalDespesas)

		else:
			print("\nNão há cadastro de despesas financeiras.\n")

	elif opcao.lower() == "c":
		if len(despesas) > 0:
			mes = input("Informe o mês de cadastro da despesa: ")
			ano = input("Informe o ano de cadastro da despesa: ")
			data = mes + "/" + ano
			achou = False
			totalDespesas = 0

			print()
			print(" " * 39, "MINHAS DESPESAS:")
			print("-" * 96)
			print("%-20s | %-15s | %-20s | %-15s | %-15s"%("DATA:","CATEGORIA:","DESCRIÇÃO:","VALOR:","SITUAÇÃO:"))
			print("-" * 21,"-" * 17,"-" * 22, "-" * 17, "-" * 15)

			for key,value in despesas.items():
				if data == key[3:10]:
					if despesas[key][3] == True:
						print("%-20s | %-15s | %-20s | %-15s | %-15s"%(key,despesas[key][0],despesas[key][1],"R$ " + str(despesas[key][2]),"Paga"))	
						totalDespesas += float(despesas[key][2])
						achou = True

					elif despesas[key][3] == False:
						print("%-20s | %-15s | %-20s | %-15s | %-15s"%(key,despesas[key][0],despesas[key][1],"R$ " + str(despesas[key][2]),"Em aberto"))	
						totalDespesas += float(despesas[key][2])
						achou = True

			print("-" * 96)
			
			mes1 = nomeMes(mes)

			if achou == False:
				print("\nNão há registro de despesas para o mês de %s de %s.\n"%(mes1,ano))
			
			else:
				print("\nPERÍODO: %s de %s."%(mes1,ano))
				print("TOTAL DESPESAS MENSAIS: R$ %.2f\n\n"%totalDespesas)

		else:
			print("\nNão há cadastro de despesas financeiras.\n")

	elif opcao.lower() == "d":
		if len(despesas) > 0:
			ano = input("Informe o ano de cadastro da despesa: ")
			data = ano
			achou = False
			totalDespesas = 0

			print()
			print(" " * 39, "MINHAS DESPESAS:")
			print("-" * 96)
			print("%-20s | %-15s | %-20s | %-15s | %-15s"%("DATA:","CATEGORIA:","DESCRIÇÃO:","VALOR:","SITUAÇÃO:"))
			print("-" * 21,"-" * 17,"-" * 22, "-" * 17, "-" * 15)

			for key,value in despesas.items():
				if data == key[6:10]:
					if despesas[key][3] == True:
						print("%-20s | %-15s | %-20s | %-15s | %-15s"%(key,despesas[key][0],despesas[key][1],"R$ " + str(despesas[key][2]),"Paga"))	
						totalDespesas += float(despesas[key][2])
						achou = True

					elif despesas[key][3] == False:
						print("%-20s | %-15s | %-20s | %-15s | %-15s"%(key,despesas[key][0],despesas[key][1],"R$ " + str(despesas[key][2]),"Em aberto"))
						totalDespesas += float(despesas[key][2])
						achou = True

			print("-" * 96)
			
			if achou == False:
				print("\nNão há registro de despesas para o ano de %s.\n"%ano)

			else:
				print("\nPERÍODO: Ano de %s"%ano)
				print("TOTAL DESPESAS ANUAIS: R$ %.2f\n\n"%totalDespesas)

		else:
			print("\nNão há cadastro de despesas financeiras.\n")
	
	elif opcao.lower() == "e":

		if len(despesas) > 0:
			print(" ATENÇÃO: ----------------------")
			print("|                              |")
			print("| Lembre-se: informe uma das   |")
			print("| opções a seguir no campo     |")
			print("| categoria.                   |")
			print("|                              |")
			print("|  - Habitação                 |")
			print("|  - Alimentação               |")
			print("|  - Saúde                     |")
			print("|  - Pessoal                   |")
			print("|  - Transporte                |")
			print("|  - Lazer                     |")
			print("|                              |")
			print("--------------------------------\n")
			categoria = input("Informe a categoria da despesa : ")
			categoria = categoria.upper()

			if (categoria == "HABITAÇÃO") or (categoria == "ALIMENTAÇÃO") or (categoria == "SAÚDE") or (categoria == "PESSOAL") or (categoria == "TRANSPORTE") or (categoria == "LAZER"):

				mes = input("Informe o mês de cadastro da despesa : ")
				ano = input("Informe o ano de cadastro da despesa : ")
				data = mes + "/" + ano
				achou = False
				totalDespesas = 0

				print()
				print(" " * 39, "MINHAS DESPESAS:")
				print("-" * 96)
				print("%-20s | %-15s | %-20s | %-15s | %-15s"%("DATA:","CATEGORIA:","DESCRIÇÃO:","VALOR:","SITUAÇÃO:"))
				print("-" * 21,"-" * 17,"-" * 22, "-" * 17, "-" * 15)

				for key,value in despesas.items():
					if (data == key[3:10]) and (despesas[key][0] == categoria):
						if despesas[key][3] == True:
							print("%-20s | %-15s | %-20s | %-15s | %-15s"%(key,despesas[key][0],despesas[key][1],"R$ " + str(despesas[key][2]),"Paga"))	
							totalDespesas += float(despesas[key][2])
							achou = True

						elif despesas[key][3] == False:
							print("%-20s | %-15s | %-20s | %-15s | %-15s"%(key,despesas[key][0],despesas[key][1],"R$ " + str(despesas[key][2]),"Em aberto"))	
							totalDespesas += float(despesas[key][2])
							achou = True

				print("-" * 96)
				
				mes1 = nomeMes(mes)

				if achou == False:
					print("\nNão há registro de despesas de %s para o mês de %s.\n"%(categoria,mes1))
				
				else:
					print("\nPERÍODO: %s de %s"%(mes1,ano))
					print("TOTAL GASTO COM %s: R$ %.2f\n\n"%(categoria,totalDespesas))

			else:
				print("\nVocê informou uma opção de categoria inválida.\n")

		else:
			print("\nNão há cadastro de despesas financeiras.\n")
	
def pagarDespesa():
	print("\nMódulo - Pagar Despesa\n")
	print(" ATENÇÃO: -------------------------------")
	print("|                                       |")
	print("| Para pagar uma despesa você deve      |")
	print("| informar a data completa de cadastro  |")
	print("| da despesa.                           |")
	print("|                                       |")
	print("| Formato da data: dd/mm/aaaa HH:MM:SS. |")
	print("|                                       |")
	print("-----------------------------------------\n")
	data_f = input("Informe a data de cadastro da despesa: ")
	print()
	
	if data_f in despesas:

		if despesas[data_f][3] == True:
			print("DESPESA FINANCEIRA LOCALIZADA!")
			print("-" * 96)
			print("%-20s | %-15s | %-20s | %-15s | %-15s"%("DATA:","CATEGORIA:","DESCRIÇÃO:","VALOR:","SITUAÇÃO:"))
			print("-" * 21,"-" * 17,"-" * 22, "-" * 17, "-" * 15)
			print("%-20s | %-15s | %-20s | %-15s | %-15s"%(data_f,despesas[data_f][0],despesas[data_f][1],"R$" + str(despesas[data_f][2]),"Paga"))	
			print("-" * 96)
			print()
			print("Esta despesa já esta paga.")
			print()

		elif despesas[data_f][3] == False:
			print("DESPESA FINANCEIRA LOCALIZADA!")
			print("-" * 96)
			print("%-20s | %-15s | %-20s | %-15s | %-15s"%("DATA:","CATEGORIA:","DESCRIÇÃO:","VALOR:","SITUAÇÃO:"))
			print("-" * 21,"-" * 17,"-" * 22, "-" * 17, "-" * 15)
			print("%-20s | %-15s | %-20s | %-15s | %-15s"%(data_f,despesas[data_f][0],despesas[data_f][1],"R$ " + str(despesas[data_f][2]),"Em aberto"))	
			print("-" * 96)
			print()
			print()
			
			numeroConta = input("Informe o número da conta bancária: ")
			
			if numeroConta in contas:
				valor = float(despesas[data_f][2])
				saldo = float(contas[numeroConta][3])

				if saldo >= valor:
					data_b = gerarData()

					confirma = input("Confirma o pagamento desta conta (S/N) ? ")

					if confirma.upper() == "S":
						contas[numeroConta][3] -= valor
						despesas[data_f][3] = True
						nome = despesas[data_f][1]
						pagamentos[data_b] = [numeroConta,nome,valor]
						print("\nOperação realizada com sucesso.\n")
					
					elif confirma.upper() == "N":
						print("\nOperação cancelada.\n")

					else:
						print("\nVocê informou uma opção inválida para esta operação.\n")

				else:
					print("\nSALDO INSUFICIENTE.\n")

			else:
				print("\nA conta bancária informada não existe em nossa base de dados.\n")

	else:
		print("\nNão há registro de despesas com a data informada.\n")

#Relatórios ______________________________________________________________________

def relatorioMensal():
	print("\nMódulo - Relatório Mensal\n")
	print(" ATENÇÃO: -----------------------------")
	print("|                                     |")
	print("| Para visualizar o relatório mensal, |")
	print("| informe o MÊS e ANO de cadastro das |")
	print("| receitas e despesas.                |")
	print("|                                     |")
	print("| Não informe o nome do mês, informe  |")
	print("| o número referente à ele, por exem- |")
	print("| plo, caso o mês seja Janeiro, digi- |")
	print("| te 01.                              |")
	print("|                                     |")
	print("| O relatório realiza os cálculos le- |")
	print("| vando em conta as despesas que es-  |")
	print("| tão pagas.                          |")
	print("|                                     |")
	print("---------------------------------------\n")

	mes = input("Informe o mês que deseja ver o relatório: ")
	ano = input("Informe o ano que deseja ver o relatório: ")
	data = mes + "/" + ano

	mes1 = nomeMes(mes)

	totalReceitas = 0
	totalDespesas = 0
	saldoTotal = 0
	contR = 0
	contD = 0
	
	if (len(receitas) > 0) and (len(despesas) > 0):

		print("\n"," " * 15,"RELATÓRIO: %s DE %s\n"%(mes1,ano))
		print("MINHAS RECEITAS:")
		print("-" * 61)
		print("%-20s | %-20s | %-20s"%("DATA:","DESCRIÇÃO:","VALOR:"))
		print('-' * 21, '-' * 22, '-' * 16)

		arq = open('relatorio.txt','w')
		arq.write(" ")
		arq.close()

		arq = open('relatorio.txt','a')
		arq.write(" " * 15 + "RELATÓRIO: %s DE %s\n"%(mes1,ano) + "\n")
		arq.write("MINHAS RECEITAS:" + "\n")
		arq.write("-" * 61 + "\n")
		arq.write("%-20s | %-20s | %-20s"%("DATA:","DESCRIÇÃO:","VALOR:") + "\n")
		arq.write('-' * 21 + '-' * 22 + '-' * 18 + "\n")
		arq.close()

		for key,value in receitas.items():
			if key[3:10] == data:
				print("%-20s | %-20s | %-20s"%(key,receitas[key][0],"R$ " + str(receitas[key][1])))

				arq = open('relatorio.txt','a')
				arq.write("%-20s | %-20s | %-20s"%(key,receitas[key][0],"R$ " + str(receitas[key][1])) + "\n")
				arq.close()

				totalReceitas += float(receitas[key][1])
				contR += 1

		print("-" * 61)
		print()

		print("MINHAS DESPESAS:")
		print("-" * 61)
		print("%-20s | %-20s | %-20s"%("DATA:","DESCRIÇÃO:","VALOR:"))
		print('-' * 21 + '-' * 22 + '-' * 18)

		arq = open('relatorio.txt','a')
		arq.write("-" * 61 + "\n\n")
		arq.write("MINHAS DESPESAS:" + "\n")
		arq.write("-" * 61 + "\n")
		arq.write("%-20s | %-20s | %-20s"%("DATA:","DESCRIÇÃO:","VALOR:") + "\n")
		arq.write('-' * 21 + '-' * 22 + '-' * 18 + "\n")
		arq.close()

		for chave,valor in despesas.items():
			if chave[3:10] == data:
				if despesas[chave][3] == False:
					print("%-20s | %-20s | %-20s"%(chave,despesas[chave][1],"R$ " + str(despesas[chave][2])))

					arq = open('relatorio.txt', 'a')
					arq.write("%-20s | %-20s | %-20s"%(chave,despesas[chave][1],"R$ " + str(despesas[chave][2])) + "\n")
					arq.close()

					totalDespesas += float(despesas[chave][2])
					contD += 1

		print("-" * 61)
		print()

		arq = open('relatorio.txt','a')
		arq.write("-" * 61 + "\n\n")
		arq.close()
		
		if (contR == 0) or (contD == 0):
			print("Não há registro de receitas ou de despesas para o mês de %s de %s.\n"%(mes1,ano))

			arq = open('relatorio.txt','a')
			arq.write("Não há registro de receitas ou de despesas para o mês de %s de %s.\n"%(mes1,ano) + "\n\n")
			arq.close()

		else:
			saldoTotal = totalReceitas - totalDespesas
			print("RECEITAS : R$ %.2f"%totalReceitas)
			print("DESPESAS : R$ %.2f"%totalDespesas)
			print("SALDO    : R$ %.2f\n\n"%saldoTotal)

			arq = open('relatorio.txt','a')
			arq.write("RECEITAS : R$ %.2f"%totalReceitas + "\n")
			arq.write("DESPESAS : R$ %.2f"%totalDespesas + "\n")
			arq.write("SALDO    : R$ %.2f\n\n"%saldoTotal + "\n")
			arq.close()
		
		print()  

		confirma = input("Deseja receber o relatório por e-mail (S/N) ? ")
		print()

		if confirma.upper() == "S":

			try:
				email = input("Informe seu e-mail: ")
				email_from = "pyfinanc@gmail.com"
				email_to = email

				smtp = "smtp.gmail.com"

				server = smtplib.SMTP(smtp, 587)
				server.starttls()
				server.login(email_from, open('senha.txt').read().strip())

				message = "Olá, somos da equipe do PyFinance. Anexamos o seu RELATÓRIO MENSAL logo abaixo. Qualquer dúvida entre em contato conosco através deste e-mail.\n"
				msg = MIMEMultipart()
				msg['Subject'] = 'RELATÓRIO MENSAL'
				msg.attach(MIMEText(message, 'plain'))

				filename = 'relatorio.txt'
				attachment = open('relatorio.txt', 'rb')

				part = MIMEBase('application','octet-stream')
				part.set_payload((attachment).read())
				encoders.encode_base64(part)
				part.add_header('Content-Disposition', "attachment; filename = %s" %filename)

				msg.attach(part)
				attachment.close()

				server.sendmail(email_from, email_to, msg.as_string())
				server.quit()

				print("\nE-mail enviado com sucesso.\n")
			
			except:
				print("\nErro ao enviar e-mail.")

		
		elif confirma.upper() == "N":
			print("Tudo bem! Talvez da próxima.\n")
		
		else:
			print("Você informou um valor inválido para esta operação.\n")

	else:
		print("\nNão há registro de receitas ou despesas financeiras.\n")

def relatorioAnual():
	print("\nMódulo - Relatório Anual\n")
	print(" ATENÇÃO: -----------------------------")
	print("|                                      |")
	print("| Para visualizar o relatório anual,   |")
	print("| informe o ANO de cadastro das recei- |")
	print("| ceitas e despesas.                   |")
	print("|                                      |")
	print("| O relatório realiza os cálculos le- |")
	print("| vando em conta as despesas que es-  |")
	print("| tão pagas.                          |")
	print("|                                     |")
	print("---------------------------------------\n")

	ano = input("Informe o ano que deseja ver o relatório: ")

	totalReceitas = 0
	totalDespesas = 0
	saldoTotal = 0
	contR = 0
	contD = 0
	
	if (len(receitas) > 0) and (len(despesas) > 0):

		print("\n"," " * 15,"RELATÓRIO: ANO DE %s\n"%ano)
		print("MINHAS RECEITAS:")
		print("-" * 61)
		print("%-20s | %-20s | %-20s"%("DATA:","DESCRIÇÃO:","VALOR:"))
		print('-' * 21, '-' * 22, '-' * 16)

		arq = open('relatorioAnual.txt', 'w')
		arq.write(" ")
		arq.close()

		arq = open('relatorioAnual.txt', 'a')
		arq.write(" " * 15 + "RELATÓRIO: ANO DE %s\n"%ano + "\n")
		arq.write("MINHAS RECEITAS:" + "\n")
		arq.write("-" * 61 + "\n")
		arq.write("%-20s | %-20s | %-20s"%("DATA:","DESCRIÇÃO:","VALOR:") + "\n")
		arq.write('-' * 21 + '-' * 22 + '-' * 18 + "\n")
		arq.close()

		for key,value in receitas.items():
			if key[6:10] == ano:
				print("%-20s | %-20s | %-20s"%(key,receitas[key][0],"R$ " + str(receitas[key][1])))

				arq = open('relatorioAnual.txt','a')
				arq.write("%-20s | %-20s | %-20s"%(key,receitas[key][0],"R$ " + str(receitas[key][1])) + "\n")
				arq.close()

				totalReceitas += float(receitas[key][1])
				contR += 1

		print("-" * 61)
		print()

		arq = open('relatorioAnual.txt','a')
		arq.write("-" * 61 +"\n\n")
		arq.close()
		
		print("MINHAS DESPESAS:")
		print("-" * 61)
		print("%-20s | %-20s | %-20s"%("DATA:","DESCRIÇÃO:","VALOR:"))
		print('-' * 21, '-' * 22, '-' * 16)

		arq = open('relatorioAnual.txt', 'a')
		arq.write("MINHAS DESPESAS:" + "\n")
		arq.write("-" * 61 + "\n")
		arq.write("%-20s | %-20s | %-20s"%("DATA:","DESCRIÇÃO:","VALOR:") + "\n")
		arq.write('-' * 21 + '-' * 22 + '-' * 18 + "\n")
		arq.close()
			
		for chave,valor in despesas.items():
			if chave[6:10] == ano:
				if despesas[chave][3] == False:
					print("%-20s | %-20s | %-20s"%(chave,despesas[chave][1],"R$ " + str(despesas[chave][2])))

					arq = open('relatorioAnual.txt','a')
					arq.write("%-20s | %-20s | %-20s"%(chave,despesas[chave][1],"R$ " + str(despesas[chave][2])) + "\n")
					arq.close()

					totalDespesas += float(despesas[chave][2])
					contD += 1
		
		print("-" * 61)
		print()
		
		if (contR == 0) or (contD == 0):
			print("Não há registro de receitas ou de despesas para o ano de %s.\n"%ano)

			arq = open('relatorioAnual.txt','a')
			arq.write("Não há registro de receitas ou de despesas para o ano de %s.\n"%ano + "\n")
			arq.close()

		else:
			saldoTotal = totalReceitas - totalDespesas
			print("RECEITAS : R$ %.2f"%totalReceitas)
			print("DESPESAS : R$ %.2f"%totalDespesas)
			print("SALDO    : R$ %.2f\n"%saldoTotal)

			arq = open('relatorioAnual.txt','a')
			arq.write("\nRECEITAS : R$ %.2f"%totalReceitas + "\n")
			arq.write("DESPESAS : R$ %.2f"%totalDespesas + "\n")
			arq.write("SALDO    : R$ %.2f\n"%saldoTotal + "\n")
			arq.close()
		
		print()  

		confirma = input("Deseja receber o relatório por e-mail (S/N) ? ")
		print()

		if confirma.upper() == "S":

			try:
				email = input("Informe seu e-mail: ")
				email_from = "pyfinanc@gmail.com"
				email_to = email

				smtp = "smtp.gmail.com"

				server = smtplib.SMTP(smtp, 587)
				server.starttls()
				server.login(email_from, open('senha.txt').read().strip())

				message = "Olá, somos da equipe do PyFinance. Anexamos o seu RELATÓRIO ANUAL logo abaixo. Qualquer dúvida entre em contato conosco através deste e-mail.\n"
				msg = MIMEMultipart()
				msg['Subject'] = 'RELATÓRIO ANUAL'
				msg.attach(MIMEText(message, 'plain'))

				filename = 'relatorioAnual.txt'
				attachment = open('relatorioAnual.txt', 'rb')

				part = MIMEBase('application','octet-stream')
				part.set_payload((attachment).read())
				encoders.encode_base64(part)
				part.add_header('Content-Disposition', "attachment; filename = %s" %filename)

				msg.attach(part)
				attachment.close()

				server.sendmail(email_from, email_to, msg.as_string())
				server.quit()

				print("\nE-mail enviado com sucesso.\n")
			
			except:
				print("\nErro ao enviar e-mail.")
		
		elif confirma.upper() == "N":
			print("Tudo bem! Talvez da próxima.\n")
		
		else:
			print("Você informou um valor inválido para esta operação.\n")

	else:
		print("\nNão há registro de receitas ou despesas financeiras.\n")

#Contas ____________________________________________________________________

def gerenciarCarteira():
	print("\nMódulo - Gerenciar Carteira\n")
	print(" ATENÇÃO: -------------------------")
	print("|                                 |")
	print("| A carteira é onde você controla |")
	print("| o dinheiro em espécie. Quanto   |")
	print("| você tem no bolso agora ?       |")
	print("|                                 |")
	print("-----------------------------------\n")

	if len(carteira) == 0:
		print("Você ainda não cadastrou quanto você tem na carteira.\n")
		decisao = input("Deseja cadastrar algum valor (S/N) ? ")
		print()

		if decisao.upper() == "S":
			valor = float(input("Informe quanto você tem na carteira: "))
			carteira["carteira"] = valor
			print("\nSaldo da carteira alterado.")
			print("Saldo Carteira: R$ %.2f\n"%valor)

		elif decisao.upper() == "N":
			print("Tudo bem, vamos deixar para outra hora.\n")

		else:
			print("Você informou um valor invalido para esta operaçao.\n")
	
	else:
		print("Saldo Carteira: R$ %.2f\n"%carteira["carteira"])
		decisao = input("Deseja alterar o valor que você tem na carteira (S/N) ? ")
		print()

		if decisao.upper() == "S":
			valor = float(input("Informe quanto você tem na carteira: "))
			carteira["carteira"] = valor
			print("\nSaldo da carteira alterado.")
			print("Saldo Carteira: R$ %.2f\n"%valor)

		elif decisao.upper() == "N":
			print("Tudo bem, vamos deixar para outra hora.\n")

		else:
			print("\nVocê informou um valor invalido para esta operaçao.\n")

def adicionarConta():
	print("\nMódulo - Adicionar Conta Bancária\n")
	numeroConta = input("Informe o número da conta bancária  : ")
	numeroConta = numeroConta.replace("-", "")
	tam = len(numeroConta)
	mutliplicador = 6
	soma = 0

	for i in range(tam-1):
		soma += int(numeroConta[i]) * mutliplicador
		mutliplicador -= 1
	resto = soma % 11
	digito = 11 - resto

	if digito == 10:
		digito = 0
	
	if int(numeroConta[5]) == digito:
		numeroConta = numeroConta[0:5] + "-" + numeroConta[5]
		nomeBanco = input("Informe o nome da Agência bancária  : ")
		nomeBanco = nomeBanco.upper()

		tipoConta = input("Informe o tipo da conta bancária    : ")
		tipoConta = tipoConta.upper()

		nomeTitular = input("Informe o titular da conta bancária : ")
		nomeTitular = nomeTitular.upper()
		
		saldo = float(input("Informe o saldo da conta bancária   : "))
		achou = False

		for key,value in contas.items():
			if numeroConta == key:
				achou = True

		if achou == False:
			contas[numeroConta] = [nomeBanco, tipoConta, nomeTitular, saldo]	
			print("\nConta bancária adicionada.\n")

		else:
			print("\nO número da conta informada já existe em nossa base de dados.\n")

	else:
		print("\nCONTA INVÁLIDA.\n")

def buscarConta():
	print("\nMódulo - Buscar Conta Bancária\n")
	numeroConta = input("Informe o número da conta que você quer buscar: ")
	print()

	if numeroConta in contas:
		print("\n", " " * 41, "CONTA BANCÁRIA LOCALIZADA!")
		print("-" * 115)
		print("%-20s | %-15s | %-15s | %-35s | %-15s"%("NÚMERO DA CONTA:","AGÊNCIA BANCÁRIA:","TIPO DA CONTA:","TITULAR DA CONTA:","SALDO DA CONTA:"))
		print("-" * 21,"-" * 19,"-" * 17, "-" * 37, "-" * 17)
		print("%-20s | %-17s | %-15s | %-35s | R$ %-15s"%(numeroConta,contas[numeroConta][0],contas[numeroConta][1],contas[numeroConta][2],contas[numeroConta][3]))	
		print("-" * 115)
	
	else:
		print("\nO número da conta informado não existe em nossa base de dados.\n")

	print()
	print()

def excluirConta():
	print("\nMódulo - Excluir Conta Bancária\n")
	numeroConta = input("Informe o número da conta que você quer excluir : ")
	print()

	if numeroConta in contas:
		print("\n"," " * 41, "CONTA BANCÁRIA LOCALIZADA!")
		print("-" * 115)
		print("%-20s | %-15s | %-15s | %-35s | %-15s"%("NÚMERO DA CONTA:","AGÊNCIA BANCÁRIA:","TIPO DA CONTA:","TITULAR DA CONTA:","SALDO DA CONTA:"))
		print("-" * 21,"-" * 19,"-" * 17, "-" * 37, "-" * 17)
		print("%-20s | %-17s | %-15s | %-35s | R$ %-15s"%(numeroConta,contas[numeroConta][0],contas[numeroConta][1],contas[numeroConta][2],contas[numeroConta][3]))	
		print("-" * 115)
		print()
		print()
		confirma = input("Confirma a exclusão desta conta bancária (S/N) ? ")

		if confirma.upper() == "S":
			del contas[numeroConta]
			print("\nConta bancária excluída.\n")
		
		elif confirma.upper() == "N":
			print("\nOperação cancelada.\n")
		
		else:
			print("\nVocê informou um valor inválido para esta operação.\n")
	
	else:
		print("\nO número da conta informado não existe em nossa base de dados.\n")

def editarConta():
	print("\nMódulo - Editar Conta Bancária\n")
	numeroConta = input("Informe o número da conta que você quer editar: ")
	print()

	if numeroConta in contas:
		print("\n"," " * 41,"CONTA BANCÁRIA LOCALIZADA!")
		print("-" * 115)
		print("%-20s | %-15s | %-15s | %-35s | %-15s"%("NÚMERO DA CONTA:","AGÊNCIA BANCÁRIA:","TIPO DA CONTA:","TITULAR DA CONTA:","SALDO DA CONTA:"))
		print("-" * 21,"-" * 19,"-" * 17, "-" * 37, "-" * 17)
		print("%-20s | %-17s | %-15s | %-35s | R$ %-15s"%(numeroConta,contas[numeroConta][0],contas[numeroConta][1],contas[numeroConta][2],contas[numeroConta][3]))	
		print("-" * 115)
		print()
		print()
		decisao = input("Alterar todos os campos da conta bancária (S/N) ? ")
		print()

		if decisao.upper() == "S":
			nomeBanco = input("Informe o nome da Agência bancária  : ")
			nomeBanco = nomeBanco.upper()
			tipoConta = input("Informe o tipo da conta bancária    : ")
			tipoConta = tipoConta.upper()
			nomeTitular = input("Informe o titular da conta bancária : ")
			nomeTitular = nomeTitular.upper()
			saldo = float(input("Informe o saldo da conta bancária   : "))
			contas[numeroConta] = [nomeBanco,tipoConta,nomeTitular,saldo]
			print("\nConta bancária alterada.\n")

		elif decisao.upper() == "N":
			print("a) Digite 'a' para alterar o nome da agência")
			print("b) Digite 'b' para alterar o tipo da conta")
			print("c) Digite 'c' para alterar o titular da conta")
			print("d) Digite 'd' para alterar o saldo da conta\n")

			opcao = input("Informe sua opção: ")
			print()				

			if opcao.lower() == "a":
				nomeBanco = input("Informe o nome da Agência bancária: ")
				nomeBanco = nomeBanco.upper()
				contas[numeroConta][0] = nomeBanco
				print("\nNome da agência alterado.\n")

			elif opcao.lower() == "b":
				tipoConta = input("Informe o tipo da conta bancária: ")
				tipoConta = tipoConta.upper()
				contas[numeroConta][1] = tipoConta
				print("\nTipo da Conta alterado.\n")
			
			elif opcao.lower() == "c":
				nomeTitular = input("Informe o titular da conta bancária: ")
				nomeTitular = nomeTitular.upper()
				contas[numeroConta][2] = nomeTitular
				print("\nNome do titular da conta alterado.\n")
			
			elif opcao.lower() == "d":
				saldo = float(input("Informe o saldo da conta bancária: "))
				contas[numeroConta][3] = saldo
				print("\nSaldo da conta bancária alterado.\n")
			
			else:
				print("\nVocê informou um valor inválido para esta operação.\n")
		
		else:
			print("\nVocê informou um valor inválido para esta operação.\n")

	else:
		print("\nO número da conta informada não existem em nossa base de dados.\n")

def listarContas():
	print("\nMódulo - Listar Contas Bancárias\n")

	if len(contas) == 0:
		print("Não há contas bancárias cadastradas.\n")
	
	else:
		print("\n"," "*41,"MINHAS CONTAS BANCÁRIAS:")
		print("-" * 115)
		print("%-20s | %-15s | %-15s | %-35s | %-15s"%("NÚMERO DA CONTA:","AGÊNCIA BANCÁRIA:","TIPO DA CONTA:","TITULAR DA CONTA:","SALDO DA CONTA:"))
		for key,value in contas.items():
			print("-" * 21,"-" * 19,"-" * 17, "-" * 37, "-" * 17)
			print("%-20s | %-17s | %-15s | %-35s | R$ %-15s"%(key,contas[key][0],contas[key][1],contas[key][2],contas[key][3]))	
		print("-" * 115)
		print()
		print()
	
#Funções das operações ____________________________________________________________________

def realizarSaque():
	print("\nMódulo - Realizar Saque\n")
	data_f = gerarData()
	numeroConta = input("Informe o número da conta a realizar o saque: ")
	print()

	if numeroConta in contas:
		print("\n"," " * 41,"CONTA BANCÁRIA LOCALIZADA!")
		print("-" * 115)
		print("%-20s | %-15s | %-15s | %-35s | %-15s"%("NÚMERO DA CONTA:","AGÊNCIA BANCÁRIA:","TIPO DA CONTA:","TITULAR DA CONTA:","SALDO DA CONTA:"))
		print("-" * 21,"-" * 19,"-" * 17, "-" * 37, "-" * 17)
		print("%-20s | %-17s | %-15s | %-35s | R$ %-15s"%(numeroConta,contas[numeroConta][0],contas[numeroConta][1],contas[numeroConta][2],contas[numeroConta][3]))	
		print("-" * 115)

		saldo = contas[numeroConta][3]
		print()
		saque = float(input("Informe o valor do saque: "))
		print()

		if saldo >= saque:
			confirma = input("Confirma a retirada de R$ %.2f (S/N) ? "%saque)
			print()

			if confirma.upper() == "S":
				saques[data_f] = [numeroConta, saque]
				contas[numeroConta][3] -= saque
				print("Operação realizada com sucesso.\n")
				print("Saldo Atual: R$ %.2f\n"%contas[numeroConta][3])

			elif confirma.upper() == "N":
				print("Operação cancelada.\n")
			
			else:
				print("Você informou um valor inválido para esta operação.\n")

		else:
			print("\nSALDO INSUFICIENTE.\n")

	else:
		print("\nO número da conta informada não existe em nossa base de dados.\n")

def realizarDeposito():
	print("\nMódulo - Realizar Depósito\n")
	data_f = gerarData()
	numeroConta = input("Informe o número da conta à realizar o depósito: ")
	print()

	if numeroConta in contas:
		print("\n"," "*41,"CONTA BANCÁRIA LOCALIZADA!")
		print("-" * 115)
		print("%-20s | %-15s | %-15s | %-35s | %-15s"%("NÚMERO DA CONTA:","AGÊNCIA BANCÁRIA:","TIPO DA CONTA:","TITULAR DA CONTA:","SALDO DA CONTA:"))
		print("-" * 21,"-" * 19,"-" * 17, "-" * 37, "-" * 17)
		print("%-20s | %-17s | %-15s | %-35s | R$ %-15s"%(numeroConta,contas[numeroConta][0],contas[numeroConta][1],contas[numeroConta][2],contas[numeroConta][3]))	
		print("-" * 115)
		print()
		deposito = float(input("Informe o valor do depósito: "))
		print()

		confirma = input("Confirma o depósito de R$ %.2f (S/N) ? "%deposito)
		print()

		if confirma.upper() == "S":
			depositos[data_f] = [numeroConta,deposito]
			contas[numeroConta][3] += deposito
			print("Operação realizada com sucesso.\n")

		elif confirma.upper() == "N":
			print("Operação cancelada.\n")
		
		else:
			print("Você informou um valor inválido para esta operação.\n")

	else:
		print("\nO número da conta informada não existe em nossa base de dados.\n")
	
def realizarTransferencia():
	print("\nMódulo - Realizar Transferência\n")
	data_f = gerarData()
	numeroContaOrigem = input("Informe o número da conta de origem: ")
	numeroContaDestino = input("Informe o número da conta destino : ")
	print()

	if numeroContaOrigem and numeroContaDestino in contas:
		print("\n"," " * 41,"CONTA BANCÁRIA DE ORIGEM LOCALIZADA!")
		print("-" * 115)
		print("%-20s | %-15s | %-15s | %-35s | %-15s"%("NÚMERO DA CONTA:","AGÊNCIA BANCÁRIA:","TIPO DA CONTA:","TITULAR DA CONTA:","SALDO DA CONTA:"))
		print("-" * 21,"-" * 19,"-" * 17, "-" * 37, "-" * 17)
		print("%-20s | %-17s | %-15s | %-35s | R$ %-15s"%(numeroContaOrigem,contas[numeroContaOrigem][0],contas[numeroContaOrigem][1],contas[numeroContaOrigem][2],contas[numeroContaOrigem][3]))	
		print("-" * 115)

		print("\n"," " * 41,"CONTA BANCÁRIA DE DESTINO LOCALIZADA!")
		print("-" * 115)
		print("%-20s | %-15s | %-15s | %-35s | %-15s"%("NÚMERO DA CONTA:","AGÊNCIA BANCÁRIA:","TIPO DA CONTA:","TITULAR DA CONTA:","SALDO DA CONTA:"))
		print("-" * 21,"-" * 19,"-" * 17, "-" * 37, "-" * 17)
		print("%-20s | %-17s | %-15s | %-35s | R$ %-15s"%(numeroContaDestino,contas[numeroContaDestino][0],contas[numeroContaDestino][1],contas[numeroContaDestino][2],contas[numeroContaDestino][3]))
		print("-" * 115)
		print()

		saldo = contas[numeroContaOrigem][3]
		transferencia = float(input("Informe o valor da transferência: "))
		taxa = float(input("Informe a taxa de cobrança      : "))
		print()

		if saldo >= transferencia + taxa:
			confirma = input("Confirma a transferência da quantia R$ %.2f (S/N) ? "%transferencia)
			print()

			if confirma.upper() == "S":
				transferencias[data_f] = [numeroContaOrigem,transferencia]
				contas[numeroContaOrigem][3] -= transferencia + taxa
				contas[numeroContaDestino][3] += transferencia 
				print("Operação realizada com sucesso.\n")

			elif confirma.upper() == "N":
				print("Operação cancelada.\n")

			else:
				print("Você informou um valor inválido para esta operação.\n")

		else:
			print("SALDO INSUFICIENTE.\n")

	else:
		print("\nOs números das contas informadas não existem em nossa base de dados.\n")

def emitirSaldo():
	print("\nMódulo - Emitir Saldo\n")
	data_f = gerarData()
	numeroConta = input("Informe o número da sua conta : ")
	taxa = float(input("Informe a taxa de cobrança    : "))
	print()

	if numeroConta in contas:
		saldo = contas[numeroConta][3]
		if saldo >= taxa:
			contas[numeroConta][3] -= taxa
			saldo = contas[numeroConta][3]
			print("-------------------------------------------------------\n")
			print(" EMISSÃO DE SALDO : %s"%data_f)
			print(" TAXA COBRADA     : R$ %.2f"%taxa)
			print(" CONTA            : %s"%numeroConta)
			print(" AGÊNCIA          : %s"%contas[numeroConta][0])
			print(" TIPO CONTA       : %s"%contas[numeroConta][1])
			print(" TITULAR          : %s"%contas[numeroConta][2])
			print(" SALDO ATUAL      : R$ %.2f\n"%saldo)
			print("-------------------------------------------------------\n\n")

		else:
			print("SALDO INSUFICIENTE.\n")

	else:
		print("\nO número da conta informada não existe em nossa base de dados.\n")

def emitirExtrato():
	print("\nMódulo - Emitir Extrato\n")
	data_f = gerarData()
	numeroConta = input("Informe o número da sua conta bancária  : ")
	mes = input("Informe o mês que deseja ver o extrato  : ")
	ano = input("Informe o ano que deseja ver o extrato  : ")
	data_v = mes + "/" + ano
	taxa = float(input("Informe a taxa de cobrança do seu banco : "))

	achouSaque = False
	achouDeposito = False
	achouTransferencia = False
	achouPagamento = False
	print()

	if numeroConta in contas:	
		saldo = contas[numeroConta][3]
		if saldo >= taxa:
			contas[numeroConta][3] -= taxa
			saldo = contas[numeroConta][3]
			print("------------------ EXTRATO BANCÁRIO ------------------\n")
			print(" DATA DE EMISSÃO  : %s"%data_f)
			print(" TAXA DE EMISSÃO  : R$ %.2f"%taxa)
			print(" CONTA            : %s"%numeroConta)
			print(" AGÊNCIA          : %s"%contas[numeroConta][0])
			print(" TIPO CONTA       : %s"%contas[numeroConta][1])
			print(" TITULAR          : %s"%contas[numeroConta][2])
			print(" SALDO ATUAL      : R$ %.2f\n"%saldo)
			print("---------------- HISTÓRICO FINANCEIRO ----------------\n")
			print("%-20s  %-15s  %-20s"%(" DATA:"," VALOR:"," DESCRIÇÃO:"))
			print()

			arq = open('extrato.txt', 'w')
			arq.write("")
			arq.close()

			arq = open('extrato.txt', 'a')
			arq.write("------------------ EXTRATO BANCÁRIO ------------------\n\n")
			arq.write(" DATA DE EMISSÃO : %s"%data_f + "\n")
			arq.write(" TAXA DE EMISSÃO : R$ %.2f"%taxa + "\n")
			arq.write(" CONTA           : %s"%numeroConta + "\n")
			arq.write(" AGÊNCIA         : %s"%contas[numeroConta][0] + "\n")
			arq.write(" TIPO CONTA      : %s"%contas[numeroConta][1] + "\n")
			arq.write(" TITULAR         : %s"%contas[numeroConta][2] + "\n")
			arq.write(" SALDO ATUAL     : R$ %.2f"%saldo + "\n\n")
			arq.write("---------------- HISTÓRICO FINANCEIRO ----------------\n\n")
			arq.write("%-20s  %-15s  %-20s\n\n"%(" DATA:"," VALOR:"," DESCRIÇÃO:"))
			arq.close()

			for a,b in saques.items():
				if (saques[a][0] == numeroConta) and (a[3:10] == data_v):
					print(" %-20s  %-15s  %-20s"%(a,"R$ " + str(saques[a][1]),"SAQUE"))
					arq = open('extrato.txt','a')
					arq.write(" %-20s  %-15s  %-20s\n"%(a,"R$ " + str(saques[a][1]),"SAQUE"))
					arq.close()
					achouSaque = True

			for c,d in depositos.items():
				if(depositos[c][0] == numeroConta) and (c[3:10] == data_v):
					print(" %-20s  %-15s  %-20s"%(c,"R$ " + str(depositos[c][1]),"DEPÓSITO"))
					arq = open('extrato.txt','a')
					arq.write(" %-20s  %-15s  %-20s\n"%(c,"R$ " + str(depositos[c][1]),"DEPÓSITO"))
					arq.close()
					achouDeposito = True
			
			for e,f in transferencias.items():
				if(transferencias[e][0] == numeroConta) and (e[3:10] == data_v):
					print(" %-20s  %-15s  %-20s"%(e,"R$ " + str(transferencias[e][1]),"TRANSFERÊNCIA"))
					arq = open('extrato.txt','a')
					arq.write(" %-20s  %-15s  %-20s\n"%(e,"R$ " + str(transferencias[e][1]),"TRANSFERÊNCIA"))
					arq.close()
					achouTransferencia = True

			for g,h in pagamentos.items():
				if(pagamentos[g][0] == numeroConta) and (g[3:10] == data_v):
					print(" %-20s  %-15s  %-20s\n"%(g,"R$ " + str(pagamentos[g][2]),pagamentos[g][1]))
					arq = open('extrato.txt','a')
					arq.write(" %-20s  %-15s  %-20s\n\n"%(g,"R$ " + str(pagamentos[g][2]),pagamentos[g][1]))
					arq.close()
					achouPagamento = True

			if achouSaque == False:
				print(" NÃO HOUVE SAQUES EM %s."%data_v)
				arq = open('extrato.txt','a')
				arq.write(" NÃO HOUVE SAQUES EM %s.\n"%data_v)
				arq.close()

			if achouDeposito == False:
				print(" NÃO HOUVE DEPÓSITOS EM %s."%data_v)
				arq = open('extrato.txt','a')
				arq.write(" NÃO HOUVE DEPÓSITOS EM %s.\n"%data_v)
				arq.close()

			if achouTransferencia == False:
				print(" NÃO HOUVE TRANSFERÊNCIAS EM %s."%data_v)
				arq = open('extrato.txt','a')
				arq.write(" NÃO HOUVE TRANSFERÊNCIAS EM %s.\n"%data_v)
				arq.close()

			if achouPagamento == False:
				print(" NÃO HOUVE PAGAMENTOS DE CONTAS EM %s.\n"%data_v)
				arq = open('extrato.txt','a')
				arq.write(" NÃO HOUVE PAGAMENTOS EM %s.\n\n"%data_v)
				arq.close()

			print()  

			confirma = input("Deseja receber o extrato por e-mail (S/N) ? ")
			print()

			if confirma.upper() == "S":

				try:
					email = input("Informe seu e-mail: ")
					email_from = "pyfinanc@gmail.com"
					email_to = email

					smtp = "smtp.gmail.com"

					server = smtplib.SMTP(smtp, 587)
					server.starttls()
					server.login(email_from, open('senha.txt').read().strip())

					message = "Olá, somos da equipe do PyFinance. Anexamos o seu EXTRATO MENSAL logo abaixo. Qualquer dúvida entre em contato conosco através deste e-mail.\n"
					msg = MIMEMultipart()
					msg['Subject'] = 'EXTRATO MENSAL'
					msg.attach(MIMEText(message, 'plain'))

					filename = 'extrato.txt'
					attachment = open('extrato.txt', 'rb')

					part = MIMEBase('application','octet-stream')
					part.set_payload((attachment).read())
					encoders.encode_base64(part)
					part.add_header('Content-Disposition', "attachment; filename = %s" %filename)

					msg.attach(part)
					attachment.close()

					server.sendmail(email_from, email_to, msg.as_string())
					server.quit()

					print("\nE-mail enviado com sucesso.\n")
				
				except:
					print("\nErro ao enviar e-mail.\n")
			
			elif confirma.upper() == "N":
				print("Tudo bem! Talvez da próxima.\n")
			
			else:
				print("Você informou um valor inválido para esta operação.\n")

		else:
			print("SALDO INSUFICIENTE.\n")
		
	else:
		print("\nO número da conta informada não existe em nossa base de dados.\n")




