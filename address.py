def bin_to_int(value: str) -> int:
    nbr = 0
    for exposant, bit in enumerate(reversed(value), 0):
        nbr += 2 ** exposant if bit == "1" else 0

    return nbr


def int_to_bin(value: int, bits: int = None) -> str:
    if bits is not None and (value >= 2**bits or value < 0):
        raise Exception(f"la valeur est sur {bits} bits donc sur [0 ; {2 ** bits - 1}]")

    dividende = value

    binaire = []
    while dividende >= 1:
        reste = dividende % 2
        dividende //= 2

        binaire.append(str(reste))

    binaire = binaire[::-1] # inverse la liste
    binaire = "".join(binaire)

    if bits is not None:
        binaire = "0" * (bits - len(binaire)) + binaire

    return binaire


def address_to_bin(address : str, bits: int = 8) -> list[str, str, str, str]:
    return [int_to_bin(int(i), bits=bits) for i in address.split(".")]


def bin_address_to_str(address: list[str, str, str, str]) -> str:
    return ".".join(str(bin_to_int(octet)) for octet in address)


def get_cidr(mask : list[str, str, str, str], ) -> int:
    cidr = 0
    for i in mask:
        cidr += i.count("1")

    return cidr


def get_network_address(ip : list, mask : list) -> list[str, str, str, str]:
    network_address = []
    for i in range(0, 4):
        octet = ''
        for j in range(0, 8):
            octet += f"{ int(ip[i][j]) and int(mask[i][j]) }"

        network_address.append(octet)

    return network_address


def get_broadcast_address(network_adress: list[str, str, str, str], mask: list[str, str, str, str]) -> list[str, str, str, str]:
    broadcast_address = []

    for i in range(0, len(network_adress)):
        octet = ""
        for j in range(0, len(mask[i])):
            if mask[i][j] == "1":
                octet += network_adress[i][j]
            else:
                octet += "1"
        broadcast_address.append(octet)

    return broadcast_address


def get_available_address(cidr: int) -> int:
    return 2 ** (32 - cidr) - 2


def sum_address(address: list[str, str, str, str]) -> int:
    somme = 0
    for i, octet in enumerate(address):
        somme += bin_to_int(octet) * (256 ** (3 - i))
    return somme


def is_ip_address_valid(address: list[str, str, str, str], network_address: list[str, str, str, str], broadcast_address: list[str, str, str, str]) -> bool:
    return sum_address(network_address) < sum_address(address) < sum_address(broadcast_address)
