#Um script que solicita 3 números ao usuário e calcula Bháskara.

Clear-Host

#Classe WScript.Shell
$wshell = New-Object -com Wscript.Shell

#Recebe os números do usuário
[float]$a = Read-Host "Digite o valor de a"
[float]$b = Read-Host "Digite o valor de b"
[float]$c = Read-Host "Digite o valor de c"

#Realiza os cálculos
$delta = [math]::Pow($b, 2) - 4*$a*$c
$x1 = (-1*$b + [math]::Sqrt($delta)) / (2*$a)
$x2 = (-1*$b - [math]::Sqrt($delta)) / (2*$a)

#Mostra um pop-up com as raízes da equação
$wshell.Popup("As raízes da equação são $x1 e $x2.")