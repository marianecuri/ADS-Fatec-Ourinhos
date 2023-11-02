package Exercicio1;

import javax.swing.JOptionPane;

public class Pessoa {
    private String nome;
    private String sexo;
    private int idade;
    
    public Pessoa() {
        JOptionPane.showMessageDialog(null, "Construtor padrão de Pessoa");
    }
    
    public Pessoa(String nome, String sexo, int idade) {
        this.nome = nome;
        this.sexo = sexo;
        this.idade = idade;
        JOptionPane.showMessageDialog(null, "Construtor com todos os atributos de Pessoa");
    }
    
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getSexo() {
        return sexo;
    }

    public void setSexo(String sexo) {
        this.sexo = sexo;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }
    
}