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
LOWEST_NIM =    16520077 #ISI DENGAN NIM TERENDAH DI KELAS
HIGHEST_NIM =   16520077 #ISI DENGAN NIM TERTINGGI DI KELAS
ADDITIONAL = ['16520084', '16520087', '16520124', '16520132', '16520136', '16520138', '16520140']
 #GUNAKAN ADDITIONAL UNTUK NIM TAMBAHAN DILUAR RANGE NIM
PRAKTIKUM = "02" #ISI DENGAN PRAKTIKUM KE-x DENGAN PENGISIAN "01" BUKAN 1 ATAU "02" BUKAN 2 ATAU "10" BUKAN 10
FOLDER_SUBMISI_PRAKTIKUM = ["3.1_b_2_Pra-Praktikum","3.1_b_2_Praktikum"] #FOLDER TEMPAT ANDA MENYIMPAN FILE PY PRAKTIKAN BAIK ITU TP DAN PRAKTIKUM
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
PREVIEW_AFTER_CHECKING = False
RESTRICTED_CODE = []
TOLERATED_MODE = True

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
    "exact_mode": False, #MODE GRADING MUTLAK. APABILA BENAR 100% DENGAN TEST CASE MAKA NILAI FULL, JIKA SALAH MAKA 0
    #HATI HATI DALAM MEMAKAI EXACT_MODE, KARENA APABILA JAWABAN BEDA TITIK SAJA MAKA AKAN LANGSUNG DI BERI NILAI 0.

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

tp21 = {
    "type" : "H", #ISI DENGAN 'H' UNTUK PENDAHULUAN PRAKTIKUM DAN 'P' UNTUK PRAKTIKUM
    "no_soal" : "01", # ISI DENGAN NOMOR SOAL DENGAN 01 BUKAN 1, 02 BUKAN 2
    "check_header" : False,  #CEK HEADER? BILA TIDAK NILAI HEADER LANGSUNG 0
    "skor_max_header" : 10,
    "check_komentar" :False, #CEK KOMENTAR&INDENTASI ? BILA TIDAK NILAI LANGSUNG 0
    "skor_max_komentar" :10,
    "check_penguasaan_modul":False,      #CEK PENGUASAAN MODUL ? BILA TIDAK NILAI LANGSUNG 0
    "skor_max_penguasaan_modul" : 20,   #SKOR MAKSIMAL PENGUASAAN MODUL
    "skor_max_kompilasi" : 40,      #SKOR APABILA PROGRAM TERCOMPILE DENGAN BAIK DAN BENAR
    "timeout" : 6,
    "exact_mode": False, #MODE GRADING MUTLAK. APABILA BENAR 100% DENGAN TEST CASE MAKA NILAI FULL, JIKA SALAH MAKA 0
    #CC DAPAT DITAMBAH DAN DIKURANGI. NAMUN MIN CC=1, DAN SEBISA MUNGKIN JANGAN KEBANYAKAN TC.
    #TC CUKUP 1-3 SAJA.
    "check_case" : {
        "cc1":{
            "stdin" : "testcases\\2tp\\1\\h01_cc1i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout" : "testcases\\2tp\\1\\h01_cc1a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
        },
        "cc2":{
            "stdin" : "testcases\\2tp\\1\\h01_cc2i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout" : "testcases\\2tp\\1\\h01_cc2a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
        }
    },
    #TEST CASE DAPAT DIPERBANYAK ATAU DI KURANGIN. DENGAN MIN TC=1.
    "test_case" : {
        "tc1" : {
            "stdin" : "testcases\\2tp\\1\\h01_tc1i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout" : "testcases\\2tp\\1\\h01_tc1a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
            "score" : 15                            #SCORE APABILA TC INI BENAR
        },
        "tc2"  :{
            "stdin" : "testcases\\2tp\\1\\h01_tc2i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout" : "testcases\\2tp\\1\\h01_tc2a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
            "score" : 15                            #SCORE APABILA TC INI BENAR
        },
        "tc3"  :{
            "stdin" : "testcases\\2tp\\1\\h01_tc3i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout" : "testcases\\2tp\\1\\h01_tc3a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
            "score" : 15                            #SCORE APABILA TC INI BENAR
        },
        "tc4": {
            "stdin" : "testcases\\2tp\\1\\h01_tc4i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout" : "testcases\\2tp\\1\\h01_tc4a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
            "score": 15                            #SCORE APABILA TC INI BENAR
        }

    },
}

tp22 = {
    "type" : "H", #ISI DENGAN 'H' UNTUK PENDAHULUAN PRAKTIKUM DAN 'P' UNTUK PRAKTIKUM
    "no_soal" : "02", # ISI DENGAN NOMOR SOAL DENGAN 01 BUKAN 1, 02 BUKAN 2
    "check_header" : False,  #CEK HEADER? BILA TIDAK NILAI HEADER LANGSUNG 0
    "skor_max_header" : 10,
    "check_komentar" :False, #CEK KOMENTAR&INDENTASI ? BILA TIDAK NILAI LANGSUNG 0
    "skor_max_komentar" :10,
    "check_penguasaan_modul":False,      #CEK PENGUASAAN MODUL ? BILA TIDAK NILAI LANGSUNG 0
    "skor_max_penguasaan_modul" : 20,   #SKOR MAKSIMAL PENGUASAAN MODUL
    "skor_max_kompilasi" : 40,      #SKOR APABILA PROGRAM TERCOMPILE DENGAN BAIK DAN BENAR
    "timeout" : 5,
    "exact_mode": False, #MODE GRADING MUTLAK. APABILA BENAR 100% DENGAN TEST CASE MAKA NILAI FULL, JIKA SALAH MAKA 0
    #CC DAPAT DITAMBAH DAN DIKURANGI. NAMUN MIN CC=1, DAN SEBISA MUNGKIN JANGAN KEBANYAKAN TC.
    #TC CUKUP 1-3 SAJA.
    "check_case" : {
        "cc1":{
            "stdin" : "testcases\\2tp\\2\\h01_cc1i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout" : "testcases\\2tp\\2\\h01_cc1a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
        },
        "cc2":{
            "stdin" : "testcases\\2tp\\2\\h01_cc2i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout" : "testcases\\2tp\\2\\h01_cc2a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
        }
    },
    #TEST CASE DAPAT DIPERBANYAK ATAU DI KURANGIN. DENGAN MIN TC=1.
    "test_case" : {
        "tc1" : {
            "stdin"         : "testcases\\2tp\\2\\h01_tc1i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout"        : "testcases\\2tp\\2\\h01_tc1a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
            "score"         : 15,                            #SCORE APABILA TC INI BENAR
            "w_double_grade": False,
            "double_grader" : {
                "dgrader_app"   : "",
                "dgrader_out"   : "",
                "penalty"       : 0,
            }
        },
        "tc2"  :{
            "stdin" : "testcases\\2tp\\2\\h01_tc2i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout" : "testcases\\2tp\\2\\h01_tc2a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
            "score" : 15,                            #SCORE APABILA TC INI BENAR
            "w_double_grade": False,
            "double_grader" : {
                "dgrader_app"   : "",
                "dgrader_out"   : "",
                "penalty"       : 0,
            }
        },
        "tc3"  :{
            "stdin" : "testcases\\2tp\\2\\h01_tc3i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout" : "testcases\\2tp\\2\\h01_tc3a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
            "score" : 15,                            #SCORE APABILA TC INI BENAR
            "w_double_grade": False,
            "double_grader" : {
                "dgrader_app"   : "",
                "dgrader_out"   : "",
                "penalty"       : 0,
            }
        },
        "tc4": {
            "stdin" : "testcases\\2tp\\2\\h01_tc4i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout" : "testcases\\2tp\\2\\h01_tc4a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
            "score": 15,                            #SCORE APABILA TC INI BENAR
            "w_double_grade": False,
            "double_grader" : {
                "dgrader_app"   : "",
                "dgrader_out"   : "",
                "penalty"       : 0,
            }
        }

    },
}

tp23 = {
    "type" : "H", #ISI DENGAN 'H' UNTUK PENDAHULUAN PRAKTIKUM DAN 'P' UNTUK PRAKTIKUM
    "no_soal" : "03", # ISI DENGAN NOMOR SOAL DENGAN 01 BUKAN 1, 02 BUKAN 2
    "check_header" : False,  #CEK HEADER? BILA TIDAK NILAI HEADER LANGSUNG 0
    "skor_max_header" : 10,
    "check_komentar" :False, #CEK KOMENTAR&INDENTASI ? BILA TIDAK NILAI LANGSUNG 0
    "skor_max_komentar" :10,
    "check_penguasaan_modul":False,      #CEK PENGUASAAN MODUL ? BILA TIDAK NILAI LANGSUNG 0
    "skor_max_penguasaan_modul" : 20,   #SKOR MAKSIMAL PENGUASAAN MODUL
    "skor_max_kompilasi" : 36,      #SKOR APABILA PROGRAM TERCOMPILE DENGAN BAIK DAN BENAR
    "timeout" : 4,
    "exact_mode": False, #MODE GRADING MUTLAK. APABILA BENAR 100% DENGAN TEST CASE MAKA NILAI FULL, JIKA SALAH MAKA 0
    #CC DAPAT DITAMBAH DAN DIKURANGI. NAMUN MIN CC=1, DAN SEBISA MUNGKIN JANGAN KEBANYAKAN TC.
    #TC CUKUP 1-3 SAJA.
    "check_case" : {
        "cc1":{
            "stdin" : "testcases\\2tp\\3\\h01_cc1i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout" : "testcases\\2tp\\3\\h01_cc1a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
        },
        "cc2":{
            "stdin" : "testcases\\2tp\\3\\h01_cc2i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout" : "testcases\\2tp\\3\\h01_cc2a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
        }
    },
    #TEST CASE DAPAT DIPERBANYAK ATAU DI KURANGIN. DENGAN MIN TC=1.
    "test_case" : {
        "tc1" : {
            "stdin"         : "testcases\\2tp\\3\\h01_tc1i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout"        : "testcases\\2tp\\3\\h01_tc1a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
            "score"         : 13,                            #SCORE APABILA TC INI BENAR
            "w_double_grade": False,
            "double_grader" : {
                "dgrader_app"   : "",
                "dgrader_out"   : "",
                "penalty"       : 0,
            }
        },
        "tc2"  :{
            "stdin" : "testcases\\2tp\\3\\h01_tc2i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout" : "testcases\\2tp\\3\\h01_tc2a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
            "score" : 13,                            #SCORE APABILA TC INI BENAR
            "w_double_grade": False,
            "double_grader" : {
                "dgrader_app"   : "",
                "dgrader_out"   : "",
                "penalty"       : 0,
            }
        },
        "tc3"  :{
            "stdin" : "testcases\\2tp\\3\\h01_tc3i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout" : "testcases\\2tp\\3\\h01_tc3a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
            "score" : 13,                            #SCORE APABILA TC INI BENAR
            "w_double_grade": False,
            "double_grader" : {
                "dgrader_app"   : "",
                "dgrader_out"   : "",
                "penalty"       : 0,
            }
        },
        "tc4": {
            "stdin" : "testcases\\2tp\\3\\h01_tc4i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout" : "testcases\\2tp\\3\\h01_tc4a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
            "score": 13,                            #SCORE APABILA TC INI BENAR
            "w_double_grade": False,
            "double_grader" : {
                "dgrader_app"   : "",
                "dgrader_out"   : "",
                "penalty"       : 0,
            }
        },
        "tc5": {
            "stdin" : "testcases\\2tp\\3\\h01_tc5i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout" : "testcases\\2tp\\3\\h01_tc5a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
            "score": 6,                            #SCORE APABILA TC INI BENAR
            "w_double_grade": False,
            "double_grader" : {
                "dgrader_app"   : "",
                "dgrader_out"   : "",
                "penalty"       : 0,
            }
        },
        "tc6": {
            "stdin" : "testcases\\2tp\\3\\h01_tc6i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout" : "testcases\\2tp\\3\\h01_tc6a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
            "score": 6,                            #SCORE APABILA TC INI BENAR
            "w_double_grade": False,
            "double_grader" : {
                "dgrader_app"   : "",
                "dgrader_out"   : "",
                "penalty"       : 0,
            }
        }

    },
}

prak2no2 = {
    "type" : "P", #ISI DENGAN 'H' UNTUK PENDAHULUAN PRAKTIKUM DAN 'P' UNTUK PRAKTIKUM
    "no_soal" : "02", # ISI DENGAN NOMOR SOAL DENGAN 01 BUKAN 1, 02 BUKAN 2
    "check_header" : True,  #CEK HEADER? BILA TIDAK NILAI HEADER LANGSUNG 0
    "skor_max_header" : 10,
    "check_komentar" :True, #CEK KOMENTAR&INDENTASI ? BILA TIDAK NILAI LANGSUNG 0
    "skor_max_komentar" :10,
    "check_penguasaan_modul":True,      #CEK PENGUASAAN MODUL ? BILA TIDAK NILAI LANGSUNG 0
    "skor_max_penguasaan_modul" : 20,   #SKOR MAKSIMAL PENGUASAAN MODUL
    "skor_max_kompilasi" : 20,      #SKOR APABILA PROGRAM TERCOMPILE DENGAN BAIK DAN BENAR
    "timeout" : 3,
    "exact_mode": False, #MODE GRADING MUTLAK. APABILA BENAR 100% DENGAN TEST CASE MAKA NILAI FULL, JIKA SALAH MAKA 0
    #CC DAPAT DITAMBAH DAN DIKURANGI. NAMUN MIN CC=1, DAN SEBISA MUNGKIN JANGAN KEBANYAKAN TC.
    #TC CUKUP 1-3 SAJA.
    "check_case" : {
        "cc1":{
            "stdin" : "testcases\\2tp\\4\\h01_cc1i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout" : "testcases\\2tp\\4\\h01_cc1a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
        },
        "cc2":{
            "stdin" : "testcases\\2tp\\4\\h01_cc2i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout" : "testcases\\2tp\\4\\h01_cc2a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
        }
    },
    #TEST CASE DAPAT DIPERBANYAK ATAU DI KURANGIN. DENGAN MIN TC=1.
    "test_case" : {
        "tc1" : {
            "stdin"         : "testcases\\2tp\\4\\h01_tc1i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout"        : "testcases\\2tp\\4\\h01_tc1a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
            "score"         : 8,                            #SCORE APABILA TC INI BENAR
            "w_double_grade": False,
            "double_grader" : {
                "dgrader_app"   : "",
                "dgrader_out"   : "",
                "penalty"       : 0,
            }
        },
        "tc2"  :{
            "stdin" : "testcases\\2tp\\4\\h01_tc2i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout" : "testcases\\2tp\\4\\h01_tc2a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
            "score" : 8,                            #SCORE APABILA TC INI BENAR
            "w_double_grade": False,
            "double_grader" : {
                "dgrader_app"   : "",
                "dgrader_out"   : "",
                "penalty"       : 0,
            }
        },
        "tc3"  :{
            "stdin" : "testcases\\2tp\\4\\h01_tc3i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout" : "testcases\\2tp\\4\\h01_tc3a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
            "score" : 8,                            #SCORE APABILA TC INI BENAR
            "w_double_grade": False,
            "double_grader" : {
                "dgrader_app"   : "",
                "dgrader_out"   : "",
                "penalty"       : 0,
            }
        },
        "tc4": {
            "stdin" : "testcases\\2tp\\4\\h01_tc4i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout" : "testcases\\2tp\\4\\h01_tc4a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
            "score": 8,                            #SCORE APABILA TC INI BENAR
            "w_double_grade": False,
            "double_grader" : {
                "dgrader_app"   : "",
                "dgrader_out"   : "",
                "penalty"       : 0,
            }
        },
        "tc5": {
            "stdin" : "testcases\\2tp\\4\\h01_tc5i.txt", #STDIN ADALAH INPUTAN PROGRAM
            "stdout" : "testcases\\2tp\\4\\h01_tc5a.txt", #STDOUT ADALAH KELUARAN PROGRAM YANG BENAR
            "score": 8,                            #SCORE APABILA TC INI BENAR
            "w_double_grade": False,
            "double_grader" : {
                "dgrader_app"   : "",
                "dgrader_out"   : "",
                "penalty"       : 0,
            }
        }

    },
}
LIST_SOAL = [tp22]







