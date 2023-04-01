#Um script que pede um valor e mostra na tela se o valor é positivo ou negativo.

Clear-Host

#Classe WScript.Shell
$wshell = New-Object -com Wscript.Shell

#Recebe o número do usuário
[float]$numero = Read-Host "Digite um número"

#Executa o bloco de notas
$wshell.run("Notepad")

#Ativa o Notepad
$wshell.AppActivate("Notepad")

#Espera de 1s
Start-sleep 1

#Verifica se o número é positivo ou negativo e mostra um pop-up
if ($numero -gt 0){
    $wshell.SendKeys("$numero eh um numero positivo.")
}

elseif ($numero -lt 0){
    $wshell.SendKeys("$numero eh um numero negativo.")
}

else {
    $wshell.SendKeys("$numero eh um numero neutro.")
}