/* Dado um numero qualquer n, seu programa deverá
retornar Hn com precisão de 8 casa decimais. */

#include <iostream>
#include <iomanip>
using namespace std;

int main (){
	int n;
	float h=0.0;
	
	cin >> n;
	std::cout << std::fixed << std::setprecision (8);
	
	for (int i=1; i<=n; i++)
        h = (h) + (1.0/i);
    	
	std::cout << h << std::endl;
	
	return 0;
}