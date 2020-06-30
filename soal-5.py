def bagibinary(binary):
    items = binary.split('.')
    result = []

    def arrangeData(curr=0):
        if curr < len(items):
            arrangeData(curr + 1)
            result.append(str(int(items[curr], 2)))
            return ".".join(reversed(result))
    return arrangeData()


# Testing
print(bagibinary('11000000.10101000.00000001.00000001'))
print(bagibinary('11000000.10101000.00000001.00000010'))
print(bagibinary('00001010.00001010.00001010.00001010'))
