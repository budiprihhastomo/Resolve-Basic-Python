def bagidesimal(ip_address, curr=0):
    items = ip_address.split('.')
    result = []

    def arrangeData(curr=0):
        if curr < len(items):
            arrangeData(curr + 1)
            result.append('{0:08b}'.format(int(items[curr])))
            return ".".join(reversed(result))

    return arrangeData()


# Testing
print(bagidesimal("192.168.1.1"))
print(bagidesimal("192.168.1.2"))
print(bagidesimal("10.10.10.10"))
