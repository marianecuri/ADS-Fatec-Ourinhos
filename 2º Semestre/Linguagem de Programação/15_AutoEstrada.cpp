/*  P = 2
	C = 2
	A = 1
	D = 0
Seu programa deve imprimir um número inteiro representando
quantas unidades de painel săo necessárias para cobrir toda a
extensăo da auto estrada. */

#include <iostream>
#include <cstring>
using namespace std;

int main (){
	int c, painel=0;
	
	cin >> c;
	char codigo[c];
	cin >> codigo;
	
	for (int i=0; i<c; i++){
	
		if ((codigo[i]=='P') or (codigo[i]=='C'))
			painel = painel+2;
	
		if (codigo[i]=='A')
			painel = painel+1;
		
	}

	cout << painel << endl;
			
	return 0;
}