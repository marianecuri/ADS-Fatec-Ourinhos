#Um script que solicita ao usuário um número e
#verifica se ele é um número positivo e par.

Clear-Host

#Classe WScript.Shell
$wshell = New-Object -com Wscript.Shell

#Recebe o número do usuário
[float]$numero = Read-Host "Digite um número"

#Verifica se o número é positivo e par e mostra um pop-up
if ($numero -gt 0 -and ($numero%2) -eq 0){
    $wshell.Popup("$numero é um número positivo e par.")
}

elseif ($numero -gt 0 -and ($numero%2) -ne 0){
    $wshell.Popup("$numero é um número positivo, mas não é par.")
}

elseif ($numero -le 0 -and ($numero%2) -eq 0){
    $wshell.Popup("$numero não é um número positivo, mas é par.")
}

else {
    $wshell.Popup("$numero não é um número positivo e nem par.")
}