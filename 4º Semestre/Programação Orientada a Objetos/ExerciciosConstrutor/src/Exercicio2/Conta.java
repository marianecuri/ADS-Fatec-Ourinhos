package Exercicio2;

import javax.swing.JOptionPane;

public class Conta {
    private String agencia;
    private String numero;
    private double saldo;
    private String nomeCliente;
    
    public Conta() {
        JOptionPane.showMessageDialog(null, "Construtor padrão de Conta");
    }
    
    public Conta(String agencia, String numero, double saldo, String nomeCliente) {
        this.agencia = agencia;
        this.numero = numero;
        this.saldo = saldo;
        this.nomeCliente = nomeCliente;
        JOptionPane.showMessageDialog(null, "Construtor com todos os atributos de Conta");
    }
    
    public String getAgencia() {
        return agencia;
    }

    public void setAgencia(String agencia) {
        this.agencia = agencia;
    }

    public String getNumero() {
        return numero;
    }

    public void setNumero(String numero) {
        this.numero = numero;
    }

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public String getNomeCliente() {
        return nomeCliente;
    }

    public void setNomeCliente(String nomeCliente) {
        this.nomeCliente = nomeCliente;
    }
    
}