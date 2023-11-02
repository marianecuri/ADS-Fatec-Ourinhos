package Exercicio1;

import javax.swing.JOptionPane;

public class Amigo extends Pessoa {
    private String diaDoAniversario;
    
    public Amigo() {
        JOptionPane.showMessageDialog(null, "Construtor padrão de Amigo");
    }
    
    public Amigo(String nome, String sexo, int idade, String diaDoAniversario) {
        super(nome, sexo, idade);
        this.diaDoAniversario = diaDoAniversario;
        JOptionPane.showMessageDialog(null, "Construtor com todos os atributos de Amigo");
    }

    public String getDiaDoAniversario() {
        return diaDoAniversario;
    }

    public void setDiaDoAniversario(String diaDoAniversario) {
        this.diaDoAniversario = diaDoAniversario;
    }
    
}