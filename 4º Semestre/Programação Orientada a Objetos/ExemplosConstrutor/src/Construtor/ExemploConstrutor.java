package Construtor;

import javax.swing.JOptionPane;

public class ExemploConstrutor {
    private String nome;
    private int idade;

    public ExemploConstrutor() {
        JOptionPane.showMessageDialog(null, "Construtor 1");
    }

    public ExemploConstrutor(String nome) {
        this.nome = nome;
        JOptionPane.showMessageDialog(null, "Construtor 2");
    }

    public ExemploConstrutor(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
        JOptionPane.showMessageDialog(null, "Construtor 3");
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }
    
}