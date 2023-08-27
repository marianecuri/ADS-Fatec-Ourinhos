/*                                  
* Ler as notas da 1ª e 2ª avaliações de um aluno. Calcular a média
* aritmética simples e escrever uma mensagem que diga se o aluno foi
* ou não aprovado (considerar que nota igual ou maior que 6 o aluno é
* aprovado). Escrever também a média calculada.
*/

package EstruturaSelecao;

import javax.swing.JOptionPane;

public class Exercicio4
{
    public static void main(String args[])
    {
        double a1, a2, media;

        while (true)
        {
            a1 = Double.parseDouble(JOptionPane.showInputDialog("Digite a nota da avaliação 1:"));

            if (a1 >= 0 && a1 <= 10)
            {
                while (true)
                {
                    a2 = Double.parseDouble(JOptionPane.showInputDialog("Digite a nota da avaliação 2:"));

                    if (a2 >= 0 && a2 <= 10)
                    {
                        media = (a1 + a2) / 2;

                        if (media >= 6)
                            JOptionPane.showMessageDialog(null, "Média do aluno: " + media + "\nSituação: Aprovado!");
                        
                        else
                            JOptionPane.showMessageDialog(null, "Média do aluno: " + media + "\nSituação: Reprovado.");

                        break;
                    }

                    JOptionPane.showMessageDialog(null, "Nota inválida.");
                }

                break;
            }

            JOptionPane.showMessageDialog(null, "Nota inválida.");
        }

    }

}