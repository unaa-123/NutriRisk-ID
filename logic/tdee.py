def hitung_tdee(bmr, aktivitas):
    """
    aktivitas:
    1.2   = sangat ringan
    1.375 = ringan
    1.55  = sedang
    1.725 = berat
    """

    faktor_aktivitas = {
        "sangat ringan": 1.2,
        "ringan": 1.375,
        "sedang": 1.55,
        "berat": 1.725
    }

    if aktivitas not in faktor_aktivitas:
        raise ValueError("Aktivitas harus: sangat ringan, ringan, sedang, atau berat")

    tdee = bmr * faktor_aktivitas[aktivitas]
    return round(tdee, 2)
