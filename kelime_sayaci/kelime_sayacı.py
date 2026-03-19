print("Kelime Sayacı Programı")

metin = input("Bir metin gir: ")

kelime_sayisi = len(metin.split())
harf_sayisi = len(metin.replace(" ", ""))

# Her harfin kaç kere geçtiğini sayalım
harf_sayaci = {}
for harf in metin.replace(" ", "").lower():
    if harf in harf_sayaci:
        harf_sayaci[harf] += 1
    else:
        harf_sayaci[harf] = 1

print("\nToplam kelime sayısı:", kelime_sayisi)
print("Toplam harf sayısı:", harf_sayisi)
print("Harf dağılımı:")
for harf, sayi in harf_sayaci.items():
    print(f"{harf}: {sayi}")
