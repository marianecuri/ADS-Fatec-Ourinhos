package Exercicio1;

import javax.swing.JOptionPane;

public class Executa {
    public static void main(String[] args) {
        Amigo a = new Amigo();

        a.setNome(JOptionPane.showInputDialog("Digite o nome do amigo:"));
        a.setSexo(JOptionPane.showInputDialog("Digite o sexo do amigo:"));
        a.setIdade(Integer.parseInt(JOptionPane.showInputDialog("Digite a idade do amigo:")));
        a.setDiaDoAniversario(JOptionPane.showInputDialog("Digite o dia do aniversário do amigo:"));

        JOptionPane.showMessageDialog(null, 
                "Nome: " + a.getNome() +
                "\nSexo: " + a.getSexo() +
                "\nIdade: " + a.getIdade() +
                "\nDia do Aniversário: " + a.getDiaDoAniversario());
    }

}