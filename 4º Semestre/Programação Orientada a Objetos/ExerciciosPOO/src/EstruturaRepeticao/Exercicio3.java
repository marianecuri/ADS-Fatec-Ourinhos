/* Ler 2 valores, calcular e escrever a soma dos inteiros existentes entre os 2
* valores lidos (incluindo os valores lidos na soma). Considere que o segundo
* valor lido será sempre maior que o primeiro valor lido. 
*/

package EstruturaRepeticao;

import javax.swing.JOptionPane;

public class Exercicio3
{
    public static void main(String args[])
    {
        int num1, num2, soma = 0;

        num1 = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite o primeiro valor:"));

        while (true)
        {
            num2 = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite o segundo valor:"));

            if (num2 > num1)
            {
                for (int i = num1; i <= num2; i++)
                    soma += i;

                JOptionPane.showMessageDialog(null, "Soma dos inteiros existentes entre " + num1 + " e " + num2 + " = " + soma);

                break;
            }

            JOptionPane.showMessageDialog(null, "O segundo valor deve ser maior que o primeiro.");
        }

    }

}