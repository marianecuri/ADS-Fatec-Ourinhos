// Imprimir a Matriz C resultante de AxB.

#include <iostream>
using namespace std;

int main (){
	long int lin_A, col_A, lin_B, col_B, p, q, r;

	// Matriz A
	cin >> lin_A >> col_A;
	int A[lin_A][col_A] = {};
	
	for (p=0; p<lin_A; p++){

		for (q=0; q<col_A; q++)
			cin >> A[p][q];
            
	}
	
	// Matriz B
	cin >> lin_B >> col_B;
	int B[lin_B][col_B] = {};
	
	for (q=0; q<lin_B; q++){

		for (r=0; r<col_B; r++)
			cin >> B[q][r];

	}
	
	// Matriz C (AxB)
	int AxB[lin_A][col_B] = {};
	
	for (p=0; p<lin_A; p++){

		for (r=0; r<col_B; r++){

			for (q=0; q<col_A; q++)
				AxB[p][r] = AxB[p][r] + (A[p][q] * B[q][r]);

		}

	}
	
	for (p=0; p<lin_A; p++){

		for (r=0; r<col_B; r++)
			cout << AxB[p][r] << "\t";
        
		cout << endl;
	}
	
	return 0;
}