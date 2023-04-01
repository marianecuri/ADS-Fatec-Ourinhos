/* A entrada é um dado grau G e o valor X a ser avaliado,
na sequência são informados G elementos do polinomio. O
resultado deve ser double com precisão de 2 casas decimais. */

#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

double poli (double*, int, double);
int main (){
	int g;
	double x, resultado;
	
	cin >> g >> x;
	
	int expoente=g;
	double vet[expoente+1];
	
	for (int i=0; i<=g; i++)
		cin >> vet[i];
	
	resultado = poli (vet, g, x);
	cout << fixed << setprecision (2);
	cout << resultado << endl;

	return 0;
}

double poli (double* vet, int grau, double x){
	double resultado=0;
	int expoente=grau;
	
	for (int i=0; i<=grau; i++){
		resultado = resultado + (vet[i]) * pow(x, expoente);
		expoente--;
	}

	return resultado;
}