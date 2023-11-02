package Construtor;

import javax.swing.JOptionPane;

public class ExecutaExemploConstrutor {
    public static void main(String[] args) {
        String nome = JOptionPane.showInputDialog("Nome");
        int idade = Integer.parseInt(JOptionPane.showInputDialog("Idade"));
        ExemploConstrutor e = new ExemploConstrutor();
    }

}