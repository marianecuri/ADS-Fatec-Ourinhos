package Ex8;

public class Pessoa {
    private String nome;
    private int ano;
    private double altura;

    public void setNome(String n) {
        nome = n;
    }
    public String getNome() {
        return nome;
    }

    public void setAnoNascimento(int an) {
        ano = an;
    }
    public int getAnoNascimento() {
        return ano;
    }
    
    public void setAltura(double a) {
        altura = a;
    }
    public double getAltura() {
        return altura;
    }
    
}