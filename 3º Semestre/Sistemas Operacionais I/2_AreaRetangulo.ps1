#Um script que calcula a área de um retângulo e verifica se a área é maior,
#menor ou igual a 50. O usuário deve inserir a base e a altura do retângulo.

Clear-Host

#Classe WScript.Shell
$wshell = New-Object -com Wscript.Shell

#Recebe os números do usuário e calcula a área
[float]$base = Read-Host "Digite o valor da base do retângulo"
[float]$altura = Read-Host "Digite o valor da altura do retângulo"
[float]$area = $base*$altura

#Mostra um pop-up dizendo se a área é maior, menor ou igual a 50
if ($area -gt 50){
    $wshell.Popup("A área do retângulo ($area) é maior que 50.")
}

elseif ($area -lt 50){
    $wshell.Popup("A área do retângulo ($area) é menor que 50.")
}

else {
    $wshell.Popup("A área do retângulo ($area) é igual a 50.")
}