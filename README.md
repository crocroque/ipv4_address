# Ipv4 
## Example usage
```python

from address import *

if __name__ == "__main__":
    ip_bin = address_to_bin("192.168.10.10")
    print(ip_bin) # output : ['11000000', '10101000', '00001010', '00001010']

    mask_bin = address_to_bin("255.255.0.0")
    print(mask_bin) # output : ['11111111', '11111111', '00000000', '00000000']

    network_address_bin = get_network_address(ip_bin, mask_bin)
    print(network_address_bin) # output : ['11000000', '10101000', '00000000', '00000000']

    broadcast_address_bin = get_broadcast_address(network_address_bin, mask_bin)
    print(broadcast_address_bin) # output : ['11000000', '10101000', '11111111', '11111111']

    str_broadcast_address = bin_address_to_str(address=broadcast_address_bin)
    print(str_broadcast_address) # output : "192.168.255.255"

    ip_test = "192.168.0.0"
    bin_ip_test = address_to_bin(address=ip_test)
    ip_test_is_valid = is_ip_address_valid(address=bin_ip_test,
                                           network_address=network_address_bin,
                                           broadcast_address=broadcast_address_bin)
    print(ip_test_is_valid) # output : False

    ip_test = "192.168.52.2"
    bin_ip_test = address_to_bin(address=ip_test)
    ip_test_is_valid = is_ip_address_valid(address=bin_ip_test,
                                           network_address=network_address_bin,
                                           broadcast_address=broadcast_address_bin)
    print(ip_test_is_valid) # output : True


```
