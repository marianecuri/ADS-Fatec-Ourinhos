/* Implementar um programa que dados dois vértices e um ponto
qualquer, responda se o ponto é interno ou externo ao retângulo. */

#include <iostream>
using namespace std;

void dentro_ret (int, int, int, int, int, int);
int main (){
	int x0, y0, x1, y1, x, y;
	
	cin >> x0 >> y0;
	cin >> x1 >> y1;
	cin >> x >> y;
	dentro_ret (x0, y0, x1, y1, x, y);
	
	return 0;
}

void dentro_ret (int x0, int y0, int x1, int y1, int x, int y){

	if ((x0<x1) and (x<x0 or x>x1 or y<y0 or y>y1))
		cout << "EXTERNO" << endl;
	
	else if ((x0>x1) and (x>x0 or x<x1 or y<y0 or y>y1))
		cout << "EXTERNO" << endl;
	
	else
		cout << "INTERNO" << endl;

}