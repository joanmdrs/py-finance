import funcoes as func

func.verificarArquivoReceitas()
func.verificarArquivoDespesas()
func.verificarArquivoPagamentos()
func.verificarArquivoCarteira()
func.verificarArquivoContas()
func.verificarArquivoSaques()
func.verificarArquivoDepositos()
func.verificarArquivoTransferencias()

resp = ""
while resp != "0":

	resp = func.menu()

# 1 ______________________________________________________________________
	if resp == "1":
		func.addReceita()

# 2 ______________________________________________________________________
	elif resp == "2":
		func.buscarReceita()

# 3 ______________________________________________________________________
	elif resp == "3":
		func.excluirReceita()

# 4 ______________________________________________________________________
	elif resp == "4":
		func.editarReceita()

# 5 ______________________________________________________________________
	elif resp == "5":
		func.listarReceitas()

#6 _______________________________________________________________________
	elif resp == "6":
		func.adicionarDespesa()

#7 _______________________________________________________________________
	elif resp == "7":
		func.buscarDespesa()

#8 _______________________________________________________________________
	elif resp == "8":
		func.excluirDespesa()

#9 _______________________________________________________________________
	elif resp == "9":
		func.editarDespesa()

#10 ______________________________________________________________________
	elif resp == "10":
		func.listarDespesas()

#11   ______________________________________________________________________
	elif resp == "11":
		func.pagarDespesa()

#12 ______________________________________________________________________
	elif resp == "12":
		func.relatorioMensal()

#13 _________________________________________________________________________
	elif resp == "13":
		func.relatorioAnual()

#14 ____________________________________________________________________
	elif resp == "14":
		func.gerenciarCarteira()

#15 ___________________________________________________________________
	elif resp == "15":
		func.adicionarConta()

#16 ____________________________________________________________________
	elif resp == "16":
		func.buscarConta()

#17 ____________________________________________________________________
	elif resp == "17":
		func.excluirConta()

	#18 ____________________________________________________________________
	elif resp == "18":
		func.editarConta()

	#19 ____________________________________________________________________
	elif resp == "19":
		func.listarContas()

	#20 ____________________________________________________________________
	elif resp == "20":
		func.realizarSaque()

#21 ______________________________________________________________________
	elif resp == "21":
		func.realizarDeposito()

	#22 ____________________________________________________________________
	elif resp == "22":
		func.realizarTransferencia()

	#23 ____________________________________________________________________
	elif resp == "23":
		func.emitirSaldo()

	#24 ______________________________________________________________________
	elif resp == "24":
		func.emitirExtrato()

	elif int(resp) < 0 or int(resp) > 24:
		print("\nVocê informou um valor inválido para esta operação.\n")

print("\nOBRIGADO POR USAR O NOSSO SISTEMA!\n")
func.gravarArquivoReceitas()
func.gravarArquivoDespesas()
func.gravarArquivoCarteira()
func.gravarArquivoContas()
func.gravarArquivoSaques()
func.gravarArquivoDepositos()
func.gravarArquivoTransferencias()
func.gravarArquivoPagamentos()