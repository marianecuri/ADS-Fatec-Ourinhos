/* Você receberá uma única entrada, um valor de n, e seu trabalho
é calcular a aproximação de e para esse valor de n. */

#include <iostream>
#include <iomanip>
using namespace std;

int main (){
	int n;
	long double e=0, fat=1;
	
	cin >> n;
	
    for (int i=0; i<=n; i++){
    	
		if (i>1.0)
			fat*=i;
			
		e+= (1.0/fat);
		
	}
	
    cout << setprecision (17);
	cout << e << endl;
	
	return 0;
}