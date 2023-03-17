#include <iostream>
#include <cstdio>
#include <cstring>
#include <clocale>
using namespace std;

struct Produto {
  wchar_t nome[30];    // Nome do produto
  int codigo;          // Código do produto
  double preco;        // Preço do produto
};

int main (){
  setlocale (LC_ALL, "Portuguese");   // Define a localidade
  Produto produtos[10];               // Cria um vetor de 10 produtos

  // Atribui os valores ao primeiro produto
  wcscpy (produtos[0].nome, L"Pé de Moleque");
  produtos[0].codigo = 13205;
  produtos[0].preco = 0.20;

  // Atribui os valores ao segundo produto
  wcscpy (produtos[1].nome, L"Cocada Baiana");
  produtos[1].codigo = 15202;
  produtos[1].preco = 0.50;

  // Pede ao usuário os valores dos próximos oito produtos
  for (int i=2; i<10; i++){
    wcout << L"Produto " << i+1 << endl;

    wcout << L"Nome: ";
    if (i>2)
      wcin.getline (produtos[i].nome, 30);   // Dummy getline() call
    wcin.getline (produtos[i].nome, 30);

    wcout << L"Código: ";
    wcin >> produtos[i].codigo;

    wcout << L"Preço: ";
    wcin >> produtos[i].preco;

    wcout << endl;
  }

  // Altera a precisão para 2 casas decimais
  wcout.precision (2);
  wcout << fixed;

  // Imprime na tela um menu contendo os produtos
  wcout << L"\nLista de produtos:\n" << endl;

  for (int i=0; i<10; i++)
    wcout << L"[" << i+1 << L"] " << produtos[i].nome << endl;

  wcout << L"\nDigite o número de um produto para conferir mais informações sobre ele." << endl;
  wcout << L"Pressione qualquer outra tecla para sair.\n" << endl;

  // Mostra as informações do produto escolhido
  int i = 0;
  while (wcin >> i) {

    if (i>0 and i<=10){
      wcout << L"Nome: " << produtos[i-1].nome << endl;
      wcout << L"Código: " << produtos[i-1].codigo << endl;
      wcout << L"Preço: R$ " << produtos[i-1].preco << endl;
      wcout << endl;
    }

    else {
      wcout << L"Saindo do programa..." << endl;
      break;
    }

  }

  return 0;
}