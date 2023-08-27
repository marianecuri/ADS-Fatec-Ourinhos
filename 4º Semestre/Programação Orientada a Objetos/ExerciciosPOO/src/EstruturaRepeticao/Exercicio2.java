// Fazer um programa para encontrar todos os pares entre 1 e 38.

package EstruturaRepeticao;

import javax.swing.JOptionPane;

public class Exercicio2
{
    public static void main(String args[])
    {
        StringBuilder numeros_pares = new StringBuilder();

        numeros_pares.append("Números pares entre 1 e 38:\n\n   ");

        for (int i = 2; i <= 38; i += 2) {
            if (i > 2)
                numeros_pares.append("    ");

            if (i % 20 == 0)
                numeros_pares.append("\n");

            numeros_pares.append(String.format("%02d", i));
        }

        JOptionPane.showMessageDialog(null, numeros_pares.toString());
    }

}