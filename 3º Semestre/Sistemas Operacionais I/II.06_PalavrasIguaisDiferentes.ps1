#Um script que solicita ao usuário duas palavras e verifica se elas são iguais ou diferentes.

Clear-Host

#Classe WScript.Shell
$wshell = New-Object -com Wscript.Shell

#Recebe as palavras do usuário
[string]$palavra1 = Read-Host "Digite uma palavra"
[string]$palavra2 = Read-Host "Digite outra palavra"

#Executa o bloco de notas
$wshell.run("Notepad")

#Ativa o Notepad
$wshell.AppActivate("Notepad")

#Espera de 1s
Start-sleep 1

#Verifica se as palavras são iguais e exibe uma mensagem no Notepad
if ($palavra1 -eq $palavra2){
    $wshell.SendKeys("A palavras sao iguais.")
}

else {
    $wshell.SendKeys("As palavras sao diferentes.")
}