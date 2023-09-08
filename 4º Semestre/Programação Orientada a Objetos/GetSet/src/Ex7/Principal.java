/*
* Crie uma classe para representar um cliente de uma academia. Defina 4 possíveis
* atributos e implemente os métodos getters e setters. Criar o main para testar.
*/

package Ex7;

import javax.swing.JOptionPane;

public class Principal {
    public static void main(String[] args) {
        Cliente c = new Cliente();
        String nome = JOptionPane.showInputDialog("Nome:");
        String telefone = JOptionPane.showInputDialog("Telefone:");
        int idade = Integer.parseInt(JOptionPane.showInputDialog("Idade:"));
        double peso = Double.parseDouble(JOptionPane.showInputDialog("Peso (kg):"));

        c.setNome(nome);
        c.setTelefone(telefone);
        c.setIdade(idade);
        c.setPeso(peso);
        
        JOptionPane.showMessageDialog(null, "Nome: " + c.getNome() + 
        "\nTelefone: " + c.getTelefone() + "\nIdade: " + c.getIdade() +
        " anos\nPeso: " + c.getPeso() + " kg");
    }
    
}