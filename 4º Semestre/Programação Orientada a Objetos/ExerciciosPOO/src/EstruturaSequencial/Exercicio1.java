/*
* Fazer um algoritmo que leia um número inteiro
* e escreva o seu antecessor e o seu sucessor.
*/

package EstruturaSequencial;

import javax.swing.JOptionPane;

public class Exercicio1
{
    public static void main(String args[])
    {
        int num;

        num = Integer.parseInt(JOptionPane.showInputDialog("Digite um número:"));

        JOptionPane.showMessageDialog(null, "Antecessor: " + (num - 1) + "\n" + "Sucessor: " + (num + 1));
    }

}