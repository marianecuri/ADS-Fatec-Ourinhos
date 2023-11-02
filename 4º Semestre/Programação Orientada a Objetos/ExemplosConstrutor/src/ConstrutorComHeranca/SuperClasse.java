package ConstrutorComHeranca;

import javax.swing.JOptionPane;

public class SuperClasse {
    public SuperClasse() {
        JOptionPane.showMessageDialog(null, "Construtor 1 da SuperClasse");
    }

    public SuperClasse(String x) {
        JOptionPane.showMessageDialog(null, "Construtor 2 da SuperClasse");
    }

    public SuperClasse(String x, int a) {
        JOptionPane.showMessageDialog(null, "Construtor 3 da SuperClasse");
    }

}