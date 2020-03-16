<#------------------------------------------------------ 
	PowerShell Script 
	update: 2-Mrz-20
	(c) 2020 Jan Unger 
	* Backup -> zip
------------------------------------------------------#>
Clear-Host # cls

#---------------------------------------
$thema  = "Machine-Learning-Notiz" # anpassen
#---------------------------------------

# löschen
if(test-path ../"${thema}.zip"){rm ../"${thema}.zip" -force -recurse}
# zip
Compress-Archive ./ -Update -dest ../"${thema}.zip"
