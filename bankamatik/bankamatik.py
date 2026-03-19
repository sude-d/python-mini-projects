hesapA = {
    'ad': 'Sude Dağaşan',
    'hesapno': '13245678',
    'bakiye': 3000,
    'ekHesap': 2000
}

hesapB = {
    'ad': 'Mine Dağaşan',
    'hesapno': '12345678',
    'bakiye': 2000,
    'ekHesap': 1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        print('Bakiyeniz yeterli. Paranızı alabilirsiniz.')
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']
        
        if (toplam >= miktar):
            ekHesapKullanimi = input('Bakiye yetersiz. Ek hesap kullanılsın mı? (evet/hayır): ')
            if ekHesapKullanimi == 'evet':
                print('Ek hesabınızdan çekim yapıldı. Paranızı alabilirsiniz.')
            else:
                print(f"{hesap['hesapno']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır.")
        else:
            print('Üzgünüz, toplam bakiye ve ek hesap limitiniz yetersiz.')
print("1. İşlem (Sude Hanım")
paraCek(hesapA, 4000)

print("2. İşlem (Mine Hanım)")
paraCek(hesapB, 5000) 
