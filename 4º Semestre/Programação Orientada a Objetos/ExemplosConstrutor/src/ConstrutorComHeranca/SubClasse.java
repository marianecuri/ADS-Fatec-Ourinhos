package ConstrutorComHeranca;

import javax.swing.JOptionPane;

public class SubClasse extends SuperClasse {
    public SubClasse() {
        super("", 0);
        JOptionPane.showMessageDialog(null, "Construtor da SubClasse");
    }

}