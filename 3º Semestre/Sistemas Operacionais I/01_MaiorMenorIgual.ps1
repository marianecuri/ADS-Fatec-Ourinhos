#Um script que solicita ao usuário 2 números e retorna se o
#primeiro número é maior, menor ou igual ao segundo número.

Clear-Host

#Classe WScript.Shell
$wshell = New-Object -com Wscript.Shell

#Recebe os números do usuário
[float]$numero1 = Read-Host "Digite um número"
[float]$numero2 = Read-Host "Digite outro número"

#Mostra um pop-up dizendo se o número é maior, menor ou igual
if ($numero1 -gt $numero2){
    $wshell.Popup("$numero1 é maior que $numero2.")
}

elseif ($numero1 -lt $numero2){
    $wshell.Popup("$numero1 é menor que $numero2.")
}

else {
    $wshell.Popup("$numero1 é igual a $numero2.")
}