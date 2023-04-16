#Um script que script que l? tr?s números e mostra o maior deles.

Clear-Host

#Classe WScript.Shell
$wshell = New-Object -com Wscript.Shell

#Recebe os números do usuário
[float]$numero1 = Read-Host "Digite o primeiro número"
[float]$numero2 = Read-Host "Digite o segundo número"
[float]$numero3 = Read-Host "Digite o terceiro número"

#Executa o bloco de notas
$wshell.run("Notepad")

#Ativa o Notepad
$wshell.AppActivate("Notepad")

#Espera de 1s
Start-sleep 1

#Mostra o maior número no Notepad
if ($numero1 -ge $numero2 -and $numero1 -ge $numero3){
    $wshell.SendKeys("$numero1 eh o maior numero.")
}

elseif ($numero2 -ge $numero1 -and $numero2 -ge $numero3){
    $wshell.SendKeys("$numero2 eh o maior numero.")
}

else {
    $wshell.SendKeys("$numero3 eh o maior numero.")
}