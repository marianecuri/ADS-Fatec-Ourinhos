/* A entrada são três números reais, A, B e C. Imprima
os valores das duas raízes (2 casas decimais), quando
existirem. Quando não existirem imprima NARN. */

#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

void raizes (float, float, float, float*, float*);
int main (){
	float a, b, c, x1, x2;
	
	cin >> a >> b >> c;
    raizes (a, b, c, &x1, &x2);

	return 0;
}

void raizes (float a, float b, float c, float* x1, float* x2){
	float delta;
	
    delta = b*b - 4*a*c;
    
    if (a==0 or delta<0)
    	cout << "NARN" << endl;	
    
	else {
		*x1 = (-b + sqrt(delta)) / (2*a);
    	*x2 = (-b - sqrt(delta)) / (2*a);
    	cout << fixed << setprecision (2);
    	cout << *x1 << "\t" << *x2 << endl;
    }

}