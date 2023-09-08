/*
* Crie uma classe para representar uma pessoa com os atributos privados:
* nome, ano de nascimento e altura. Crie os métodos necessários para acesso
* aos atributos (sets e gets) e um método para calcular a idade da pessoa,
* de acordo com o ano corrente (calcular sem se preocupar com data exata,
* somente considerar o ano). Preencha e exiba todos os dados, incluindo a idade atual.
*/

package Ex8;

import javax.swing.JOptionPane;

public class Principal {
    public static void main(String[] args) {
        Pessoa p = new Pessoa();
        String nome = JOptionPane.showInputDialog("Nome:");
        int ano = Integer.parseInt(JOptionPane.showInputDialog("Ano de nascimento:"));
        double altura = Double.parseDouble(JOptionPane.showInputDialog("Altura (m): "));
        int idade;

        p.setNome(nome);
        p.setAnoNascimento(ano);
        p.setAltura(altura);
        idade = 2023 - p.getAnoNascimento();
        
        JOptionPane.showMessageDialog(null, "Nome: " + p.getNome() + 
        "\nAno de nascimento: " + p.getAnoNascimento() + "\nIdade: " + idade +
        " anos\nAltura: " + p.getAltura() + " m");
    }
    
}