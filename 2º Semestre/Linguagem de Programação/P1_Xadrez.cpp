/* Um tabuleiro de xadrez é composto por 64 casas espalhadas regularmente num layout
de 8x8 e com as casas em cores alternadas. Criar um programa que gere um arquivo PGM:
A única exigência é quanto ao número de pixels que cada casa do tabuleiro deve ter em altura e largura. */

#include <iostream>
using namespace std;

int main (){
	int N, G, linha, coluna;
	
	cin >> N >> G;
	cout << "P2" << endl;
	cout << 8*N << "\t" << 8*N << endl;
	cout << G << endl;
	
	for (linha=1; linha<=(8*N); linha++){
		
		if ((linha<=N) or (linha>(2*N) and linha<=(3*N)) or (linha>(4*N) and linha<=(5*N)) or (linha>(6*N) and linha<=(7*N))){
		
			for (coluna=1; coluna<=(8*N); coluna++){
			
				if ((coluna<=N) or (coluna>(2*N) and coluna<=(3*N)) or (coluna>(4*N) and coluna<=(5*N)) or (coluna>(6*N) and coluna<=(7*N)))
					cout << G << "\t";
			
				else
					cout << "0" << "\t";
				
			}
		
		}
			
		else {
		
			for (coluna=1; coluna<=(8*N); coluna++){
			
				if ((coluna<=N) or (coluna>(2*N) and coluna<=(3*N)) or (coluna>(4*N) and coluna<=(5*N)) or (coluna>(6*N) and coluna<=(7*N)))
					cout << "0" << "\t";
			
				else
					cout << G << "\t";
				
			}
		
		}
		
		cout << endl;
	}
				
	return 0;
}