/* Implementar um programa que dados os números de pomonas x em estoque no
primeiro dia e um número m, que responda se a produção parará em algum momento.
Considere que o intervalo máximo de dias sem pedidos é de 30 dias. */

#include <iostream>
using namespace std;

int main (){
	int x, m, fim;
	
	cin >> x >> m;
	
	for (int i=0; i<=30; i++){
		
		if (x%m==0)
			fim = 1;
		
		else {
			x = x + (x%m);
			fim = 0;
		}
		
	}
	
	if (fim==0)
		cout << "NONSTOP" << endl;
		
	else
		cout << "STOP" << endl;
	
	return 0;
}