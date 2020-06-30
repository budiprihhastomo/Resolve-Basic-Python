def soal_ganjil(value):
    hasilTambah = []

    def operation(value, currentValue=1):
        if currentValue > value:
            return
        operation(value, currentValue + 1)
        if currentValue % 2 > 0:
            hasilTambah.append(currentValue)
        return sum(hasilTambah)
    
    return operation(value)


# Testing
print(soal_ganjil(5))
print(soal_ganjil(10))
print(soal_ganjil(100))
