/*
* Um posto está vendendo combustíveis com a seguinte tabela de descontos:
* Álcool: até 20 litros, desconto de 3% por litro / acima de 20 litros, desconto de 5% por litro.
* Gasolina: até 20 litros, desconto de 4% por litro / acima de 20 litros, desconto de 6% por litro.
* Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível
* (codificado da seguinte forma: 1-álcool, 2-gasolina), calcule e imprima o valor a ser pago pelo
* cliente sabendo-se que o preço do litro da gasolina é R$ 3,30 e o preço do litro do álcool é R$ 2,90.
*/

package EstruturaSelecao;

import javax.swing.JOptionPane;
import java.text.DecimalFormat;

public class Exercicio6 
{
    public static void main(String args[])
    {
        double litros, valor;
        int codigo;

        while (true)
        {
            litros = Integer.parseInt(JOptionPane.showInputDialog("Digite o número de litros vendidos:"));

            if (litros > 0)
            {
                while (true)
                {
                    codigo = Integer.parseInt(JOptionPane.showInputDialog("Selecione o tipo de combustível:\n(1) Álcool\n(2) Gasolina"));

                    switch (codigo)
                    {
                        case 1 ->
                        {
                            if (litros <= 20)
                                valor = (litros * 2.9) - (0.03 * 2.9 * litros);
                            
                            else
                                valor = (litros * 2.9) - (0.05 * 2.9 * litros);
                            
                            break;
                        }

                        case 2 ->
                        {
                            if (litros <= 20)
                                valor = (litros * 3.3) - (0.04 * 3.3 * litros);
                            
                            else
                                valor = (litros * 3.3) - (0.06 * 3.3 * litros);

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

            JOptionPane.showMessageDialog(null, "O número de litros deve ser maior que 0.");
        }

        DecimalFormat df = new DecimalFormat("#.00");
        JOptionPane.showMessageDialog(null, "Valor a ser pago: R$ " + df.format(valor));
    }

}