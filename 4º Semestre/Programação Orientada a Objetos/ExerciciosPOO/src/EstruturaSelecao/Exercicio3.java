/*
* Uma loja fornece 10% de desconto para funcionários e 5% de desconto para clientes
* vips. Faça um programa que calcule o valor total a ser pago por uma pessoa. O programa
* deverá ler o valor total da compra efetuada e um código que identifique se o comprador
* é um cliente comum (1), funcionário (2) ou vip (3).
*/

package EstruturaSelecao;

import javax.swing.JOptionPane;
import java.text.DecimalFormat;

public class Exercicio3
{
    public static void main(String args[])
    {
        double total_compra, total_final;
        int codigo;

        while (true)
        {
            total_compra = Double.parseDouble(JOptionPane.showInputDialog("Digite o valor total da compra (R$):"));

            if (total_compra > 0)
            {
                while (true)
                {
                    codigo = Integer.parseInt(JOptionPane.showInputDialog("Selecione o tipo de cliente:\n(1) Cliente comum\n(2) Funcionário\n(3) Vip"));

                    switch (codigo)
                    {
                        case 1 ->
                        {
                            total_final = total_compra;
                            break;
                        }

                        case 2 ->
                        {
                            total_final = total_compra - (total_compra * 0.1);
                            break;
                        }

                        case 3 ->
                        {
                            total_final = total_compra - (total_compra * 0.05);
                            break;
                        }

                        default ->
                        {
                            JOptionPane.showMessageDialog(null, "Código inválido.");
                            continue;
                        }

                    }

                    break;
                }

                break;
            }

            JOptionPane.showMessageDialog(null, "Valor inválido.");
        }

        DecimalFormat df = new DecimalFormat("#.00");
        String total_finalf = df.format(total_final);

        JOptionPane.showMessageDialog(null, "O valor total a ser pago é: R$ " + total_finalf);
    }

}