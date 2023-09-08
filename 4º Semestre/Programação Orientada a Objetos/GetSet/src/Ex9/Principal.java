/*
* Crie uma classe para representar um jogador de futebol com os atributos nome, posição,
* nacionalidade, altura e peso. Crie os métodos getters e setters. Preencha os dados e exiba-os.
*/

package Ex9;

import javax.swing.JOptionPane;

public class Principal {
    public static void main(String[] args) {
        Jogador j = new Jogador();
        String nome = JOptionPane.showInputDialog("Nome:");
        String posicao = JOptionPane.showInputDialog("Posição:");
        String nacionalidade = JOptionPane.showInputDialog("Nacionalidade:");
        double altura = Double.parseDouble(JOptionPane.showInputDialog("Altura (m): "));
        double peso = Double.parseDouble(JOptionPane.showInputDialog("Peso (kg): "));

        j.setNome(nome);
        j.setPosicao(posicao);
        j.setNacionalidade(nacionalidade);
        j.setAltura(altura);
        j.setPeso(peso);
        
        JOptionPane.showMessageDialog(null, "Nome: " + j.getNome() + 
        "\nPosição: " + j.getPosicao() + "\nNacionalidade: " + j.getNacionalidade() +
        "\nAltura: " + j.getAltura() + " m\nPeso: " + j.getPeso() + " kg");
    }
    
}