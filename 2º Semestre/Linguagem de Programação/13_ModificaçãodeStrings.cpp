/* Escolher um k tal que a cadeia obtida após a modificação mencionada
seja lexicograficamente a menor possível entre todas as opções de k. */

#include <iostream>
#include <cstring>
#define N 5005
using namespace std;

int main (){
	char s[N], s_ans[N], temp[N];
	int ans_int, t;
	
	cin >> t;
	
	while (t--){
		int n;
		cin >> n >> s;
		
		ans_int = 1;
		strcpy (s_ans, s);
		int j1, j2;
		char c;
		
		for (int k=2; k<=n; k++){
			strcpy (temp, s);
			
			for (int i=0; i<=(n-k); i++){
				j1 = i;
				j2 = i+k-1;
				
				while (j1<j2){
					c = temp[j1];
					temp[j1] = temp[j2];
					temp[j2] = c;
					j1++;
					j2--;
				}
				
			}
	
			if (strcmp (temp, s_ans)<0){
				strcpy (s_ans, temp);
				ans_int = k;
			}
				
		}
			
		cout << s_ans << endl << ans_int << endl;
	}
	
	return 0;
}