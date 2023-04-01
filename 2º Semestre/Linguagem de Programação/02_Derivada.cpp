/* A entrada é um dado grau G, na sequência são informados
G elementos do polinômio. Teremos G+1 linhas subsequentes.
O resultado deve ser a derivada primeira do polinômio informado. */

#include <iostream>
#include <iomanip>
using namespace std;

void derivada (double*, int);
int main (){
	int g;

	cin >> g;
	
	int expoente=g;
	double vet[g+1];
	
	for (int i=0; i<=g; i++)
		cin >> vet[i];
	
	derivada (vet, g);
	
	for (int i=0; i<=g; i++){
		
		expoente--;
		cout << fixed << setprecision (0);
		cout << vet[i];
		
		if (expoente!=0 and expoente!=1)
			cout << "x^" << expoente << "+";
		
		else if (expoente==1)
			cout << "x+";
		
		else
			break;
		
	}
	
	return 0;
}

void derivada (double* vet, int grau){
	int expoente=grau;
	
	for (int i=0; i<=grau; i++){
		vet[i] = vet[i]*expoente;
		expoente--;
	}

}