<?php
printf("<html>
    <link rel='stylesheet' href='estilos.css'>
    <meta charset='UTF-8'>
    <head>
    <title>Tratador</title>
    </head>
    <body>");
printf("Mostrando todos os valores do vetor de uma vez:\n");
printf("<pre>\n");
print_r($_REQUEST);
printf("</pre>\n");
printf("</body></html>");
?>