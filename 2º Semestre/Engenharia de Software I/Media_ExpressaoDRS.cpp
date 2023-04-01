/* Escreva um algoritmo que leia três números inteiros
e positivos (A, B, C) e calcule a expressão. */

#include <iostream>
#include <clocale>
using namespace std;

int main (){
    setlocale (LC_ALL, "Portuguese");
    int a, b, c, d, r, s;
    
    do {
        cout << "A: ";
        cin >> a;
    } while (a<1 or a>10);
    
    do {
        cout << "B: ";
        cin >> b;
    } while (b<1 or b>10);
    
    do {
        cout << "C: ";
        cin >> c;
    } while (c<1 or c>10);
    
    r = (a+b)*(a+b);
    s = (b+c)*(b+c);
    d = (r+s)/2;
    
    if (d<200)
        wcout << L"Valor abaixo da média." << endl;
    
    else if (d==200)
        wcout << L"Valor na média." << endl;
    
    else
        wcout << L"Valor acima da média." << endl;
    
    return 0;
}