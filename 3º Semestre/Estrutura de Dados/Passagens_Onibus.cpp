#include <iostream>
#include <iomanip>
#include <cstring>
#include <clocale>
using namespace std;

int distancia_cidades (int, int);
float valor_passagem (int, int);

typedef struct {
    wchar_t cidades[50];
    wchar_t poltrona[15];
    wchar_t horario[5];
} Passagem;

int main (){
    setlocale (LC_ALL, "Portuguese");   // Define a localidade
    Passagem onibus[16];                // Cria um vetor de 15 elementos
    int origem, destino, tipo_poltrona, num_poltrona, dia, mes, horario, distancia;
    float valor;

    // Atribui os nomes das cidades
    wcscpy (onibus[1].cidades, L"Assis");
    wcscpy (onibus[2].cidades, L"Campos Novos Paulista");
    wcscpy (onibus[3].cidades, L"Cândido Mota");
    wcscpy (onibus[4].cidades, L"Canitar");
    wcscpy (onibus[5].cidades, L"Chavantes");
    wcscpy (onibus[6].cidades, L"Ibirarema");
    wcscpy (onibus[7].cidades, L"Ipaussu");
    wcscpy (onibus[8].cidades, L"Ocauçu");
    wcscpy (onibus[9].cidades, L"Ourinhos");
    wcscpy (onibus[10].cidades, L"Palmital");
    wcscpy (onibus[11].cidades, L"Platina");
    wcscpy (onibus[12].cidades, L"Ribeirão do Sul");
    wcscpy (onibus[13].cidades, L"Salto Grande");
    wcscpy (onibus[14].cidades, L"Santa Cruz do Rio Pardo");
    wcscpy (onibus[15].cidades, L"São Pedro do Turvo");

    // Imprime na tela um menu contendo as cidades
    wcout << L"Lista de cidades:" << endl;
    for (int i=1; i<=15; i++){
        wcout << L"[" << i << L"] " << onibus[i].cidades << endl;
    }

    // Pede ao usuário a cidade de origem
    wcout << L"\nDigite o número da sua cidade de origem (01-15): ";
    while (wcin >> origem){
        if (origem<1 or origem>15)
            wcout << L"Número inválido. Digite noveamente: ";

        else
            break;
    }

    // Pede ao usuário a cidade de destino
    wcout << L"Digite o número da sua cidade de destino (01-15): ";
    while (wcin >> destino){
        if (destino<1 or destino>15)
            wcout << L"Número inválido. Digite noveamente: ";

        else if (destino==origem)
            wcout << L"O destino e a origem não podem ser iguais. Digite noveamente: ";

        else
            break;
    }

    // Atribui os tipos de poltronas
    wcscpy (onibus[1].poltrona, L"Convencional");
    wcscpy (onibus[2].poltrona, L"Executivo");
    wcscpy (onibus[3].poltrona, L"Semi-leito");
    wcscpy (onibus[4].poltrona, L"Leito");
    wcscpy (onibus[5].poltrona, L"Leito-cama");

    // Imprime na tela um menu contendo as poltronas
    wcout << L"\nTipos de poltronas:" << endl;
    for (int i=1; i<=5; i++){
        wcout << L"[" << i << L"] " << onibus[i].poltrona << endl;
    }

    // Pede ao usuário o tipo de poltrona
    wcout << L"\nDigite o número do tipo de poltrona (01-05): ";
    while (wcin >> tipo_poltrona){
        if (tipo_poltrona<1 or tipo_poltrona>5)
            wcout << L"Numero inválido. Digite noveamente: ";

        else
            break;
    }

    // Pede ao usuário o número da poltrona
    wcout << L"Digite o número da poltrona desejada (01-40): ";
    while (wcin >> num_poltrona){
        if (num_poltrona<1 or num_poltrona>40)
            wcout << L"Numero inválido. Digite noveamente: ";

        else
            break;
    }

    // Pede ao usuário o dia da viagem
    wcout << L"\nDigite o dia da viagem (01-31): ";
    while (wcin >> dia){
        if (dia<1 or dia>31)
            wcout << L"Dia inválido. Digite noveamente: ";

        else
            break;
    }

    // Pede ao usuário o mês da viagem
    wcout << L"Digite o mês da viagem (01-12): ";
    while (wcin >> mes){
        if (mes<1 or mes>12)
            wcout << L"Mês inválido. Digite noveamente: ";

        else
            break;
    }

    // Atribui os horários
    wcscpy (onibus[1].horario, L"6h");
    wcscpy (onibus[2].horario, L"7h");
    wcscpy (onibus[3].horario, L"8h");
    wcscpy (onibus[4].horario, L"9h");
    wcscpy (onibus[5].horario, L"10h");
    wcscpy (onibus[6].horario, L"11h");
    wcscpy (onibus[7].horario, L"12h");
    wcscpy (onibus[8].horario, L"13h");
    wcscpy (onibus[9].horario, L"14h");
    wcscpy (onibus[10].horario, L"15h");
    wcscpy (onibus[11].horario, L"16h");
    wcscpy (onibus[12].horario, L"17h");
    wcscpy (onibus[13].horario, L"18h");

    // Imprime na tela um menu contendo os horários de saída
    wcout << L"\nHorários de saída:" << endl;
    for (int i=1; i<=13; i++){
        wcout << L"[" << i << L"] " << onibus[i].horario << endl;
    }

    // Pede ao usuário o horário de saída
    wcout << L"\nDigite o número do horário de saída (01-13): ";
    while (wcin >> horario){
        if (horario<1 or horario>13)
            wcout << L"Numero inválido. Digite noveamente: ";

        else
            break;
    }

    // Atribui o valor da passagem
    distancia = distancia_cidades (origem, destino);
    valor = valor_passagem (tipo_poltrona, distancia);
    
    // Altera a precisão para 2 casas decimais
    wcout.precision(2);
    wcout << fixed;

    // Imprime na tela as informações da passagem escolhida
    wcout << L"\nInformações da passagem:" << endl;
    wcout << L"Origem: " << onibus[origem].cidades << endl;
    wcout << L"Destino: " << onibus[destino].cidades << endl;
    wcout << L"Data: ";
    cout << setfill('0') << setw(2) << dia;
    wcout << "/";
    cout << setfill('0') << setw(2) << mes;
    wcout << L"/23";
    wcout << L"   |   Horário: " << onibus[horario].horario << endl;
    wcout << L"Poltrona: ";
    cout << setfill('0') << setw(2) << num_poltrona;
    wcout << L"     |   Tipo: " << onibus[tipo_poltrona].poltrona << endl;
    wcout << L"Valor: R$ " << valor << endl;

    return 0;
}


int distancia_cidades (int origem, int destino){
    int distancias[15][15] = {
        // A  CN  CM  Ca  Ch  Ib   Ip   Oc  Ou  Pa  Pl  RS  SG  SC  SP
        {  0, 68, 11, 86, 91, 44, 100, 100, 73, 33, 23, 68, 58, 99, 97},  // Assis
        { 68,  0, 62, 68, 73, 26,  82,  34, 55, 45, 26, 24, 40, 78, 57},  // Campos Novos Paulista
        { 11, 62,  0, 79, 85, 38,  94,  95, 67, 27, 30, 62, 52, 93, 90},  // Cândido Mota
        { 86, 68, 79,  0, 10, 41,  19,  72, 11, 60, 70, 38, 28, 34, 44},  // Canitar
        { 91, 73, 85, 10,  0, 49,  11,  81, 19, 68, 78, 46, 36, 32, 52},  // Chavantes
        { 44, 26, 38, 41, 49,  0,  58,  50, 31, 21, 32, 26, 16, 57, 54},  // Ibirarema
        {100, 82, 94, 19, 11, 58,   0,  90, 28, 77, 87, 55, 45, 19, 47},  // Ipaussu
        {100, 34, 95, 72, 81, 50,  90,   0, 63, 77, 87, 43, 59, 90, 64},  // Ocauçu
        { 73, 55, 67, 11, 19, 31,  28,  62,  0, 51, 62, 30, 20, 34, 39},  // Ourinhos
        { 33, 45, 27, 60, 68, 21,  77,  77, 51,  0, 21, 45, 35, 75, 73},  // Palmital
        { 23, 26, 30, 70, 78, 32,  87,  87, 62, 21,  0, 56, 46, 86, 84},  // Platina
        { 68, 24, 62, 38, 46, 26,  55,  43, 30, 45, 56,  0, 15, 52, 30},  // Ribeirão do Sul
        { 58, 40, 52, 28, 36, 16,  45,  59, 20, 35, 46, 15,  0, 45, 43},  // Salto Grande
        { 99, 78, 93, 34, 32, 57,  19,  90, 34, 75, 86, 52, 45,  0, 22},  // Santa Cruz do Rio Pardo
        { 97, 57, 90, 44, 52, 54,  47,  64, 39, 73, 84, 30, 43, 22,  0}   // São Pedro do Turvo
    };

    return distancias[origem-1][destino-1];
}


float valor_passagem (int poltrona, int distancia){
    float valor;

    if (poltrona==1)                       // Convencional
        valor = 0.23333*distancia;

    else if (poltrona==2)                  // Executivo
        valor = 0.29166*distancia;

    else if (poltrona==3)                  // Semi-leito
        valor = 0.34999*distancia;

    else if (poltrona==4)                  // Leito
        valor = 0.40832*distancia;

    else                                   // Leito-cama
        valor = 0.52499*distancia;

    return valor;
}