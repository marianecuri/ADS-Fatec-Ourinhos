/* Seu programa deve imprimir uma única linha, contendo a
quantidade de sequências que se repetem dentro do segmento. */

#include <iostream>
#include <cstring>
using namespace std;

int main (){
	int t, seq=0, test, rep=0;
	char x[16], d[16], z[16], sub[16], sub2[16][16]={0};
	
	cin >> x >> d >> z;
	cin >> t;
	
	if (strlen (x)<4 or strlen (x)>15 or strlen (d)<4 or strlen (d)>15 or strlen (z)<4 or strlen (z)>15 or t<2 or t>15)
		return 0;
	
	if (strstr (x, " ") or strstr (d, " ") or strstr (z, " "))
		return 0;
	
	test = strlen (x);
	
	for (int i=0; i<=(test-t); i++){
        strncpy (sub, x+i, t);
        sub[t] = '\0';
        
        if (strstr (d, sub) and strstr (z, sub)){
           
		    for (int i=0; i<seq; i++){   
				if (strcmp (sub2[i], sub)==0){
                    rep = 1;
                    break;
                }
            }

            if (!rep){
                strcpy (sub2[seq], sub);
                seq++;
            }
            
        }
        
    }
    
	cout << seq << endl;
	
	return 0;
}