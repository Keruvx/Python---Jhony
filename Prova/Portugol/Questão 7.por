programa
{
	
	funcao inicio()
	{


	inteiro n
	inteiro impar=0
	inteiro par=0
	
	para(inteiro i = 1; i<=5; i++){
		escreva("Informe um numero: ")leia (n)

		
	se(n % 2 == 0){
		par = par++
	}
	senao{
		impar = impar++
	}
	}
	
	escreva("Numeros impares: ",impar)
	escreva("\nNumeros pares: ",par)







	
	
	}

	
}




/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 291; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */