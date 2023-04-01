<#
Um script que verifica se um número  é par ou ímpar.
Se for par, exibe "O número é par". Caso contrário, exibe "O número é ímpar".
#>

Clear-Host

#Classe WScript.Shell
$wshell = New-Object -com Wscript.Shell

#Recebe o número do usuário
[float]$numero = Read-Host "Digite um número"

#Verifica se o número é par ou ímpar e mostra um pop-up
if ($numero%2 -eq 0){
    $wshell.Popup("O numero $numero é par.")
}

else {
    $wshell.Popup("O numero $numero é ímpar.")
}