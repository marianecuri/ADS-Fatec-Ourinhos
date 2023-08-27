/*
* Entrar com um número inteiro positivo e exibir o fatorial deste número,
* lembrando que 0! = 1. Exemplo: 5! = 5x4x3x2x1 = 120
*/

package EstruturaRepeticao;

import javax.swing.JOptionPane;

public class Exercicio6
{
    public static void main(String[] args)
    {
        int numero, fatorial = 1;
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite um número inteiro positivo:"));
        
        for (int i = 2; i <= numero; i++)
            fatorial *= i;

        JOptionPane.showMessageDialog(null, numero + "! = " + fatorial);
    }

}