def skor_usia(usia):
    if usia < 35:
        return 0
    elif usia < 45:
        return 1
    elif usia < 55:
        return 2
    else:
        return 3


def skor_imt(imt):
    if imt < 23:
        return 0
    elif imt < 25:
        return 1
    elif imt < 30:
        return 2
    else:
        return 3


def skor_aktivitas(aktivitas):
    if aktivitas in ["sedang", "berat"]:
        return 0
    elif aktivitas == "ringan":
        return 1
    else:  # sangat ringan
        return 2


def skor_riwayat_keluarga(ada):
    return 2 if ada else 0


def skor_pola_makan(tidak_sehat):
    return 1 if tidak_sehat else 0


def total_skor_risiko(usia, imt, aktivitas, riwayat, pola_makan):
    total = (
        skor_usia(usia)
        + skor_imt(imt)
        + skor_aktivitas(aktivitas)
        + skor_riwayat_keluarga(riwayat)
        + skor_pola_makan(pola_makan)
    )
    return total


def kategori_risiko(total_skor):
    if total_skor <= 2:
        return "Risiko rendah"
    elif total_skor <= 5:
        return "Risiko meningkat"
    else:
        return "Risiko tinggi"
