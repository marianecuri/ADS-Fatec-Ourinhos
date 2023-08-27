// Exibir os números de 1 até 50 na tela.

package EstruturaRepeticao;

import javax.swing.JOptionPane;

public class Exercicio1
{
    public static void main(String args[])
    {
        StringBuilder numeros = new StringBuilder();

        numeros.append("Números de 1 a 50:\n");

        for (int i = 1; i <= 50; i++)
        {
            if (i > 1)
                numeros.append("    ");

            if (i % 10 == 1)
                numeros.append("\n");

            numeros.append(String.format("%02d", i));
        }

        JOptionPane.showMessageDialog(null, numeros.toString());
    }

}