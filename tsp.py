import os,csv
from itertools import permutations
lintasan=""
database="database.csv"
data_salesman = []
data_user = []
tampung_username = []    
tampung_password = []  
graf = [[0,4,6,8,10,12], #jakarta
        [4,0,20,38,22,11], #bogor
        [6,20,0,18,16,11], #semarang
        [8,38,18,0,18,21], #malang
        [10,22,16,18,0,11], #yogya
        [12,11,11,21,11,0,]] #purwo
try :
    with open(database, "r") as csvWrite:
        reader= csv.reader(csvWrite, delimiter=",")
        for baris in reader:
            data_salesman.append(baris)
except:
    pass

def main():
    os.system("cls")
    print("="*108)
    print("||"+"NinjaGoo".center(104)+"||")
    print("="*108)
    print("||"+"Selamat datang di aplikasi NinjaGoo!".center(104)+"||")
    print("||"+"Silahkan login jika anda telah memiliki akun".center(104)+"||")
    print("||"+"Dan silahkan mendaftar terlebih dahulu jika anda tida mempunyai akun.".center(104)+"||")
    print("="*108)
    print("|| "+" [1] Masuk".ljust(103)+"||")
    print("|| "+" [2] Daftar".ljust(103)+"||")    
    print("|| "+" [3] Keluar".ljust(103)+"||")    
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
    pilih = input("=> Masukkan pilihan anda = ")
    if pilih == "1":
        login()
    elif pilih == "2":
        register()
    elif pilih == "3":
        exit()
        
def menu_kota():
    os.system("cls")
    global start
    print("="*108)
    print("||"+"Daftar Menu kota".center(104)+"||")
    print("="*108)
    print("||"+"  0 = Jakarta".ljust(104)+"||")
    print("||"+"  1 = Bogor".ljust(104)+"||")
    print("||"+"  2 = Semarang".ljust(104)+"||")
    print("||"+"  3 = Malang".ljust(104)+"||")
    print("||"+"  4 = Yogyakarta".ljust(104)+"||")
    print("||"+"  5 = Purwokerto".ljust(104)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)   
    start = int(input("==> Masukkan titik awal : "))

def tsp(graf, start): 
    global lintasan
    tampung_point = []
    lintasan_tsp=[]
    for point in range(len(graf)): #0,1,2,3,4,5
        if point != start:
            tampung_point.append(point)
    min_cost = 1000000
    tampung_permutasi = permutations(tampung_point)
    for permutasi in tampung_permutasi:
        kota_awal(start)
        lintasan+="-->"
        current_cost = 0
        baris=start 
        for kolom in permutasi: #2,3,1,2,5
            kota_tengah(kolom)
            current_cost += graf[baris][kolom]
            baris = kolom
        kota_awal(start)     
        current_cost += graf[baris][start]
        lintasan_copy=lintasan
        if current_cost == min_cost:
            lintasan_tsp.append(lintasan_copy)
        elif current_cost < min_cost:
            lintasan_tsp.clear()
            lintasan_tsp.append(lintasan_copy)
        min_cost = min(min_cost, current_cost)
        lintasan=""
    return min_cost,lintasan,lintasan_tsp

def kota_awal(start):
    global lintasan
    if start ==0:
        lintasan+="Jakarta"
    elif start ==1:
        lintasan+="Bogor"
    elif start ==2:
        lintasan+="Semarang"
    elif start ==3:
        lintasan+="Malang" 
    elif start ==4:
        lintasan+="Yogjakarta" 
    elif start ==5:
        lintasan+="Purwokerto" 
    elif start ==6:
        lintasan+="Bandung"

def kota_tengah(kolom):
    global lintasan
    if kolom ==0:
        lintasan+="Jakarta-->"
    elif kolom ==1:
        lintasan+="Bogor-->"
    elif kolom ==2:
        lintasan+="Semarang-->"
    elif kolom ==3:
        lintasan+="Malang-->"
    elif kolom ==4:
        lintasan+="Yogjakarta-->"
    elif kolom ==5:
        lintasan+="Purwokerto-->"
                           
def hasil():
    cost_bbm=10000
    pertamax=4
    jmlh_pertamax=tsp(graf, start)[0]/pertamax
    total_biaya=tsp(graf, start)[0]/pertamax*cost_bbm
    print("="*108)
    print("||"+"Kesimpulan".center(104)+"||")
    print("="*108)
    print("||"+"  Lintasan terpendek    : ",tsp(graf, start)[0],"km".ljust(74)+"||")
    print("||"+"  Menghabiskan pertamax : ",jmlh_pertamax,"liter".ljust(72)+"||")
    print("||"+"  Total biaya           : ",total_biaya,"".ljust(68)+"||")
    for i in range(len(tsp(graf, start)[2])):
        print("||"+"  Lintasan yang dilalui : ",tsp(graf, start)[2][i].ljust(77)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
    input("Tekan enter untuk kembali")
    dashboard()

def detail():
    kota=["Jakata","Bogor","Semarang","Malang","Yogyakarta","Purwokerto"]
    menu_kota()
    input("Tekan enter untuk melihat detail rute..")
    print("="*108)
    print("||"+"Detail rute".center(104)+"||")
    print("="*108)
    for i in range(len(graf)):
        cost=str(kota[start])+"-->"+str(kota[i])+" = "+str(graf[start][i])+" km"
        print("||"+f'  {cost}'.ljust(104)+"||")  
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
    
def login():
    os.system("cls")
    print("="*108)
    print("||"+"NinjaGo".center(104)+"||")
    print("="*108)
    nama = []
    sandi = []
    with open("database.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        try:
            for row in csv_reader:
                nama.append(row[0])
                sandi.append(row[1])
        except:
            pass
    username = input("  Username      : ")
    password = input("  Password      : ")
    if username in nama:
        index = nama.index(username)
        if password == sandi[index]:
            dashboard()
        else:
            print("Username atau Password salah")
    else:
        print("Username tidak ditemukan")
    input("Enter untuk kembali")
    main()
    
def dashboard():
    os.system("cls")
    print("="*108)
    print("||"+"NinjaGo".center(104)+"||")
    print("="*108)
    print("||"+"  [1] = Mulai rute".ljust(104)+"||")
    print("||"+"  [2] = Detail rute".ljust(104)+"||")
    print("||"+"  [0] = Keluar".ljust(104)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
    pilihan=input("Masukkan pilihan anda : ")
    if pilihan=='1':
        menu_kota()   
        tsp(graf, start)
        hasil()
    elif pilihan=='2':
        detail()
        input("Tekan enter untuk kembali")
        dashboard()
    elif pilihan=='0':
        confirm=input("Apakah anda yakin untuk keluar ? [y] : ")
        if confirm == 'y':
            main()
        else :
            dashboard()
    else :
        dashboard()

def register():   
    os.system("cls")
    errors = 0
    print("="*108)
    print("||"+"NinjaGo".center(104)+"||")
    print("="*108)
    username = input("  Username      : ")
    password = input("  Password      : ")
    if username.isalnum() == False or password.isalnum() == False:
        errors += 1
        print("Username atau password hanya berupa huruf dan angka saja")
    if len(username) < 6 or len(password) < 6:
        errors += 1
        print("Username atau password minimal terdiri dari 6 karakter")
    if username == password:
        errors += 1
        print("Username dan password tidak boleh sama")
    if errors == 0:
        data_salesman.append([username, password])
        with open("database.csv", "w", newline="") as css:
            write = csv.writer(css, delimiter=",")
            for t in data_salesman:
                write.writerow(t)
        print("Akun anda berhasil dibuat,silahkan login!")
    input("Tekan enter untuk kembali..")
    main()
        
main()   