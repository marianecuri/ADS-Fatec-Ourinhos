/* A entrada é o número de discos posicionados inicialmente no pino A e como 
resposta seu programa deve imprimir todos os movimentos que solucionarão o
problema. Mover todos os discos do pino A para o pino B usando C como auxiliar. */

#include <iostream>
using namespace std;

void hanoi (int, char, char, char);
int main (){
	int n;
	
	cin >> n;
	hanoi (n, 'A', 'B', 'C');
	
	return 0;
}

void hanoi (int d, char A, char B, char C){

	if (d==1)
		cout << "Mover disco " << d << " do pino " << A << " para pino " << B << endl;
	
	else {
		hanoi (d-1, A, C, B);
		cout << "Mover disco " << d << " do pino " << A << " para pino " << B << endl;
		hanoi (d-1, C, B, A);
	}

}