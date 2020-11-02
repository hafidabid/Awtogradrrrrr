import pandas as pd
import openpyxl
import os
import xlsxwriter
class sheetgenerator:
    NIM = "NIM"
    Header = "Header&Nama"
    Kompilasi = "Kompilasi"
    Indentasi ="IndentasiKomentar"
    PenguasaanModul = "penguasaan modul"
    Kebenaran_Prog = "kebenaran_program"
    def __init__(self,dictsoal):
        self.soalKe = dictsoal["no_soal"]
        self.data = {
            self.NIM: [],
            self.Header :[],
            self.Indentasi : [],
            self.Kompilasi :[],
            self.PenguasaanModul :[],
            self.Kebenaran_Prog : [],
        }
        c=1
        for x in dictsoal["check_case"]:
            s = "check_case"+str(c)
            c=c+1
            self.data[s] = []

        c = 1
        for x in dictsoal["test_case"]:
            s = "test_case" + str(c)
            c = c + 1
            self.data[s] = []

    def push(self,nim, skorHeader,skorIndentasi,skorKompilasi,skorPenguasaan,skorKebenaran,check_case_res,test_case_res):
        self.data[self.NIM].append(nim)
        self.data[self.Header].append(skorHeader)
        self.data[self.Indentasi].append(skorIndentasi)
        self.data[self.Kompilasi].append(skorKompilasi)
        self.data[self.PenguasaanModul].append(skorPenguasaan)
        self.data[self.Kebenaran_Prog].append(skorKebenaran)

        for x in range(1,len(check_case_res)+1):
            s = "check_case" + str(x)
            self.data[s].append(check_case_res[x-1])

        for x in range(1,len(test_case_res)+1):
            s = "test_case" + str(x)
            self.data[s].append(test_case_res[x-1])

    def toExcel(self,filename):
        if(not os.path.isdir("output")):
            os.makedirs("output")

        df = pd.DataFrame(self.data)
        #we = pd.ExcelWriter("output\\"+filename+".xlsx",engine="xlsxwriter")
        #shetname = "soal_"+self.soalKe
        #df.to_excel(we,sheet_name=shetname,index=False)
        df.to_csv("output\\"+filename+self.soalKe+".csv")
        #we.save()

    def toXCL(self,arrshg,filename):
        arr = []
        for x in arrshg:
            df= pd.DataFrame(x.data)
            arr.append(df)
        we = pd.ExcelWriter("output\\" + filename + ".xlsx", engine="xlsxwriter")
        c=0
        for x in arr:
            x.to_excel(we,sheet_name="soal_"+arrshg[c].soalKe)
            c=c+1

        we.save()


class colors:
    '''
    Colors class:reset all colors with colors.reset; two
    sub classes fg for foreground
    and bg for background; use as colors.subclass.colorname.
    i.e. colors.fg.red or colors.bg.greenalso, the generic bold, disable,
    underline, reverse, strike through,
    and invisible work with the main class i.e. colors.bold'''
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg:
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'
