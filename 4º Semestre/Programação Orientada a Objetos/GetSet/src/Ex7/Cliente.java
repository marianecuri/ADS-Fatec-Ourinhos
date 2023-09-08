package Ex7;

public class Cliente {
    private String nome;
    private int idade;
    private String telefone;
    private double peso;

    public void setNome(String n) {
        nome = n;
    }
    public String getNome() {
        return nome;
    }

    public void setIdade(int i) {
        idade = i;
    }
    public int getIdade() {
        return idade;
    }
    
    public void setTelefone(String t) {
        telefone = t;
    }
    public String getTelefone() {
        return telefone;
    }
    
    public void setPeso(double p) {
        peso = p;
    }
    public double getPeso() {
        return peso;
    }
    
}