programa
{
	
	funcao inicio()
	{
	cadeia userName
	cadeia userSenha
	cadeia login
	cadeia senha
	inteiro tent=0

	escreva("Olá, efetue seu cadastro\n\n")
	escreva("Informe Login: ")leia (userName)
	escreva("Informe senha: ")leia (userSenha)

	escreva("\n\nEntrar no sistema\n\n")


	enquanto(tent < 3){
		
	escreva("\nLogin: ")leia (login)
	escreva("Senha: ")leia (senha)
		
	se(login != userName e login != userSenha){
		escreva("Tentativa ",tent+1," invalida")
		tent = tent+1
	}
	se(login == userName e senha == userSenha){
		escreva("\nLogin realizado com sucesso!❤️")
	}
	se(tent == 3){
		escreva("\nAcesso bloqueado")
	}
	}
	
	}

}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 608; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */