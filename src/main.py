from netmiko import ConnectHandler


device = {
    'device_type': 'cisco_ios',  # change to your device type
    'ip':   '10.0.0.1',  # change to your device's IP
    'username': 'admin',  # change to your username
    'password': 'password',  # change to your password
    'secret': 'secret',  # change to your secret
}

connection = ConnectHandler(**device)

output = connection.send_command('show ip int brief')

print(output)

connection.disconnect()