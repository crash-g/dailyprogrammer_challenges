def solve(addresses):
    # filter a sorted array of addresses
    if not addresses:
        return []
    filteredAddresses = [addresses[0]]
    current=0
    for i in range(1,len(addresses)):
        if addresses[current][1] not in addresses[i][1]:
            current = i
            filteredAddresses.append(addresses[i])
    return filteredAddresses

def parse(fileName):
    with open(fileName, "r") as lines:
        ipList = []
        for i in range(0,int(lines.readline().strip())):
            line = lines.readline().strip()
            ip, bits =line.split("/")
            ipList.append((line, "".join(["{0:08b}".format(int(n)) for n in ip.split(".")])[:int(bits)]))
        # array containing the ip address and its binary representation (only significant digits)
        return ipList

print("\n".join(a[0] for a in solve(sorted(parse("ip_addresses.txt"), key=lambda ip: ip[1]))))
