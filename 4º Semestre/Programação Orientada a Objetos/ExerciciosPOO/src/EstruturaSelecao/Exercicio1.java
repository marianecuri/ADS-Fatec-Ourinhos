/*
* Faça um algoritmo para ler dois números inteiros
* e informar se estes são iguais ou diferentes.
*/

package EstruturaSelecao;

import javax.swing.JOptionPane;

public class Exercicio1
{
    public static void main(String args[])
    {
        int num1, num2;

        num1 = Integer.parseInt(JOptionPane.showInputDialog("Digite um número:"));
        num2 = Integer.parseInt(JOptionPane.showInputDialog("Digite outro número:"));

        if (num1 == num2)
            JOptionPane.showMessageDialog(null, "Os números são iguais.");
        
        else
            JOptionPane.showMessageDialog(null, "Os números são diferentes.");
    }

}