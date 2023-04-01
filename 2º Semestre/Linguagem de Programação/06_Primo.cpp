/* Implementar um programa que dado um número inteiro, seu
programa deve responder se o mesmo é ou não primo. */

#include <iostream>
using namespace std;

void primo (int);
int main (){
	int n;
	
	cin >> n;
	primo (n);
	
	return 0;
}

void primo (int n){
	int contador=0;
	
    for (int i=1; i<=n; i++){
		if (n%i==0)
			contador++;
	}
	
	if (contador==2)
		cout << "PRIMO" << endl;
		
	else
		cout << "!PRIMO" << endl;

}