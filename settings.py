'''
AWTOGRDRR PENGKOM, by Cah Pesisir
disclaimer : ini bukan full autograde, namun semi autograde. bila jawaban salah anda bisa memberi nilai secara manual
jawaban skor penuh akan diberikan jika jawaban 'excactly true' dan skor 0 akan diberi jika Compile error.
'''
'''
RANGE NIM DAN DETAIL PRAKTIKUM
NB : UNTUK KASUS PENGOREKSIAN DENGAN NIM ACAK, EX : 16520004,16520020,16520026
GUNAKAN LOWEST_NIM = HIGHEST_NIM = 16520004, LALU DI ARRAY ADDITIONAL KASIH [16520020,16520026]

UNTUK FOLDER SUBMISI PRAKTIKUM, KASIH LIST DENGAN DIRECTORY TEMPAT ANDA MENYIMPAN FOLDER
BERISIKAN FOLDER-FOLDER PRAKTIKAN (P0X_1XX20XXX). KALAU BISA TARUH PADA DIREKTORI SEJAJAR DENGAN FILE INI
EX:
-AWTOGRADRR
    -output                 #folder ini tempat meletakkan file .xlsx dan .csv hasil autograding
    -settings.py
    -awtoogradrrr.py
    -sheetgenerator.py
    -requirements.txt
    -FOLDER_PRAK_01
    -FOLDER_TP_01

'''
LOWEST_NIM =    16520080 #ISI DENGAN NIM TERENDAH DI KELAS
HIGHEST_NIM =   16520080 #ISI DENGAN NIM TERTINGGI DI KELAS
ADDITIONAL = [16520085,16520096] #GUNAKAN ADDITIONAL UNTUK NIM TAMBAHAN DILUAR RANGE NIM
PRAKTIKUM = "01" #ISI DENGAN PRAKTIKUM KE-x DENGAN PENGISIAN "01" BUKAN 1 ATAU "02" BUKAN 2 ATAU "10" BUKAN 10
FOLDER_SUBMISI_PRAKTIKUM = ["PRAKTIKUM_01_3.1B","TP_01_3.1B"] #FOLDER TEMPAT ANDA MENYIMPAN FILE PY PRAKTIKAN BAIK ITU TP DAN PRAKTIKUM
'''
GENERAL SETTINGS

AUTOSCORE_HEADER BERFUNGSI UNTUK LANGSUNG MEMBERI NILAI HEADER FULL APABILA FORMAT FILE DAN PADA HEADER
TERDAPAT NAMA, NIM VALID, TANGGAL, DAN DESKRIPSI

AUTOSCORE_KOMENTAR BERFUNGSI UNTUK MEMBERI NILAI KOMENTAR & INDENTASI FULL APABILA SOURCECODE MENGANDUNG
KAMUS DAN ALGORITMA

USE_PRESS_ENTER_TO_CONTINUE BERGUNA PADA SETELAH GRADING PROGRAM DENGAN STATUS EXCACT TRUE ATAU CE, 
BILA TRUE MAKA AKAN MINTA KLIK ENTER UNTUK LANJUT
BILA FALSE MAKA AKAN AUTO CONTINUE SETELAH 2-3 DETIK

PREVIEW_AFTER_CHECKING BERGUNA UNTUK MENAMPILKAN PREVIEW HASIL PENILAIAN SETIAP SELESAI MENILAI 1 SUBMISI

RESTRICTED_CODE UNTUK DAFTAR-DAFTAR KODE YANG DILARANG, EX: SUM, BREAK, DSB.
-> FITUR MASIH COMING SOON
'''
AUTOSCORE_HEADER = True
AUTOSCORE_KOMENTAR = True
USE_PRESS_ENTER_TO_CONTINUE= False
PREVIEW_AFTER_CHECKING = True
RESTRICTED_CODE = []

'''
SOAL DAN JAWABAN, PERHATIKAN UNTUK UPDATE ELEMEN LIST_SOAL SESUAI DENGAN SOAL YANG INGIN DI CHECK!!!
LIST SOAL ADA DI LINE PALING BAWAH

CONTOH INISIALISASI SOAL BARU
soal1 = {
    "type" : "P", #ISI DENGAN 'H' UNTUK PENDAHULUAN PRAKTIKUM DAN 'P' UNTUK PRAKTIKUM
    "no_soal" : "01", # ISI DENGAN NOMOR SOAL DENGAN 01 BUKAN 1, 02 BUKAN 2
    "check_header" : True,  #CEK HEADER? BILA TIDAK NILAI HEADER LANGSUNG 0
    "skor_max_header" : 10,
    "check_komentar" :True, #CEK KOMENTAR&INDENTASI ? BILA TIDAK NILAI LANGSUNG 0
    "skor_max_komentar" :10,
    "check_penguasaan_modul":True,      #CEK PENGUASAAN MODUL ? BILA TIDAK NILAI LANGSUNG 0
    "skor_max_penguasaan_modul" : 20,   #SKOR MAKSIMAL PENGUASAAN MODUL
    "skor_max_kompilasi" : 20,      #SKOR APABILA PROGRAM TERCOMPILE DENGAN BAIK DAN BENAR
    "timeout" : 5,
    #CC DAPAT DITAMBAH DAN DIKURANGI. NAMUN MIN CC=1, DAN SEBISA MUNGKIN JANGAN KEBANYAKAN TC.
    #TC CUKUP 1-3 SAJA.
    "check_case" : {
        "cc1":{
            "stdin" : "testcases\\1.1\\1cc1i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout" : "testcases\\1.1\\1cc1a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
        },
    },
    #TEST CASE DAPAT DIPERBANYAK ATAU DI KURANGIN. DENGAN MIN TC=1.
    "test_case" : {
        "tc1" : {
            "stdin" : "testcases\\1.1\\1tc1i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout" : "testcases\\1.1\\1tc1a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
            "score" : 10                            #SCORE APABILA TC INI BENAR
        },
        "tc2"  :{
            "stdin" : "testcases\\1.1\\1tc2i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout" : "testcases\\1.1\\1tc2a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
            "score" : 10                            #SCORE APABILA TC INI BENAR
        }

    },
}

MEMASUKKAN soal1 KE DALAM LIST
LIST_SOAL = [soal1]
'''
soal1 = {
    "type" : "P", #ISI DENGAN 'H' UNTUK PENDAHULUAN PRAKTIKUM DAN 'P' UNTUK PRAKTIKUM
    "no_soal" : "01", # ISI DENGAN NOMOR SOAL DENGAN 01 BUKAN 1, 02 BUKAN 2
    "check_header" : True,  #CEK HEADER? BILA TIDAK NILAI HEADER LANGSUNG 0
    "skor_max_header" : 10,
    "check_komentar" :True, #CEK KOMENTAR&INDENTASI ? BILA TIDAK NILAI LANGSUNG 0
    "skor_max_komentar" :10,
    "check_penguasaan_modul":True,      #CEK PENGUASAAN MODUL ? BILA TIDAK NILAI LANGSUNG 0
    "skor_max_penguasaan_modul" : 20,   #SKOR MAKSIMAL PENGUASAAN MODUL
    "skor_max_kompilasi" : 20,      #SKOR APABILA PROGRAM TERCOMPILE DENGAN BAIK DAN BENAR
    "timeout" : 5,
    #CC DAPAT DITAMBAH DAN DIKURANGI. NAMUN MIN CC=1, DAN SEBISA MUNGKIN JANGAN KEBANYAKAN TC.
    #TC CUKUP 1-3 SAJA.
    "check_case" : {
        "cc1":{
            "stdin" : "testcases\\1.1\\1cc1i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout" : "testcases\\1.1\\1cc1a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
        },
        "cc2":{
            "stdin" : "testcases\\1.1\\1cc2i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout" : "testcases\\1.1\\1cc2a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
        }
    },
    #TEST CASE DAPAT DIPERBANYAK ATAU DI KURANGIN. DENGAN MIN TC=1.
    "test_case" : {
        "tc1" : {
            "stdin" : "testcases\\1.1\\1tc1i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout" : "testcases\\1.1\\1tc1a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
            "score" : 10                            #SCORE APABILA TC INI BENAR
        },
        "tc2"  :{
            "stdin" : "testcases\\1.1\\1tc2i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout" : "testcases\\1.1\\1tc2a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
            "score" : 10                            #SCORE APABILA TC INI BENAR
        },
        "tc3"  :{
            "stdin" : "testcases\\1.1\\1tc3i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout" : "testcases\\1.1\\1tc3a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
            "score" : 10                            #SCORE APABILA TC INI BENAR
        },
        "tc4": {
            "stdin" : "testcases\\1.1\\1tc4i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout" : "testcases\\1.1\\1tc4a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
            "score": 10                            #SCORE APABILA TC INI BENAR
        }

    },
}

soal2 = {
    "type" : "P", #ISI DENGAN 'H' UNTUK PENDAHULUAN PRAKTIKUM DAN 'P' UNTUK PRAKTIKUM
    "no_soal" : "03", # ISI DENGAN NOMOR SOAL DENGAN 01 BUKAN 1, 02 BUKAN 2
    "check_header" : False,
    "skor_max_header" : 10,
    "check_komentar" :False,
    "skor_max_komentar" :10,
    "check_penguasaan_modul":False,
    "skor_max_penguasaan_modul" : 20,
    "skor_max_kompilasi" : 60,
    "timeout" : 5,
    "check_case" : {
        "cc1":{
            "stdin" : "testcases\\1.3\\cc1i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout" : "testcases\\1.3\\cc1a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
        },
    },
    "test_case" : {
        "tc1" : {
            "stdin": "testcases\\1.3\\tc1i.txt",  # STDIN ADALAH INPUTAN PROGRAM
            "stdout": "testcases\\1.3\\tc1a.txt",  # STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
            "score" : 20
        },
        "tc2"  :{
            "stdin": "testcases\\1.3\\tc2i.txt",  # STDIN ADALAH INPUTAN PROGRAM
            "stdout": "testcases\\1.3\\tc2a.txt",  # STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
            "score" : 20
        },

    },
}

LIST_SOAL = [soal1]







