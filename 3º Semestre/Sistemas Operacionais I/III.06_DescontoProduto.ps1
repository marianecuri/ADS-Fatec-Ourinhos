<#
Um script que calcula o desconto em um produto com base no preço original e
na porcentagem de desconto oferecida. Verifica se o desconto é maior que 10%.
Se for, exibe "Desconto concedido". Caso contrário, exibe "Desconto insuficiente".
#>

Clear-Host

#Classe WScript.Shell
$wshell = New-Object -com Wscript.Shell

#Recebe o valor e a porcentagem de desconto do usuário
[float]$preco_original = Read-Host "Digite o preço original do produto (R$)"
[float]$porcentagem = Read-Host "Digite a porcentagem de desconto oferecida (%)"

#Verifica se o desconto é menor ou menor que 10% e exibe um pop-up
if ($porcentagem -gt 10){
    [float]$desconto = [math]::Round($preco_original*($porcentagem/100), 2)
    [float]$novo_preco = [math]::Round($preco_original-$desconto, 2)
    $wshell.Popup("Desconto concedido.`nValor do desconto: R$ $desconto`nPreço do produto com desconto: R$ $novo_preco")
}

else {
    $wshell.Popup("Desconto insuficiente.")
}