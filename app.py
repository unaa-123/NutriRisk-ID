from flask import Flask, render_template, request

from logic.imt import hitung_imt, kategori_imt_asia
from logic.bmr import hitung_bmr
from logic.tdee import hitung_tdee
from logic.risiko import total_skor_risiko, kategori_risiko

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = None

    if request.method == "POST":
        bb = float(request.form["bb"])
        tb = float(request.form["tb"])
        usia = int(request.form["usia"])
        jk = request.form["jk"]
        aktivitas = request.form["aktivitas"]
        riwayat = request.form.get("riwayat") == "ya"
        pola_makan = request.form.get("pola_makan") == "tidak_sehat"

        imt = round(hitung_imt(bb, tb), 1)
        kategori_imt = kategori_imt_asia(imt)

        bmr = round(hitung_bmr(jk, bb, tb, usia))
        tdee = round(hitung_tdee(bmr, aktivitas))

        skor = total_skor_risiko(
            usia=usia,
            imt=imt,
            aktivitas=aktivitas,
            riwayat=riwayat,
            pola_makan=pola_makan
        )

        kategori = kategori_risiko(skor)

        if kategori == "Risiko rendah":
            interpretasi = (
                "Risiko diabetes tergolong rendah. "
                "Pertahankan pola hidup sehat dan aktivitas fisik teratur."
                )
        elif kategori == "Risiko meningkat":
            interpretasi = (
                "Risiko diabetes mulai meningkat. "
                "Disarankan memperbaiki pola makan dan meningkatkan aktivitas fisik."
                )
        else:
            interpretasi = (
                "Risiko diabetes tergolong tinggi. "
                "Disarankan melakukan evaluasi medis dan konsultasi dengan tenaga kesehatan."
                )


        if kategori == "Risiko rendah":
            warna = "rendah"
        elif kategori == "Risiko meningkat":
            warna = "sedang"
        else:
            warna = "tinggi"

        hasil = {
            "imt": imt,
            "kategori_imt": kategori_imt,
            "bmr": bmr,
            "tdee": tdee,
            "skor": skor,
            "kategori_risiko": kategori,
            "interpretasi": interpretasi,
             "warna": warna
        }

    return render_template("index.html", hasil=hasil)

@app.route("/edukasi")
def edukasi():
    return render_template("edukasi.html")

if __name__ == "__main__":
    app.run()
