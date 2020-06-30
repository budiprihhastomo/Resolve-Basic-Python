def faktorialganjil(jumlah, awal=0):
    if jumlah == 1:
        return jumlah
    if jumlah % 2 == 0:
        return jumlah//2 * faktorialganjil(jumlah - 1, awal + 1)
    else:
        print(jumlah)
        return jumlah * faktorialganjil(jumlah - 1, awal + 1)

    # else:
    #     if awal < jumlah:
        # if jumlah % 2 == 0:  # Jika Genap
        #     return (jumlah//2) * faktorialganjil(jumlah - 1, awal + 1)
        # else:
        # return (jumlah) * faktorialganjil(jumlah - 1, awal + 1)


print(faktorialganjil(5, 0))
