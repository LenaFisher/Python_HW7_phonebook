import csv 
import interface

# num = 0
# num2 = 0
# surname = ""
# name = ""
# phone = ""
# description = ""

def initChoises(n,n2):
    global num
    global num2
    num = n
    num2= n2

def init(srn, nm, ph, desc):
    global surname
    global name
    global phone
    global description
    surname = srn
    name = nm
    phone = ph
    description = desc



def do_action():
    if num2==1 and num == 1:  
        add_to_CSV()
    elif num2==2 and num == 1:
        import_data_csv()
    elif num2 ==1 and num == 2:
        add_to_TXT()
    elif num2 ==2 and num == 2:
        import_data_txt()
 

def add_to_TXT():
    with open("txt.txt","a", encoding="utf-8") as f_txt:
        f_txt.write(f"{surname}\n{name}\n{phone}\n{description}\n\n")
        print("создана запись в файле TXT формата")


def add_to_CSV():
    with open("scv_file.csv","w", encoding="utf-8") as f_csv:
        writer = csv.writer(f_csv)
        writer.writerow([surname, name, phone, description])
        print("создана запись в файле CSV формата")

def import_data_txt():
    with open("txt.txt", "r",encoding="utf-8") as f_txt:
        for line in f_txt:
            print(f_txt.readlines())

def import_data_csv():
    with open("scv_file.csv", encoding="utf-8") as f_csv:
        reader = csv.reader(f_csv)
        for line in reader:
            print(line)


