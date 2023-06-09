#include <iostream>
#include <string>
#include <locale>
using namespace std;

// Define a Struct Restaurante
struct Restaurante {
    wstring nome;
    wstring endereco;
    wstring tipoComida;
    float notaCozinha;
    Restaurante* proximo;
};

// Função que cria um novo restaurante e retorna um ponteiro para ele
Restaurante* criarRestaurante (wstring nome, wstring endereco, wstring tipoComida, float notaCozinha){
    Restaurante* novoRestaurante = new Restaurante {nome, endereco, tipoComida, notaCozinha, nullptr};
    return novoRestaurante;
}

// Função que insere um novo restaurante na lista encadeada
void inserirRestaurante (Restaurante** lista, wstring nome, wstring endereco, wstring tipoComida, float notaCozinha){
    Restaurante* novoRestaurante = criarRestaurante (nome, endereco, tipoComida, notaCozinha);

    // Compara as strings para ordenar a lista em ordem alfabética
    if (*lista == nullptr or wcscoll((*lista)->nome.c_str(), nome.c_str()) > 0){
        novoRestaurante->proximo = *lista;
        *lista = novoRestaurante;
        return;
    }

    Restaurante* atual = *lista;

    while (atual->proximo != nullptr and wcscoll(atual->proximo->nome.c_str(), nome.c_str()) < 0){
        atual = atual->proximo;
    }

    novoRestaurante->proximo = atual->proximo;
    atual->proximo = novoRestaurante;
}

// Função que cadastra previamente alguns restaurantes na lista encadeada
void cadastrarRestaurantes (Restaurante** lista){
    inserirRestaurante (lista, L"Casarao Bar e Gastronomia", L"R. Antônio Luís Viana, 663 - Centro, Ribeirão do Sul - SP", L"Brasileira", 4.0);
    inserirRestaurante (lista, L"Kenko Sushi Bar", L"Av. Antônio Almeida Leite, 841 - Jardim Paulista, Ourinhos - SP", L"Japonesa", 4.5);
    inserirRestaurante (lista, L"La Parrilla Restaurante Argentino", L"R. dos Expedicionários, 1344 - Centro, Ourinhos - SP", L"Argentina", 4.7);
    inserirRestaurante (lista, L"Rancho's Beer", L"R. Padre Diogo Antônio Feijó, 423, Salto Grande - SP", L"Brasileira", 4.7);
    inserirRestaurante (lista, L"Restaurante Castell", L"R. Luzardo García Paes, 502, Ribeirão do Sul - SP", L"Brasileira", 4.7);
}

// Função que percorre a lista e exibe as informações de todos os restaurantes
void listarRestaurantes (Restaurante* lista){
    if (lista == nullptr)
        wcout << L"A lista de restaurantes está vazia." << endl;

    else {
        wcout << L"Lista de restaurantes:" << endl;
        Restaurante* atual = lista;

        while (atual != nullptr){
            wcout << L"\nNome: " << atual->nome << endl;
            wcout << L"Endereço: " << atual->endereco << endl;
            wcout << L"Tipo de comida: " << atual->tipoComida << endl;
            wcout << L"Nota da cozinha: " << atual->notaCozinha << endl;
            atual = atual->proximo;
        }
    }
}

// Função que percorre a lista e exibe as informações dos restaurantes por nota
void listarRestaurantesPorNota (Restaurante* lista, float notaMinima){
    bool encontrou = false;
    wcout << L"Restaurantes com nota igual ou superior a " << notaMinima << L":" << endl;
    Restaurante* atual = lista;
    
    while (atual != nullptr){
        if (atual->notaCozinha >= notaMinima){
            wcout << L"\nNome: " << atual->nome << endl;
            wcout << L"Endereço: " << atual->endereco << endl;
            wcout << L"Tipo de comida: " << atual->tipoComida << endl;
            wcout << L"Nota da cozinha: " << atual->notaCozinha << endl;
            encontrou = true;
        }
        atual = atual->proximo;
    }
    
    if (!encontrou)
        wcout << L"Nenhum restaurante com nota igual ou superior a " << notaMinima << L" encontrado." << endl;
}

// Função que percorre a lista e exibe as informações dos restaurantes por tipo de comida
void listarRestaurantesPorTipoComida (Restaurante* lista, wstring tipoComida){
    bool encontrou = false;
    wcout << L"Restaurantes de comida " << tipoComida << L":" << endl;
    Restaurante* atual = lista;

    while (atual != nullptr){
        if (atual->tipoComida == tipoComida){
            wcout << L"\nNome: " << atual->nome << endl;
            wcout << L"Endereço: " << atual->endereco << endl;
            wcout << L"Tipo de comida: " << atual->tipoComida << endl;
            wcout << L"Nota da cozinha: " << atual->notaCozinha << endl;
            encontrou = true;
        }
        atual = atual->proximo;
    }
    
    if (!encontrou)
        wcout << L"Nenhum restaurante de comida " << tipoComida << L" encontrado." << endl;
}

// Função que atualiza as informações do restaurante especificado
void atualizarRestaurante (Restaurante** lista, wstring nome, wstring novoNome, wstring endereco, wstring tipoComida, float notaCozinha){
    Restaurante* atual = *lista;
    Restaurante* anterior = nullptr;

    while (atual != nullptr){
        if (atual->nome == nome){
            if (anterior == nullptr)
                *lista = atual->proximo;
            else
                anterior->proximo = atual->proximo;

            delete atual;
            inserirRestaurante(lista, novoNome, endereco, tipoComida, notaCozinha);

            wcout << L"Informações do restaurante atualizadas com sucesso!" << endl;
            return;
        }

        anterior = atual;
        atual = atual->proximo;
    }

    wcout << L"Restaurante não encontrado." << endl;
}

// Função que deleta um restaurante especificado
void deletarRestaurante (Restaurante** lista, wstring nome){
    if (*lista == nullptr){
        wcout << L"A lista de restaurantes está vazia." << endl;
        return;
    }
    
    Restaurante* atual = *lista;
    Restaurante* anterior = nullptr;
    
    while (atual != nullptr){
        if (atual->nome == nome){
            if (anterior == nullptr)
                *lista = atual->proximo;
            else
                anterior->proximo = atual->proximo;
            
            delete atual;
            wcout << L"Restaurante deletado com sucesso!" << endl;
            return;
        }
        
        anterior = atual;
        atual = atual->proximo;
    }
    
    wcout << L"Restaurante não encontrado." << endl;
}

// Função que libera a memória alocada dinamicamente para os restaurantes
void liberarLista (Restaurante** lista){
    Restaurante* atual = *lista;

    while (atual != nullptr){
        Restaurante* proximo = atual->proximo;
        delete atual;
        atual = proximo;
    }

    *lista = nullptr;
}

int main (){
    setlocale (LC_ALL, "Portuguese");           // Define a localidade
    Restaurante* listaRestaurantes = nullptr;   // Declara um ponteiro do tipo Restaurante    
    wchar_t opcao;

    cadastrarRestaurantes (&listaRestaurantes); // Chama a função que cadastra restaurantes previamente

    // Exibe um menu de opções para o usuário
    while (true){
        wcout << L"--------------------------------------------------\n" << endl;
        wcout << L"Menu de opções:\n" << endl;
        wcout << L"0) Sair" << endl;
        wcout << L"1) Inserir um novo restaurante" << endl;
        wcout << L"2) Listar todos os restaurantes" << endl;
        wcout << L"3) Listar restaurantes por nota" << endl;
        wcout << L"4) Listar restaurantes por tipo de comida" << endl;
        wcout << L"5) Atualizar informações de um restaurante" << endl;
        wcout << L"6) Deletar um restaurante cadastrado" << endl;
        wcout << L"\nEscolha uma opção: ";
        wcin >> opcao;
        wcin.ignore ();
        wcout << L"\n--------------------------------------------------\n" << endl;
        
        // Sair do programa
        if (opcao == L'0'){
            wcout << L"Saindo do programa..." << endl;
            break;
        }
        
        switch (opcao){
            // Inserir um novo restaurante
            case L'1': {
                wstring nome, endereco, tipoComida;
                float notaCozinha;
                wcout << L"Digite o nome do restaurante: ";
                getline (wcin, nome);
                wcout << L"Digite o endereço do restaurante: ";
                getline (wcin, endereco);
                wcout << L"Digite o tipo de comida do restaurante: ";
                getline (wcin, tipoComida);
                wcout << L"Digite a nota da cozinha do restaurante (entre 0 e 5): ";
                wcin >> notaCozinha;
                inserirRestaurante (&listaRestaurantes, nome, endereco, tipoComida, notaCozinha);
                wcout << L"Restaurante inserido com sucesso!" << endl;
                break;
            }

            // Listar todos os restaurantes
            case L'2':
                listarRestaurantes (listaRestaurantes);
                break;

            // Listar restaurantes por nota
            case L'3': {
                float notaMinima;
                wcout << L"Digite a nota mínima: ";
                wcin >> notaMinima;
                listarRestaurantesPorNota (listaRestaurantes, notaMinima);
                break;
            }

            // Listar restaurantes por tipo de comida
            case L'4': {
                wstring tipoComida;
                wcout << L"Digite o tipo de comida: ";
                getline (wcin, tipoComida);
                listarRestaurantesPorTipoComida (listaRestaurantes, tipoComida);
                break;
            }
            
            // Atualizar informações de um restaurante
            case L'5': {
                wstring nome, novoNome, endereco, tipoComida;
                float notaCozinha;
                wcout << L"Digite o nome do restaurante que deseja atualizar: ";
                getline (wcin, nome);

                // Verifica se o restaurante existe antes de solicitar as demais informações
                Restaurante* restauranteEncontrado = nullptr;
                Restaurante* atual = listaRestaurantes;
                while (atual != nullptr){
                    if (atual->nome == nome){
                        restauranteEncontrado = atual;
                        break;
                    }
                    atual = atual->proximo;
                }

                if (restauranteEncontrado != nullptr){
                    wcout << L"Digite o novo nome: ";
                    getline (wcin, novoNome);
                    wcout << L"Digite o novo endereço: ";
                    getline (wcin, endereco);
                    wcout << L"Digite o novo tipo de comida: ";
                    getline (wcin, tipoComida);
                    wcout << L"Digite a nova nota da cozinha (entre 0 e 5): ";
                    wcin >> notaCozinha;
                    atualizarRestaurante (&listaRestaurantes, nome, novoNome, endereco, tipoComida, notaCozinha);
                }
                else
                    wcout << L"Restaurante não encontrado." << endl;

                break;
            }

            // Deletar um restaurante cadastrado
            case L'6': {
                wstring nome;
                wcout << L"Digite o nome do restaurante que deseja deletar: ";
                getline (wcin, nome);
                deletarRestaurante (&listaRestaurantes, nome);
                break;
            }

            // Opção inválida
            default:
                wcout << L"Opção inválida. Tente novamente." << endl;
                break;
        }
        
        wcout << endl;
    }
    
    // Liberar a memória alocada dinamicamente para os restaurantes
    liberarLista (&listaRestaurantes);
    
    return 0;
}