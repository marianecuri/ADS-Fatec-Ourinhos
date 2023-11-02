package Exercicio2;

import javax.swing.JOptionPane;

public class Cliente {
    private String nome;
    private String endereco;
    private String rg;
    private String telefone;
    
    public Cliente() {
        JOptionPane.showMessageDialog(null, "Construtor padrão de Cliente");
    }
    
    public Cliente(String nome, String endereco, String rg, String telefone) {
        this.nome = nome;
        this.endereco = endereco;
        this.rg = rg;
        this.telefone = telefone;
        JOptionPane.showMessageDialog(null, "Construtor com todos os atributos de Cliente");
    }
    
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getEndereco() {
        return endereco;
    }

    public void setEndereco(String endereco) {
        this.endereco = endereco;
    }

    public String getRg() {
        return rg;
    }

    public void setRg(String rg) {
        this.rg = rg;
    }

    public String getTelefone() {
        return telefone;
    }

    public void setTelefone(String telefone) {
        this.telefone = telefone;
    }
    
}