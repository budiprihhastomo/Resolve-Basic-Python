import re
kalimat = 'jancuk! aku dikibuli toko online.'
terlarang = ["jancuk", "aku"]
pengganti = 'wkwkwk'


def sensor_kalimat(kalimat, terlarang, pengganti):
    s = kalimat
    for i in range(len(terlarang)):
        s = re.sub(terlarang[i], pengganti, kalimat)
    return s


print(sensor_kalimat(kalimat, terlarang, pengganti))
