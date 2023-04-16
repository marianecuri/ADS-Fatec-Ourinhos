<#
Um script que recebe o valor da venda, escolhe a condição
de pagamento no menu e mostra o total da venda final.
#>

Clear-Host

#Classe WScript.Shell
$wshell = New-Object -com Wscript.Shell

#Recebe o valor da venda do usuário
[float]$valor = Read-Host "Valor da venda (R$)"

#Mostra um menu com as opções de pagamento
Write-Host "`nSelecione uma opção de cálculo:"
Write-Host "[a] Venda a Vista - desconto de 10%"
Write-Host "[b] Venda a Prazo 30 dias - desconto de 5%"
Write-Host "[c] Venda a Prazo 60 dias - mesmo preço"
Write-Host "[d] Venda a Prazo 90 dias - acréscimo de 5%"
Write-Host "[e] Venda com cartão de débito - desconto de 8%"
Write-Host "[f] Venda com cartão de crédito - desconto de 7%"

[string]$opcao = Read-Host

#Calcula o valor total da venda final
switch ($opcao)
{
    a {$total = $valor - ($valor*0.1)}
    b {$total = $valor - ($valor*0.05)}
    c {$total = $valor}
    d {$total = $valor + ($valor*0.05)}
    e {$total = $valor - ($valor*0.08)}
    f {$total = $valor - ($valor*0.07)}
    default {$wshell.Popup("Opção inválida.")}
}

#Mostra um pop-up com o valor total da venda final
if ($opcao -eq 'a' -or $opcao -eq 'b'-or $opcao -eq 'c' -or $opcao -eq 'd' -or $opcao -eq 'e' -or $opcao -eq 'f'){
    $wshell.Popup("Valor total da venda final: R$ $total.")
}