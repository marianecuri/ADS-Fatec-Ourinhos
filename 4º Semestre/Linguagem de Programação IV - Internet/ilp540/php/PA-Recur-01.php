<?php
printf("<html>\n");
printf("<body>\n");
$bloco = (ISSET($_REQUEST['bloco'])) ? $_REQUEST['bloco'] : '1';
switch (TRUE)
{
    case ($bloco == 1);
    {
        printf("<form action='./PA-Recur-01.php' method='POST'>\n");
        printf("<input type='hidden' name='bloco' value='2'>\n");
        printf("Nome: <input type='text' name='txnomemedico' size='40' maxlength='90'><br>\n");
        printf("Nascimento: <input type='date' name='dtnascmedico'><br>\n");
        printf("<input type='reset' value='Limpar'>\n");
        printf("<input type='submit' value='Enviar'>\n");
        printf("<button onclick='history.go(-1)'>Sair</button>\n");
        printf("</form>\n");
        break;
    }
    case ($bloco == 2):
    {
        printf("<pre>\n");
        print_r($_REQUEST);
        printf("</pre>\n");
        printf("<button onclick='history.go(-1)'>Voltar</button>\n");
        break;
    }
}
printf("</body>\n");
printf("</html>\n");
?>