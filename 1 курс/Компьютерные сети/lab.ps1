$inte = Read-Host "interface: "
$interface = Get-NetAdapter -Name $inte
echo "1 - Auto, 2 - Manually, 3 - Info"
$choice = Read-Host "Your choice: "
if ($choice -eq 1) {
	Set-NetIPInterface -InterfaceIndex $interface.ifIndex -Dhcp Enabled
    Set-DnsClientServerAddress -InterfaceIndex $interface.ifIndex -ResetServerAddresses
} elseif ($choice -eq 2) {
	Set-NetIPInterface -InterfaceIndex $interface.ifIndex -Dhcp Disabled
    Remove-NetIPAddress -InterfaceIndex $interface.ifIndex -Confirm:$false
    Remove-NetRoute -InterfaceIndex $interface.ifIndex -Confirm:$false
	$ip = Read-Host "ip: "
    $mask = Read-Host "mask: "
    $gateway = Read-Host "gateway: "
    $dns = Read-Host "dns: "
    New-NetIPAddress -InterfaceIndex $interface.ifIndex -IPAddress $ip -PrefixLength $mask -DefaultGateway $gateway
	Set-DnsClientServerAddress -InterfaceIndex $interface.ifIndex -ServerAddresses $dns
} elseif ($choice -eq 3) {
	$interface
} else {
	# skip
}
echo "Done!"
pause
