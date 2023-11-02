package Exercicio2;

import javax.swing.JOptionPane;

public class Poupanca extends Conta {
    private double rendimento;
    
    public Poupanca() {
        JOptionPane.showMessageDialog(null, "Construtor padrão de Poupanca");
    }
    
    public Poupanca(String agencia, String numero, double saldo, String nomeCliente, double rendimento) {
        super(agencia, numero, saldo, nomeCliente);
        this.rendimento = rendimento;
        JOptionPane.showMessageDialog(null, "Construtor com todos os atributos de Poupanca");
    }
    
    public double getRendimento() {
        return rendimento;
    }
    
    public void setRendimento (double rendimento) {
        this.rendimento = rendimento;
    }
    
}