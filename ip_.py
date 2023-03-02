import ipaddress

def ip(ip_address, netmask):
    ip = ipaddress.ip_address(ip_address)
    net = ipaddress.ip_network(f'{ip_address}/{netmask}', strict=False)
    network = str(net.network_address)
    num_addresses = net.num_addresses
    first_address = str(net[1])
    last_address = str(net[-2])
    return (network, first_address, last_address, num_addresses)

ip_address = "192.168.1.100"
netmask = "24"
print(ip(ip_address, netmask))




