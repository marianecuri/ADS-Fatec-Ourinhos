<#
Um script que recebe um número real, digitado pelo usuário e mostra
o menu para selecionar o tipo de cálculo que deve ser realizado:
1-Raiz quadrada
2-A metade
3-10% do número
4-O dobro
#>

Clear-Host

#Classe WScript.Shell
$wshell = New-Object -com Wscript.Shell

#Recebe o número do usuário
[float]$numero = Read-Host "Digite um número"

#Mostra um menu com as opções de cálculo
Write-Host "`nSelecione uma opção de cálculo:"
Write-Host "[1] Raiz quadrada"
Write-Host "[2] A metade"
Write-Host "[3] 10% do número"
Write-Host "[4] O dobro"

[int]$operacao = Read-Host

#Mostra um pop-up de opção inválida
if ($operacao -ne "1" -and $operacao -ne "2" -and $operacao -ne "3" -and $operacao -ne "4"){
    $wshell.Popup("$operacao não é uma opção válida.")
}

#Recebe os números do usuário e mostra um pop-up com o resultado da operação
else {

    if ($operacao -eq "1"){
        [float]$resultado = [math]::Sqrt($numero)
        $wshell.Popup("A raiz quadrada de $numero é $resultado.")
    }

    elseif ($operacao -eq "2"){
        [float]$resultado = $numero/2
        $wshell.Popup("O metade de $numero é $resultado.")
    }

    elseif ($operacao -eq "3"){
        [float]$resultado = $numero * 0.1
        $wshell.Popup("10% de $numero é $resultado.")
    }

    else {
        [float]$resultado = $numero * 2
        $wshell.Popup("O dobro de $numero é $resultado.")
    }

}