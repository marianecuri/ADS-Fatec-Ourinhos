// Descobrir o n-ésimo termo da série Fibonacci.

#include <iostream>
using namespace std;

long int fibonacci (long int);
int main (){
	long int n;
	
	cin >> n;   
	cout << fibonacci (n);
	
	return 0;
}

long int fibonacci (long int n){
	long int i, f=0, t1=0, t2=1;
	
	for (i=1; i<=n; i++){
        
        f = t1+t2;
        
        if (i<=2){
        	f=1;
		}
		
        t1 = t2;
        t2 = f;
    
	}
	
	return f;
}