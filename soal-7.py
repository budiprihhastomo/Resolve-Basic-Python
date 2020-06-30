import time
from datetime import datetime

data = ['2019-01-01', '2019-01-15', '2019-01-22',
        '2020-03-01', '2020-04-01', '2020-06-11']
data_second = ['2020-01-22', '2017-01-01', '2019-01-15',
               '2021-03-01', '2020-04-10', '2020-06-11']


def cek_urut(data):
    sort = ""
    way = ""
    duplicate = list(data)
    for index, tanggal in enumerate(data):
        formatTanggal = time.mktime(
            datetime.strptime(tanggal, "%Y-%m-%d").timetuple())
        duplicate[index] = formatTanggal

    # Checking Sort
    testSort = []
    for index, value in enumerate(duplicate):
        if index < len(duplicate) - 1:
            if float(duplicate[index]) < float(duplicate[index + 1]):
                testSort.append(1)
                way = "naik"
            elif float(duplicate[index]) > float(duplicate[index + 1]):
                testSort.append(0)
                way = "turun"
            else:
                return False
    sort = len(set(testSort)) == 1
    print("Urut" + " " + way if sort else "Tidak urut")


cek_urut(data)
cek_urut(data_second)
