package Exercicio2;

import javax.swing.JOptionPane;

public class ContaCorrente extends Conta {
    private double limite;
    
    public ContaCorrente() {
        JOptionPane.showMessageDialog(null, "Construtor padrão de ContaCorrente");
    }
    
    public ContaCorrente(String agencia, String numero, double saldo, String nomeCliente, double limite) {
        super(agencia, numero, saldo, nomeCliente);
        this.limite = limite;
        JOptionPane.showMessageDialog(null, "Construtor com todos os atributos de ContaCorrente");
    }
    
    public double getLimite() {
        return limite;
    }
    
    public void setLimite (double limite) {
        this.limite = limite;
    }
    
}