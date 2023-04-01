#Um script que realiza operações matemáticas básicas.

Clear-Host

#Classe WScript.Shell
$wshell = New-Object -com Wscript.Shell

#Mostra as opções de operações e recebe a resposta do usuário
"Selecione uma opção:
[A]Adição
[S]Subtração
[M]Multiplicação
[D]Divisão"

$operacao = Read-Host

#Mostra um pop-up de opção inválida
if ($operacao -ne "A" -and $operacao -ne "S" -and $operacao -ne "M" -and $operacao -ne "D"){
    $wshell.Popup("$operacao não é uma opção válida.")
}

#Recebe os números do usuário e mostra um pop-up com o resultado da operação
else {
    
    [float]$numero1 = Read-Host "Digite um número"
    [float]$numero2 = Read-Host "Digite outro número"

    if ($operacao -eq "A"){
        [float]$numero3 = $numero1+$numero2
        $wshell.Popup("O resultado de $numero1 mais $numero2 é $numero3.")
    }

    elseif ($operacao -eq "S"){
        [float]$numero3 = $numero1-$numero2
        $wshell.Popup("O resultado de $numero1 menos $numero2 é $numero3.")
    }

    elseif ($operacao -eq "M"){
        [float]$numero3 = $numero1*$numero2
        $wshell.Popup("O resultado de $numero1 vezes $numero2 é $numero3.")
    }

    else {
        [float]$numero3 = $numero1/$numero2
        $wshell.Popup("O resultado de $numero1 dividido por $numero2 é $numero3.")
    }

}