# suhu.py

def konversi_suhu(nilai, dari, ke):
    dari = dari.lower()
    ke = ke.lower()

    # Validasi satuan
    if dari not in ["c", "f", "k"] or ke not in ["c", "f", "k"]:
        raise ValueError("Satuan tidak valid. Gunakan C, F, atau K.")

    # Validasi nilai suhu
    if dari == "k" and nilai < 0:
        raise ValueError("Nilai Kelvin tidak boleh negatif.")

    # Jika satuan asal dan tujuan sama
    if dari == ke:
        return nilai

    # Konversi awal ke Celsius
    if dari == "c":
        c = nilai
    elif dari == "f":
        c = (nilai - 32) * 5/9
    else:  # dari == "k"
        c = nilai - 273.15

    # Konversi dari Celsius ke tujuan
    if ke == "c":
        return c
    elif ke == "f":
        return (c * 9/5) + 32
    else:  # ke == "k"
        return c + 273.15
