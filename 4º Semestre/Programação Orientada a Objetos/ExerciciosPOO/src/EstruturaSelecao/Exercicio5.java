/*
* Elabore um algoritmo que dada a idade de um nadador classifica-o em uma das seguintes categorias: 
* infantil A = 5-7 anos 
* infantil B = 8-10 anos 
* juvenil A = 11-13 anos 
* juvenil B = 14-17 anos 
* adulto = maiores de 18 anos
*/

package EstruturaSelecao;

import javax.swing.JOptionPane;

public class Exercicio5
{
    public static void main(String args[])
    {
        int idade;

        while (true)
        {
            idade = Integer.parseInt(JOptionPane.showInputDialog("Digite a idade do nadador:"));

            if (idade >= 5)
            {
                if (idade <= 7)
                    JOptionPane.showMessageDialog(null, "Categoria: Infantil A.");
                
                else if (idade <= 10)
                    JOptionPane.showMessageDialog(null, "Categoria: Infantil B.");
                
                else if (idade <= 13)
                    JOptionPane.showMessageDialog(null, "Categoria: Juvenil A.");
                
                else if (idade <= 17)
                    JOptionPane.showMessageDialog(null, "Categoria: Juvenil B.");
                
                else
                    JOptionPane.showMessageDialog(null, "Categoria: Adulto.");

                break;
            }

            JOptionPane.showMessageDialog(null, "A idade mínima é de 5 anos.");
        }

    }

}