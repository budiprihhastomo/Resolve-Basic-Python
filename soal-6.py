import math


def pangkat_dua_spesial(angka):
    if angka < 0:
        return "Angka Harus Lebih Besar Dari 0"
    stringInput = str(angka)
    # Pecah Ratusan Puluhan Satuan
    def ratusan(): return int(math.floor(int(stringInput[-3]) * 100)) ** 2
    def puluhan(): return int(math.floor(int(stringInput[-2]) * 10)) ** 2
    def satuan(): return int(math.floor(int(stringInput[-1]) * 1)) ** 2

    count = 1
    result = 0
    while count < len(stringInput) + 1:
        if count == 1:
            result += satuan()
        elif count == 2:
            result += puluhan()
        elif count == 3:
            result += ratusan()
        else:
            result += 0
        count += 1
    return result


# Testing
print(pangkat_dua_spesial(25))
print(pangkat_dua_spesial(137))
print(pangkat_dua_spesial(1))
print(pangkat_dua_spesial(-2))
