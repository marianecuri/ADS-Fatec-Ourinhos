#Um script que calcula a área de um círculo. O usuário deve inserir o raio
#do círculo e o resultado deve ser arredondado para duas casas decimais.

Clear-Host

#Classe WScript.Shell
$wshell = New-Object -com Wscript.Shell

#Recebe os números do usuário e calcula a área
[double]$raio = Read-Host "Digite o raio do círculo"
$area = [math]::Round([math]::PI * [math]::Pow($raio, 2), 2)

#Mostra um pop-up com o valor da área do círculo
$wshell.Popup("A área do círculo é $area.")