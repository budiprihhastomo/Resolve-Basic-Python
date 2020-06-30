def decimaltobinary(value):
    def reverse(value):
        return reverse(value[1:]) + value[0] if value != "" else value

    def operate(value):
        if value == 0:
            return ''
        else:
            return operate(value//2) + str(value % 2)

    return reverse(operate(value))


print(decimaltobinary(10))
print(decimaltobinary(2))
print(decimaltobinary(5))
