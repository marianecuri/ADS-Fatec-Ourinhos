#Um script que imprime os números pares de 1 a 20.

Clear-Host

#Classe WScript.Shell
$wshell = New-Object -com Wscript.Shell

#Inicia a variável numero
[float]$numero = 1

#Executa o bloco de notas
$wshell.run("Notepad")

#Ativa o Notepad
$wshell.AppActivate("Notepad")

#Espera de 1s
Start-sleep 1

$wshell.SendKeys("Numeros pares de 1 a 20:`n`n")

do {

    if ($numero%2 -eq 0){
        $wshell.SendKeys("$numero`t")
    }

    $numero += 1

} while ($numero -le 20)