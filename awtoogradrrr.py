from filseparator import list_all_files as submission
import pandas
from settings import LOWEST_NIM,HIGHEST_NIM,LIST_SOAL,PRAKTIKUM,AUTOSCORE_HEADER,AUTOSCORE_KOMENTAR
from settings import USE_PRESS_ENTER_TO_CONTINUE as pakaiEnter
from settings import PREVIEW_AFTER_CHECKING,RESTRICTED_CODE,ADDITIONAL
import os
from subprocess import call
import sheetgenerator
from time import sleep
import openpyxl

'''END OF COLOR CODE'''

def cari_dir(nfile):
    retr = ""
    for x in submission:
        if nfile in x:
            retr = x
            break
    return retr

def headercheck(flname,nim):
    param = 0
    with open (flname,'r') as pyprog:
        for lines in pyprog:
            if str(nim) in lines : param=param+1
            if "nim" in lines.lower() and len(lines)>25 : param=param+1
            if "nama" in lines.lower() and len(lines) > 25: param = param + 1
            if "tanggal" in lines.lower() and len(lines)>15:  param=param+1
            if "deskripsi" in lines.lower() and len(lines)>15: param=param+1

        pyprog.close()
    if param>=5 : return True
    else : return False

def clrscreen():
    if os.name=="nt": os.system('cls')
    else: os.system('clear')

def printprogram(flname):
    print("========"+flname+"========")
    with open (flname,'r') as pyrpog:
        print(sheetgenerator.colors.fg.yellow)
        for lines in pyrpog:
            print(lines)
        print(sheetgenerator.colors.reset)
        pyrpog.close()
    print("=================================END OF PROGRAM=================================")

def getparentdir(childdir):
    n = len(childdir)-1
    while(childdir[n]!="\\"):
        childdir=childdir[:n:]
        n=n-1
    return childdir

def cekfilename(flname):
    a = len(flname)
    b = len(getparentdir(flname))
    if a-b==18 : return True
    else : return False

def checkerr(errfile):
    err =[]
    with open(errfile,'r') as kesalahan:
        for k in kesalahan:
            err.append(k)
        kesalahan.close()

    if(len(err)<=1): return False
    else:
        print(sheetgenerator.colors.bg.red)
        print("COMPILE / RUNTIME ERROR \n")
        for x in err: print(x)
        print(sheetgenerator.colors.reset)
        return True

def checkAnswer(answer,key,errfile):
    if(checkerr(errfile)):
        return 0
    else:
        ans = []
        kunjaw = []
        with open(answer,'r') as jawaban:
            for x in jawaban:
                if(x==""): ans.append("<enter>")
                else : ans.append(x)
            jawaban.close()
        with open(key,'r') as kunci:
            for x in kunci:
                if (x == ""):
                    kunjaw.append("<enter>")
                else:
                    kunjaw.append(x)
            kunci.close()

        if(len(ans)==len(kunjaw)):
            w =0
            a = True
            while(w<len(ans) and a):
                if(ans[w]!=kunjaw[w]) : a=False
                else : w=w+1

            if a:
                print(sheetgenerator.colors.fg.green+"SELAMAT JAWABAN BENAR"+sheetgenerator.colors.reset)
                return 2
            else:
                print(sheetgenerator.colors.fg.red+"JAWABAN SALAH !!!"+sheetgenerator.colors.reset)
                print("JAWABAN PRAKTIKAN")
                for x in ans : print(sheetgenerator.colors.fg.lightblue+x+sheetgenerator.colors.reset)
                print("\nJAWABAN BENAR")
                for x in kunjaw : print(sheetgenerator.colors.fg.green+x+sheetgenerator.colors.reset)
                return 1
        else:
            print(sheetgenerator.colors.fg.red+"JAWABAN SALAH !!!"+sheetgenerator.colors.reset)
            print("JAWABAN PRAKTIKAN")
            for x in ans: print(sheetgenerator.colors.fg.blue+x+sheetgenerator.colors.reset)
            print("\nJAWABAN BENAR")
            for x in kunjaw: print(sheetgenerator.colors.fg.green+x+sheetgenerator.colors.reset)
            return 1

def tulisatap(nim,flname,nosoal):
    print("SOAL = " + nosoal)
    print("NIM = " + str(nim))
    print("fileloc : " + flname)

def uinput(txt="",lowrange=0,maxrange=0,bilbulat=True):
    i = input(txt)
    if bilbulat:
        flag = True
        if i=="" : flag = False 
        for a in i:
            if (not(a>='0' and a<='9')):
                flag =False
                break

        if flag:
            ret = int(i)
            if(ret>=lowrange and ret<=maxrange):
                return ret
            else:
                print("PLEASE input number between "+str(lowrange)+" and "+str(maxrange))
                return uinput(txt, lowrange, maxrange, True)
        else:
            print("WRONG INPUT FORMAT!!!, REPEAT AGAIN")
            return uinput(txt,lowrange,maxrange,True)
    else:
        return i

def checkKomentar(flname):
    flag ={"kamus":False,"algoritma":False}
    with open (flname,'r') as pyprog:
        for x in pyprog:
            x = x.lower()
            if "kamus" in x : flag["kamus"] = True
            if "algoritma" in x : flag["algoritma"] = True

            if flag["kamus"] and flag["algoritma"]:
                break

    return flag

def korektor(nim,flname,soal):
    LOOPTIME = 0.4
    tulisatap(nim,flname,soal["no_soal"])
    print("\nFase 1. Pengoreksian Sourcecode ")
    printprogram(flname)

    if(soal["check_header"]):
        maxscr = soal["skor_max_header"]
        if not (headercheck(flname, nim) and cekfilename(flname) and AUTOSCORE_HEADER):
            print("Header Program : " + str(headercheck(flname, nim)))
            print("Nama Program : " + str(cekfilename(flname)))
            nil_header = int(uinput("penilaian nama file dan header (0-"+str(maxscr)+")= ", 0, maxscr, True))
        else:
            print("Header Program : " + str(headercheck(flname, nim)))
            print("Nama Program : " + str(cekfilename(flname)))
            print("nilai maksimum untuk nama file dan header telah diberikan ("+str(maxscr)+"/"+str(maxscr)+")")
            nil_header = maxscr
    else: nil_header = 0

    if(soal["check_komentar"]):
        maxscr = soal["skor_max_komentar"]
        if not (checkKomentar(flname)["kamus"] and checkKomentar(flname)["algoritma"] and AUTOSCORE_KOMENTAR):
            print("Kamus terdeteksi = " + str(checkKomentar(flname)["kamus"]))
            print("Algoritma terdeteksi = " + str(checkKomentar(flname)["algoritma"]))
            nil_komen = int(uinput("penilaian indentasi dan komentar (0-"+str(maxscr)+")= ", 0, maxscr, True))
        else:
            print("Kamus terdeteksi = " + str(checkKomentar(flname)["kamus"]))
            print("Algoritma terdeteksi = " + str(checkKomentar(flname)["algoritma"]))
            print("nilai maksimum untuk komentar dan indentasi telah diberikan ("+str(maxscr)+"/"+str(maxscr)+")")
            nil_komen = maxscr
    else: nil_komen = 0

    if(soal["check_penguasaan_modul"]):
        maxscr = soal["skor_max_penguasaan_modul"]
        nil_modul = int(uinput("penilaian penguasaan terhadap modul (0-"+str(maxscr)+")= ", 0, maxscr, True))
    else: nil_modul = 0

    clrscreen()

    nil_cc = []
    for x in soal['check_case']:
        tulisatap(nim, flname, soal["no_soal"])
        print("\nFase 2. Running sample case")
        try:
            temp = soal['check_case'][x]
            newansfile = getparentdir(flname)+"ans_"+x+".txt"
            newerrfile = getparentdir(flname)+"err_"+x+".txt"
            in_params = open(temp["stdin"],'r')
            correct_ans_link = temp["stdout"]
            out_params = open(newansfile,'w')
            out_params.truncate()
            err_params = open(newerrfile,'w')
            err_params.truncate()
            call(["python",flname],stdin=in_params,stdout=out_params,stderr=err_params,timeout=soal['timeout'])
            status_koreksi = checkAnswer(newansfile,correct_ans_link,newerrfile)
            nil_cc.append(int(status_koreksi))
            if(pakaiEnter):
                print("tekan enter untuk lanjut")
                x = input()
            else:
                print()
                for x in range(5):
                    print(". ",end="")
                    sleep(LOOPTIME)
            clrscreen()
        except Exception as e:
            print(e)

    if float(sum(nil_cc))/float(len(nil_cc))>=1:
        nil_kompilasi = soal["skor_max_kompilasi"]
    else: nil_kompilasi = 0

    nil_tc=[]
    for x in soal['test_case']:
        tulisatap(nim, flname, soal["no_soal"])
        print("\nFase 3. Running test case")
        try:
            temp = soal['test_case'][x]
            newansfile = getparentdir(flname) + "ans_" + x + ".txt"
            newerrfile = getparentdir(flname) + "err_" + x + ".txt"
            in_params = open(temp["stdin"], 'r')
            correct_ans_link = temp["stdout"]
            out_params = open(newansfile, 'w')
            out_params.truncate()
            err_params = open(newerrfile, 'w')
            err_params.truncate()
            call(["python", flname], stdin=in_params, stdout=out_params, stderr=err_params,timeout=soal['timeout'])
            status_koreksi = checkAnswer(newansfile, correct_ans_link, newerrfile)
            if(status_koreksi==0):
                nil_tc.append(0)
                print("Kompilasi error/ time limit exceeded. Nilai 0 telah diberikan untuk testcases ini")
                if (pakaiEnter):
                    print("tekan enter untuk lanjut")
                    x = input()
                else:
                    print()
                    for x in range(5):
                        print(". ", end="")
                        sleep(LOOPTIME)

            elif(status_koreksi==1):
                txt = "Penilaian anda untuk testcase ini (0-"+str(temp["score"])+") = "
                custnil = int(uinput(txt,0,temp["score"],True))
                nil_tc.append(custnil)
            elif(status_koreksi==2):
                nil_tc.append(int(temp["score"]))
                if (pakaiEnter):
                    print("tekan enter untuk lanjut")
                    x = input()
                else:
                    print()
                    for x in range(5):
                        print(". ", end="")
                        sleep(LOOPTIME)
            clrscreen()
        except Exception as e:
            print(e)
    nil_program = sum(nil_tc)
    print("pengoreksian soal "+soal["no_soal"]+" untuk nim "+str(nim)+" telah selesai")
    if PREVIEW_AFTER_CHECKING:
        print("=================PREVIEW PENILAIAN=================\n")
        print("filename = "+str(flname)+"\n")
        print("=================Penilaian Header==================")
        if soal["check_header"]:
            print("Penamaan File = "+str(cekfilename(flname)))
            print("Header File = "+str(headercheck(flname, nim)))
            print("Skor diberikan = "+str(nil_header))
            print()
        else: print("SKIPPED\n")

        print("=================Penilaian Komentar==================")
        if(soal["check_komentar"]):
            print("Kamus terdeteksi = " + str(checkKomentar(flname)["kamus"]))
            print("Algoritma terdeteksi = " + str(checkKomentar(flname)["algoritma"]))
            print("Skor diberikan = "+str(nil_komen))
            print()
        else:
            print("SKIPPED\n")

        print("==============Penilaian Penguasaan Modul===============")
        if(soal["check_penguasaan_modul"]):
            print("Skor diberikan = "+str(nil_modul))
            print()
        else:
            print("SKIPPED\n")

        print("=================Penilaian Kompilasi==================")
        print("penjelasan kompilasi:")
        print("kompilasi dilakukan dengan menjalankan semua check case")
        print("0 => compile error/ runtime error")
        print("1 => compile success tapi WA")
        print("2 => compile success dan jawaban benar mutlak")
        print("\nDetail Running check case = "+str(nil_cc))
        print("Skor Diberikan = "+str(nil_kompilasi))
        print()

        print("=================Penilaian Test Case==================")
        print("penilaian kebenaran program dengan mejalankan semua \n test case")
        for x in range (len(nil_tc)):
            print("TC"+str(x)+" = "+str(nil_tc[x]))
        print("\nTotal nilai test case = "+str(nil_program))

        print("=================Restricted Code==================")
        print("coming soon")

        print()
        print("Tekan Enter untuk lanjut, gunakan 's' untuk review source code")
        inp = input()

        while(inp != ""):
            if (inp == "s"):
                printprogram(flname)

            print("Tekan Enter untuk lanjut")
            inp = input()
    else:
        print("program will continue after 2,5 sec")
        sleep(2.5)
    
    clrscreen()
    res = [nil_header,nil_komen,nil_kompilasi,nil_modul,nil_program,nil_cc,nil_tc]
    return res

def mainprog():
    sgen = []
    c = 0

    print("AWTOGRADRRRR PENGKOM")
    print("=====================\n\n")
    print("CEK SETTING SEBELUM MULAI PROGRAM")
    print("RANGE NIM PENGKOREKSIAN = "+str(LOWEST_NIM)+"-"+str(HIGHEST_NIM))
    print("PRAKTIKUM KE = "+PRAKTIKUM)
    print("JUMLAH SOAL = "+str(len(LIST_SOAL)))
    print("AUTOCHECK HEADER ON = "+str(AUTOSCORE_HEADER))
    print("AUTOCHECK KOMENTAR ON = "+str(AUTOSCORE_KOMENTAR))
    print("AUTO NEXT IF CORRECT ANSWER ON = "+str(not pakaiEnter))
    print("PREVIEW AFTER CHECKING = ",str(PREVIEW_AFTER_CHECKING))
    print("RESTRICTED CODE = "+str(RESTRICTED_CODE))
    asdf = input("\nTEKAN ENTER UNTUK LANJUT, SILAHKAN KELUAR JIKA RAGU")
    clrscreen()

    LIST_NIM_PRAKTIKAN = []
    for nim in range(LOWEST_NIM, HIGHEST_NIM + 1): LIST_NIM_PRAKTIKAN.append(nim)
    for nim in ADDITIONAL : LIST_NIM_PRAKTIKAN.append(nim)

    for soal in LIST_SOAL:
        shetgen = sheetgenerator.sheetgenerator(soal)
        sgen.append(shetgen)
        for nim in LIST_NIM_PRAKTIKAN:
            try:
                filename = soal["type"] + PRAKTIKUM + "_" + str(nim) + "_" + soal["no_soal"] + ".py"
                if not cari_dir(filename)=="" :
                    r = korektor(nim,cari_dir(filename),soal)
                    sgen[c].push(nim,r[0],r[1],r[2],r[3],r[4],r[5],r[6])
                else:
                    sgen[c].push(nim,0,0,0,0,0,
                                 [0 for x in range(len(soal["check_case"]))],
                                 [0 for x in range(len(soal["test_case"]))])
                #if breaksoal or breakprogram:
                    #break
            except Exception as e:
                print(e)
        c = c+1
        #if breakprogram:
            #break

    print("All process was done")
    print("===============================")
    print("your file will be stored into .xlsx")
    outfile = input("namefile (without .xlsx)= ")
    outfile.lower()
    while(".xlsx" in outfile):
        print("DON'T PUT .XLSX PLEASE")
        outfile = input("namefile (without .xlsx)= ")
        outfile.lower()

    try:
        for ayy in sgen:
            ayy.toExcel(outfile)

        sgen[0].toXCL(sgen,outfile)
        print("your scoring sheet successfully saved as "+outfile+".xlsx")
        print("plase check output folder to check .xlsx file, we also put csv as emergency score files")
    except Exception as e:
        print(e)

    print("THANKS FOR USING THIS PROGRAM")
    print("Credit by cah pesisir if'19")
    sleep(3)

mainprog()

