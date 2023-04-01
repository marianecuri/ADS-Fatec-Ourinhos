/* Criar um programa que dada a sequência s ele deve informar uma
sequência de 26 números contendo frequência de digitação de cada letra. */

#include <iostream>
#include <cstring>
#define ALFMAX 30
using namespace std;

int main (){
	long int j, ni, k, x;
	
	cin >> j;
	
	while (j--){
		cin >> ni >> k;
		char s[ni+2];
		long int alf [ALFMAX];
		
		for (int i=0; i<ALFMAX; i++)
			alf[i]=0;
		
		cin >> s;
		
		while (k--){
			cin >> x;
			for (int i=0; i<x; i++)
				alf[s[i]-'a']++;
		}
		
		long int tam = strlen(s);
		
		for (int i=0; i<tam; i++)
			alf[s[i]-'a']++;

		for (int i=0; i<26; i++){
		
			if (i!=0)
				cout << "\t";
			
			cout << alf[i];
		}
		
		cout << endl;
	}
	
	return 0;
}