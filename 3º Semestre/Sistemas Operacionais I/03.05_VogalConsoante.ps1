#Um script que verifica se uma letra digitada é vogal ou consoante.

Clear-Host

#Classe WScript.Shell
$wshell = New-Object -com Wscript.Shell

#Recebe a letra do usuário
[string]$letra = Read-Host "Digite uma letra"

#Executa o bloco de notas
$wshell.run("Notepad")

#Ativa o Notepad
$wshell.AppActivate("Notepad")

#Espera de 1s
Start-sleep 1

#Mostra uma mensagem no Notepad dizendo se a letra é vogal ou consoante
if ($letra -eq "A" -or $letra -eq "E" -or $letra -eq "I" -or $letra -eq "O" -or $letra -eq "U"){
    $wshell.SendKeys("$letra => Vogal.")
}

else {
    $wshell.SendKeys("$letra => Consoante.")
}