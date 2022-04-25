import ipaddress


def int32_to_ip(int32):
    return str(ipaddress.IPv4Address(int32))


# def int32_to_ip(int32):
#     return '{}.{}.{}.{}'.format(*int32.to_bytes(4, 'big'))


print(int32_to_ip(32))