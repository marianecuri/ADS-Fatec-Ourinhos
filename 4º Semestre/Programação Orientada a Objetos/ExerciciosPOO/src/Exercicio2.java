/*
*Ler uma medida em polegadas e imprimir a equivalente em
*centímetros, sabendo que 2.54 cm equivale a 1 polegada.
*/

import javax.swing.JOptionPane;

public class Exercicio2 {
    public static void main(String args[]){
        double medida;
        
        medida = Double.parseDouble(JOptionPane.showInputDialog("Digite uma medida em polegadas"));
        
        JOptionPane.showMessageDialog(null, "Medida em centímetros: " + (medida*2.54));
        
    }
}