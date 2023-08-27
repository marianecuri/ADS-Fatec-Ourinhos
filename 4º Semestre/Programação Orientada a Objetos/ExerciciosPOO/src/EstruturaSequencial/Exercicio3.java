/*
* O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem 
* do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual
* do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo
* de fábrica de um carro, calcular e escrever o custo final ao consumidor.
*/

package EstruturaSequencial;

import javax.swing.JOptionPane;
import java.text.DecimalFormat;

public class Exercicio3
{
    public static void main(String args[])
    {
        double custo_fabrica, custo_final;

        custo_fabrica = Double.parseDouble(JOptionPane.showInputDialog("Digite o custo de fábrica (R$):"));
        custo_final = custo_fabrica + (custo_fabrica * 0.28) + (custo_fabrica * 0.45);

        DecimalFormat df = new DecimalFormat("#.00");
        String custo_finalf = df.format(custo_final);

        JOptionPane.showMessageDialog(null, "Custo final do carro: R$ " + custo_finalf);
    }

}