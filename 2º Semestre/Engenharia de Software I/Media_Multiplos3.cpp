/* Escrever um algoritmo que leia 10 números inteiros e positivos.
Calcule e exiba a média dos números divisíveis por 3. */

#include <iostream>
#include <clocale>
using namespace std;

int main (){
	setlocale (LC_ALL, "Portuguese");
	int vet[10], i=0, soma=0, contador=0;
	float media;
	
	wcout << L"Digite 10 números inteiros e positivos: " << endl;
	
	while (i<10){
		
		do {
			cin >> vet[i];
		} while (vet[i]<1);
		
		i++;
	}
	
	i=0;

	while (i<10){
	
		if (vet[i]%3 == 0){
			soma = soma + vet[i];
			contador++;
		}
		
		i++;
	}
	
	if (contador==0)
		wcout << L"Não há nenhum número divisível por 3." << endl;

	else {
		media = (1.0*soma)/(1.0*contador);
		wcout << L"A média dos números divisíveis por 3 é " << media << "." << endl;
	}

	return 0;
}