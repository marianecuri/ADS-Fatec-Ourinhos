#Um script que solicita ao usuário sua idade e verifica se ele é
#elegível para votar. Considere que a idade mínima para votar é 16
#anos e que a pessoa não é obrigada a votar com mais de 69 anos.

Clear-Host

#Classe WScript.Shell
$wshell = New-Object -com Wscript.Shell

#Recebe a idade do usuário
[int]$idade = Read-Host "Digite sua idade"

#Mostra um pop-up dizendo se a idade é elegível ou não
if ($idade -lt 16){
    $wshell.Popup("Você ainda não tem idade para votar.")
}

elseif ($idade -lt 70){
    $wshell.Popup("Você é elegível para votar.")
}

else {
    $wshell.Popup("Você é elegível para votar, mas não é obrigado(a).")
}