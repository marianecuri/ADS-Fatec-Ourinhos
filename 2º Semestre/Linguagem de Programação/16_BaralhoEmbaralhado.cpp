/* Seu programa deve produzir um único inteiro, o número mínimo
de vezes que o processo de embaralhamento deve ser repetido para
que o baralho fique novamente ordenado. */

#include <iostream>
using namespace std;

int main (){
	int p, a=2, b=1;
	
	cin >> p;
	
	while (a!=1){
		
		if (a<=(p/2))
			a += a;	
		
		else
			a -= (p-a+1);	
		
		b++;
	}
		
	cout << b << endl;
	
	return 0;
}