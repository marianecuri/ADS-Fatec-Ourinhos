/* Elaborar um programa que dadas as leituras do sensor
fototérmico, informe se é possível realizar a jogada ou não*/

#include <iostream>
using namespace std;

int main (){
	int t, n, L[4], R[4], x=0, direita=0, esquerda=0;
	
	cin >> t >> n;
	
	while (x<n){
	
		for (int i=0; i<4; i++)
			cin >> L[i];
	
		for (int i=3; i>=0; i--)
			cin >> R[i];
		
		if (t>R[0] and t>R[1] and t>R[2]){
			cout << "RIGTH SIDE!" << endl;
			direita++;
		}
		
		else if (t>L[0] and t>L[1] and t>L[2]){
			cout << "LEFT SIDE!" << endl;
			esquerda++;
		}
		
		else
			cout << "NO PERFORM!!!" << endl;
	
		x++;	
	}
	
	if (direita!=0 and esquerda!=0){
		
		if (esquerda<direita)
			cout << "LEFT SIDE!!! THE STRONG SIDE!!!" << endl;
		
		else
			cout << "RIGTH SIDE!!! THE STRONG SIDE!!!" << endl;
		
	}
	
	else
		cout << "WEAK SIDE!!! BOTH SIDE!!!" << endl;
	
	return 0;
}