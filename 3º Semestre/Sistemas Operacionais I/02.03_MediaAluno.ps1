<#
Um script que calcula a média aritmética de três notas de um aluno
e retorna se o aluno foi aprovado, reprovado ou está de recuperação.
#>

Clear-Host

#Classe WScript.Shell
$wshell = New-Object -com Wscript.Shell

#Recebe as notas do usuário e calcula a média
[float]$nota1 = Read-Host "Digite a nota 1"
[float]$nota2 = Read-Host "Digite a nota 2"
[float]$nota3 = Read-Host "Digite a nota 3"
[float]$media = [math]::Round(($nota1+$nota2+$nota3)/3, 2)

#Executa o bloco de notas
$wshell.run("Notepad")

#Ativa o Notepad
$wshell.AppActivate("Notepad")

#Espera de 1s
Start-sleep 1

#Verifica se as notas são válidas e mostra a situação do aluno no Notepad
if (($nota1 -ge 0 -and $nota1 -le 10) -and ($nota2 -ge 0 -and $nota2 -le 10) -and ($nota3 -ge 0 -and $nota3 -le 10)){
    
    if ($media -ge 7 -and $media -le 10){
        $wshell.SendKeys("Media: $media`nSituaçao: Aluno aprovado!")
    }

    elseif ($media -ge 4 -and $media -lt 7){
        $wshell.SendKeys("Media: $media`nSituaçao: Aluno de recuperaçao.")
    }

    else {
        $wshell.SendKeys("Media: $media`nSituaçao: Aluno reprovado.")
    }

}

#Mostra uma mensagem de nota(s) inválida(s) no notepad
else {
    $wshell.SendKeys("Voce digitou pelo menos uma nota invalida.")
}