contacts = {
    'Badu': '089879938817',
    'Hana': '0818662514110',
    'Seto': '08122290909',
    'Adi': '0856808080012',
    'Pace': '0858000000000'
}


def cari_berdasarkan_operator(contacts, operator):
    nama = []
    for name, value in contacts.items():
        if operator == "im3" and value.find("085") == 0:
            nama.append(name)
        elif operator == "three" and value.find("089") == 0:
            nama.append(name)
        elif operator == "telkomsel" and value.find("081") == 0:
            nama.append(name)
        elif operator == "xl" and value.find("081") == 0:
            nama.append(name)
    print(nama)


operator = "im3"
cari_berdasarkan_operator(contacts, operator)
