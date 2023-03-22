#Um script que solicita a entrada de 3 números e: calcula o produto
#do dobro do primeiro numero com metade do segundo; a soma do triplo
#do primeiro com o terceiro; o terceiro elevado ao cubo.

Clear-Host

#Classe WScript.Shell
$wshell = New-Object -com Wscript.Shell

#Recebe os números do usuário
[float]$a = Read-Host "Digite um número"
[float]$b = Read-Host "Digite outro número"
[float]$c = Read-Host "Digite mais um número"

#Realiza os cálculos
$x = [math]::Round((2*$a)*($b/2), 2)
$y = [math]::Round((3*$a)+$c, 2)
$z = [math]::Round([math]::Pow($c, 3), 2)

#Mostra um pop-up com o resultado das operações
$wshell.Popup("O produto do dobro de $a com metade de $b é igual a $x.
A soma do triplo de $a com $c é igual a $y.
$c elevado ao cubo é igual a $z.")