def hitung_imt(bb, tb_cm):
    tb_m = tb_cm / 100
    imt = bb / (tb_m ** 2)
    return round(imt, 2)

def kategori_imt_asia(imt):
    if imt < 18.5:
        return "Berat badan kurang"
    elif imt < 23:
        return "Normal"
    elif imt < 25:
        return "Berisiko"
    elif imt < 30:
        return "Obesitas I"
    else:
        return "Obesitas II"
