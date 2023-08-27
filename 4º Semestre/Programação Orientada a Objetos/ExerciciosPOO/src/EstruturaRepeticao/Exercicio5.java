/*
* Chico tem 1,50m e cresce 2 centímetros por ano, enquanto Juca tem 1,10m e
* cresce 3 centímetros por ano. Construir um algoritmo que calcule e imprima
* quantos anos serão necessários para que Juca seja maior que Chico. 
*/

package EstruturaRepeticao;

import javax.swing.JOptionPane;

public class Exercicio5
{
    public static void main(String[] args)
    {
        double Chico = 1.50, Juca = 1.10;
        int ano = 0;
        
        while (Juca < Chico)
        {
            Chico += 0.02;
            Juca += 0.03;
            ano++;
        }
        
        JOptionPane.showMessageDialog(null, "Serão necessários " + ano + " anos para que Juca seja maior que Chico.");
    }

}