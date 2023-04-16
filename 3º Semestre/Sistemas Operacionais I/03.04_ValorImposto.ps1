<#
Um script que calcula o imposto de renda com base no salário de uma pessoa.
Se o salário for menor que R$ 5.000,00, a taxa de imposto é 10%.
Caso contrário, a taxa de imposto é 20%. Exibe o valor do imposto a ser pago.
#>

Clear-Host

#Classe WScript.Shell
$wshell = New-Object -com Wscript.Shell

#Recebe o salário do usuário
[float]$salario = Read-Host "Digite o salário (R$)"

#Verifica se o salário é menor ou menor que 5000 e define a taxa
if ($salario -lt 5000){
    [float]$taxa_imposto = 0.1
}

else {
    [float]$taxa_imposto = 0.2
}

#Atribui o valor do imposto a ser pago
[float]$valor_imposto = [math]::Round($salario*$taxa_imposto, 2)

#Mostra um pop-up com o valor do imposto a ser pago
$wshell.Popup("O valor do imposto a ser pago é: R$ $valor_imposto")