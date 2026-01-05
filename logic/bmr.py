def hitung_bmr(jenis_kelamin, bb, tb_cm, usia):
    """
    Menghitung Kebutuhan Energi Basal (KEB/BMR)
    jenis_kelamin: 'L' atau 'P'
    bb: berat badan (kg)
    tb_cm: tinggi badan (cm)
    usia: tahun
    """

    if jenis_kelamin.upper() == 'L':
        bmr = 66.5 + (13.8 * bb) + (5 * tb_cm) - (6.8 * usia)
    elif jenis_kelamin.upper() == 'P':
        bmr = 665 + (9.6 * bb) + (1.8 * tb_cm) - (4.7 * usia)
    else:
        raise ValueError("Jenis kelamin harus 'L' atau 'P'")

    return round(bmr, 2)
