#Um script que solicita ao usuário um número e verifica se ele é positivo, negativo ou igual a zero.

Clear-Host

#Classe WScript.Shell
$wshell = New-Object -com Wscript.Shell

#Recebe o número do usuário
[float]$numero = Read-Host "Digite um número"

#Mostra um pop-up dizendo se o número é positivo, negativo ou neutro
if ($numero -gt 0){
    $wshell.Popup("$numero é um número positivo.")
}

elseif ($numero -lt 0){
    $wshell.Popup("$numero é um número negativo.")
}

else {
    $wshell.Popup("$numero é um número neutro (igual a zero).")
}