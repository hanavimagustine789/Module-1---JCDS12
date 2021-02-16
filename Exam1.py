### Exam_ Soal No 1 

# Create a return function with 1 argument that will accept input of the integer number (Seconds). And it will produce a string output with time format ("HH:MM:SS").

# HH : Hours, 2 digits, range: 00 - 99

# MM : Minutes, 2 digits, range: 00 - 59

# SS : Seconds, 2 digits, range: 00 - 59

# output:
# #Masukkan detik : 3600
# Konversi : 01:00:00

# Masukkan detik : 3665
# Konversi : 01:01:05


def timeConverter(seconds):
    try:
        time = int(input("Masukan Detik : "))
        HH = Hours
        MM = Minutes
        SS = Seconds
        H0 = 00
        M0 = 00
        S0 = 00
        time1 = 359999
        for time in range (00,359999) :
            if time > 359999:
                return "Angka yang anda masukan Tidak Valid"
            elif time < 0 :
                return "Tidak Menerima Angka Negatif"
            else:
                H0 = time // 100000   
                H1 = (time % 100000) // 10000
                M0 = ((timee % 100000) % 10000) // 10000
                M1 = ((timee % 100000) % 10000) % 1000) // 100
                S0 = ((timee % 100000) % 10000) % 1000) % 100) // 10
                S1 = (time % 100000) % 10000) % 1000) % 100) % 10
                hasil = [(H0 // 100000 ) [:] (H1 // 100000) [:] (M0 // 10000) [:] (M1 // 1000) [:] (S0 // 1000)]
                if H0 == 0 and M0 == 0 and S0 == 0:
                    print("00", ':', end '')
                    return hasil
                elif  M0 == 0 and SS == 0:
                    print("00", ":" end='')
                    return hasil
                elif S0 == 0:
                    print("00", ":" end='')
                    return hasil
    except:
        print("Tidak Menerima alfabet/Tidak menerima angka negatif dan desimal")

print(timeConverter(seconds))

            

