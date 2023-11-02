package associacaoheranca;

public class Contrato {
    private String data;
    private Imovel imovel;
    private Proprietario proprietario;
    private Inquilino inquilino;
    
    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }

    public Imovel getImovel() {
        return imovel;
    }

    public void setImovel(Imovel imovel) {
        this.imovel = imovel;
    }

    public Proprietario getProprietario() {
        return proprietario;
    }

    public void setProprietario(Proprietario proprietario) {
        this.proprietario = proprietario;
    }

    public Inquilino getInquilino() {
        return inquilino;
    }

    public void setInquilino(Inquilino inquilino) {
        this.inquilino = inquilino;
    }
    
}