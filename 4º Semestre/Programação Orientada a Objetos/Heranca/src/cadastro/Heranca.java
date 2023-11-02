package cadastro;

import javax.swing.JOptionPane;
import java.text.DecimalFormat;

public class Heranca {
    public static void main(String[] args) {
        DecimalFormat df = new DecimalFormat("#.00");
        int escolha = Integer.parseInt(JOptionPane.showInputDialog
        ("Escolha o tipo de usuário que deseja cadastrar:\n1. Empregado\n2. Cliente"));
        
        if(escolha == 1) {
            int escolha_emp = Integer.parseInt(JOptionPane.showInputDialog
            ("Escolha o tipo de empregado:\n1. Gerente\n2. Vendedor"));
         
            if(escolha_emp == 1) {
                Gerente g = new Gerente();
                
                String nome = JOptionPane.showInputDialog("Digite o nome do gerente:");
                g.setNome(nome);

                int idade = Integer.parseInt(JOptionPane.showInputDialog("Digite a idade do gerente:"));
                g.setIdade(idade);

                String sexo = JOptionPane.showInputDialog("Digite o sexo do gerente:");
                g.setSexo(sexo);
                
                double salario = Double.parseDouble(JOptionPane.showInputDialog("Digite o valor do salário do gerente:"));
                g.setSalario(salario);
                
                String matricula = JOptionPane.showInputDialog("Digite a matrícula do gerente:");
                g.setMatricula(matricula);
                
                String nomeGerencia = JOptionPane.showInputDialog("Digite o nome da gerência:");
                g.setNomeGerencia(nomeGerencia);
                
                
                JOptionPane.showMessageDialog
                (null, "Nome: " + g.getNome() +
                "\nIdade: " + g.getIdade() + " anos" +
                "\nSexo: " + g.getSexo() +
                "\nSalário: R$ " + df.format(g.getSalario()) +
                "\nMatrícula: " + g.getMatricula() +
                "\nNome da gerência: " + g.getNomeGerencia()); 
            }
            
            else if(escolha_emp == 2) {
                Vendedor v = new Vendedor();
                
                String nome = JOptionPane.showInputDialog("Digite o nome do vendedor:");
                v.setNome(nome);

                int idade = Integer.parseInt(JOptionPane.showInputDialog("Digite a idade do vendedor:"));
                v.setIdade(idade);

                String sexo = JOptionPane.showInputDialog("Digite o sexo do vendedor:");
                v.setSexo(sexo);
                
                double salario = Double.parseDouble(JOptionPane.showInputDialog("Digite o valor do salário do vendedor:"));
                v.setSalario(salario);
                
                String matricula = JOptionPane.showInputDialog("Digite a matrícula do vendedor:");
                v.setMatricula(matricula);
                
                double valorVendas = Double.parseDouble(JOptionPane.showInputDialog("Digite o valor de vendas do vendedor:"));
                v.setValorVendas(valorVendas);
                
                int qntVendas = Integer.parseInt(JOptionPane.showInputDialog("Digite a quantidade de vendas do vendedor:"));
                v.setQntVendas(qntVendas);
                
                
                JOptionPane.showMessageDialog
                (null, "Nome: " + v.getNome() +
                "\nIdade: " + v.getIdade() + " anos" +
                "\nSexo: " + v.getSexo() +
                "\nSalário: " + df.format(v.getSalario()) +
                "\nMatrícula: " + v.getMatricula() +
                "\nValor de vendas: R$ " + df.format(v.getValorVendas()) +
                "\nQuantidade de vendas: " + v.getQntVendas()); 
            }
            
        }
        
                
        else if(escolha == 2) {
            Cliente c = new Cliente();
            
            String nome = JOptionPane.showInputDialog("Digite o nome do cliente:");
            c.setNome(nome);
            
            int idade = Integer.parseInt(JOptionPane.showInputDialog("Digite a idade do cliente:"));
            c.setIdade(idade);
            
            String sexo = JOptionPane.showInputDialog("Digite o sexo do cliente:");
            c.setSexo(sexo);
            
            double valorDivida = Double.parseDouble(JOptionPane.showInputDialog("Digite o valor da dívida do cliente:"));
            c.setValorDivida(valorDivida);
            
            int anoNascim = Integer.parseInt(JOptionPane.showInputDialog("Digite o ano de nascimento do cliente:"));
            c.setAnoNascim(anoNascim);
            

            JOptionPane.showMessageDialog
            (null, "Nome: " + c.getNome() +
            "\nIdade: " + c.getIdade() + " anos" +
            "\nSexo: " + c.getSexo() +
            "\nValor da dívida: R$ " + df.format(c.getValorDivida()) +
            "\nAno de nascimento: " + c.getAnoNascim()); 
        }
        
    }
    
}