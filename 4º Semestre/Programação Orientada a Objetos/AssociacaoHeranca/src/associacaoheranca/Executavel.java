package associacaoheranca;

import javax.swing.JOptionPane;
import java.text.DecimalFormat;

public class Executavel {

    public static void main(String[] args) {
        DecimalFormat df = new DecimalFormat("#.00");
        
        // Criando um inquilino
        Inquilino inquilino = new Inquilino();
        inquilino.setNome(JOptionPane.showInputDialog("Digite o nome do(a) inquilino(a):"));
        inquilino.setCpf(JOptionPane.showInputDialog("Digite o CPF do(a) inquilino(a):"));
        inquilino.setRenda(Double.parseDouble(JOptionPane.showInputDialog("Digite a renda do(a) inquilino(a):")));
        inquilino.setProfissao(JOptionPane.showInputDialog("Digite a profissão do(a) inquilino(a):"));

        // Criando um proprietario
        Proprietario proprietario = new Proprietario();
        proprietario.setNome(JOptionPane.showInputDialog("Digite o nome do(a) proprietário(a):"));
        proprietario.setCpf(JOptionPane.showInputDialog("Digite o CPF do(a) proprietário(a):"));
        proprietario.setConjuge(JOptionPane.showInputDialog("Digite o nome do(a) cônjuge do(a) proprietário(a):"));

        // Criando um endereco
        Endereco endereco = new Endereco();
        endereco.setRua(JOptionPane.showInputDialog("Digite o nome da rua:"));
        endereco.setNumero(JOptionPane.showInputDialog("Digite o número:"));
        endereco.setBairro(JOptionPane.showInputDialog("Digite o bairro:"));
        endereco.setCidade(JOptionPane.showInputDialog("Digite a cidade:"));

        // Criando um imovel
        Imovel imovel = new Imovel();
        imovel.setEndereco(endereco);
        imovel.setValor(Double.parseDouble(JOptionPane.showInputDialog("Digite o valor do imóvel:")));

        // Criando um contrato
        Contrato contrato = new Contrato();
        contrato.setData(JOptionPane.showInputDialog("Digite a data do contrato:"));
        contrato.setImovel(imovel);
        contrato.setProprietario(proprietario);
        contrato.setInquilino(inquilino);

        // Exibindo os dados do contrato
        JOptionPane.showMessageDialog(null, "Dados do contrato:" +
                
        "\n\nData: " + contrato.getData() +
                
        "\n\nEndereço do imóvel: " +
        contrato.getImovel().getEndereco().getRua() + ", " +
        contrato.getImovel().getEndereco().getNumero() + ", " +
        contrato.getImovel().getEndereco().getBairro() + ", " +
        contrato.getImovel().getEndereco().getCidade() +
        "\nValor do imóvel: R$ " + df.format(contrato.getImovel().getValor()) +
                
        "\n\nNome do(a) proprietário(a): " + contrato.getProprietario().getNome() +
        "\nCpf do(a) proprietário(a): " + contrato.getProprietario().getCpf() +
        "\nCônjuge do(a) proprietário(a): " + contrato.getProprietario().getConjuge() +
                
        "\n\nNome do(a) inquilino(a): " + contrato.getInquilino().getNome() +
        "\nCpf do(a) inquilino(a): " + contrato.getInquilino().getCpf() +
        "\nRenda do(a) inquilino(a): R$ " + df.format(contrato.getInquilino().getRenda()) +
        "\nProfissão do(a) inquilino(a): " + contrato.getInquilino().getProfissao());
        
    }
    
}