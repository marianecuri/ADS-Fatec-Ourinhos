/* Seu programa deve produzir uma única linha, contendo um único inteiro,
que deve ser igual a r módulo 10^4, onde r é o número de sequências distintas
de L botões que levam o usuário da nave S para a nave T. */

#include <iostream>
using namespace std;

template <typename T> inline T abs (T t) {return t < 0? -t : t;}
const int modn = 10000;
inline int mod (int x) {return x % modn;}
int n, l, s, t;

void mult (int a[102][102], int b[102][102], int c[102][102]){
   
    for (int i=0; i<n; i++){
    
		for (int j=0; j<n; j++){
            c[i][j] = 0;
            
            for (int k=0; k<n; k++)
            	c[i][j] = mod (c[i][j] + a[i][k] * b[k][j]);
                
        }
        
	}
        
}


void cp (int a[102][102], int b[102][102]){
   
    for (int i=0; i<n; i++){
    
		for (int j=0; j<n; j++)
        	b[i][j] = a[i][j];
		
	}
           
}


int adj[102][102], resp[102][102];
int aux[102][102];


void fexp (){
	
    for (int i=0; i<n; i++){
    	
    	for (int j=0; j<n; j++)
        	resp[i][j] = (i==j);
		
	}
             
    for (int i=1; i<=l; i<<=1){
        
		if (i & l){
            mult (adj, resp, aux);
            cp (aux, resp);
        }
        
        mult (adj, adj, aux);
        cp (aux, adj);
    }
    
}


int main (){
    int a, b, c, d;
    
 	cin >> n >> l;
 	cin >> s >> t;
 	
    for (int i=0; i<n; i++){
        cin >> a >> b >> c >> d;
        
        for (int j=0; j<n; j++)
        	adj[i][j] = 0;
		
        adj[i][--a]++; adj[i][--b]++; adj[i][--c]++; adj[i][--d]++;
    }
    
    fexp ();
    cout << resp[--s][--t] << endl;
    
    return 0;
}