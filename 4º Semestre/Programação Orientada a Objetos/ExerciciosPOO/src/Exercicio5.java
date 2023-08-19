/*
*As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e
*R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia
*o número de maçãs compradas, calcule e escreva o custo total da compra.
*/

import javax.swing.JOptionPane;

public class Exercicio5 {
    public static void main(String args[]){
        int num_macas;
        
        num_macas = Integer.parseInt(JOptionPane.showInputDialog("Digite o número de maçãs compradas"));

        if (num_macas<12)
            JOptionPane.showMessageDialog(null, "Custo total da compra: R$ " + (num_macas * 1.30));
        
        
        else
            JOptionPane.showMessageDialog(null, "Custo total da compra: R$ " + num_macas);
        
    }
}