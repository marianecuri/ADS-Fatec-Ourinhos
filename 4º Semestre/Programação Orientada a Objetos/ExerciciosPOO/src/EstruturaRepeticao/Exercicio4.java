/*
* Faça um algoritmo para ler o código e o preço de 15 produtos, calcular e escrever (não deve ser usado vetor):
* - o maior preço lido
* - a média aritmética dos preços dos produtos
*/

package EstruturaRepeticao;

import javax.swing.JOptionPane;
import java.text.DecimalFormat;

public class Exercicio4
{
    public static void main(String[] args)
    {
        double maior = 0.0, media = 0.0;

        for (int i = 1; i <= 15; i++)
        {
            String codigo = JOptionPane.showInputDialog("Digite o código do produto " + i + ": ");
            double preco = Double.parseDouble(JOptionPane.showInputDialog("Digite o preço do produto " + codigo + " (R$): "));

            if (preco > maior)
                maior = preco;

            media += preco;
        }
        
        media = media / 15;
        
        DecimalFormat df = new DecimalFormat("#.00");
        String maiorf = df.format(maior);
        String mediaf = df.format(media);
        
        JOptionPane.showMessageDialog(null, "Maior preço: R$ " + maiorf + "\nMédia dos preços dos produtos: R$ " + mediaf);
    }

}