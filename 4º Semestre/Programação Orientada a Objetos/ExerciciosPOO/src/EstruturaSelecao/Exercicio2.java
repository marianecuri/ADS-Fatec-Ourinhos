/*
* As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e
* R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia
* o número de maçãs compradas, calcule e escreva o custo total da compra.
*/

package EstruturaSelecao;

import javax.swing.JOptionPane;
import java.text.DecimalFormat;

public class Exercicio2
{
    public static void main(String args[])
    {
        int num_macas;
        double custo_total;

        while (true)
        {
            num_macas = Integer.parseInt(JOptionPane.showInputDialog("Digite o número de maçãs compradas:"));

            if (num_macas > 0)
            {
                if (num_macas < 12)
                    custo_total = num_macas * 1.30;
                
                else
                    custo_total = num_macas;

                break;
            }

            JOptionPane.showMessageDialog(null, "Valor inválido.");
        }

        DecimalFormat df = new DecimalFormat("#.00");
        JOptionPane.showMessageDialog(null, "Custo total da compra: R$ " + df.format(custo_total));
    }

}
