package associacaoheranca;

public class Proprietario extends Pessoa {
    private String conjuge;

    public String getConjuge() {
        return conjuge;
    }

    public void setConjuge(String conjuge) {
        this.conjuge = conjuge;
    }
    
}