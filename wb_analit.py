import csv
import os
import time
# Исходные данные
Ct = time.time()

TD = os.getcwd(); S_f = os.listdir(TD); ls = len(S_f)
Spf = ['']*100; l1 = 0
for i in range(ls):
    If = S_f[i].split('.')
    if len(If) > 1:
        If2 = If[1]
        if If2 == 'csv':
            If1 = If[0]
            if If1[:3] != 'Rez':
                Spf[l1] = S_f[i]
                print(str(l1), Spf[l1])
                l1 = l1 + 1
    continue
Lspf = l1

for Nspf in range(Lspf):
    File_N000 = Spf[Nspf]
    if Nspf == 0: F_N000 = File_N000
    File_N = File_N000
    F0 = File_N.split('.')
    F1 = F0[0].replace('\\', '/')

    if not os.path.isdir(F1): os.mkdir(F1)
    TD = os.getcwd(); lt = len(TD)
    TD = TD.replace('\\', '/')
    Std = str(TD) + '/'
    Tdr = Std + F1 + '/'
    File_N0 = Std + F1 + '.csv'
    File_N = Tdr + F1 + '.csv'
    File_N_1 = Tdr + F1 + '_1.csv'
    File_Ekr = Std + F1 + '_Ekr.txt'
# Перенумерация столбцов
    Kol_Ps = 14
    Ps = [13, 12, 9, 5, 3, 0, 1, 2, 4, 6, 7, 8, 10, 11, ]

# Адрес записи файлов

    Frz4 = Tdr + 'Rez_A1.csv'
    File_N1 = Tdr + 'A1.csv'

# Номер столбца для сортировки !!! Если вставляются новые столбцы
    Np = 9

# Имя исходного файла
    Fisx = Tdr + 'Rez_A1.csv'

# Файл записи результатов
    File_N2 = Std + 'Rez_' + F_N000
    File_N2_1 = Std + 'Rez_1' + F_N000

# Столбцы печати категорий
    Sp1 = 8; Sp2 = 9; Sp3 = 12

# Топ постащиков
    N_Top = 10

# Мах. Количество поставщиков
    Dl_Sel = 200000

    Zg_0 = ''; Zg_1 = [''] * 30
    Fn_1 = [''] * Dl_Sel; Fn_2 = [0] * Dl_Sel
    Fn_4 = [0] * Dl_Sel; Fn_5 = [0] * Dl_Sel
    Fn_3 = 0
    Fn_8 = [0] * Dl_Sel
    S3 = [0] * 5; S2 = ['0'] * 6
    S4 = [0] * 91; S5 = [' '] * 3
    N1 = 1; N2 = 120

    Fw1 = open(File_N, 'w', encoding='utf-8', newline='')
    Fw1_1 = open(File_N_1, 'w', encoding='cp1251', newline='')
    Fw4 = open(File_Ekr, 'w')
    # Выходые данные
    with open(File_N0, 'r', encoding='utf-8', newline='') as Fr1:
        # Входные
        dialect = csv.Sniffer().sniff(Fr1.read(1024))
        Fr1.seek(0)
        Sr = csv.reader(Fr1, dialect=dialect, delimiter=';')
        Wr = csv.writer(Fw1, dialect='excel', delimiter=';')
        Wr_1 = csv.writer(Fw1_1, dialect='excel', delimiter=';')

        i = 0; Npc1 = 0
        for St in Sr:
            i = i + 1
            l1 = len(St); i3=0
            if l1 > 21 :
                for i1 in range(l1 - 1) :
                    St2=St[i1]; l2=len(St2)
                    for i2 in range(l2-1):
                        if St2[i2] == '\n': i3=i2
                        continue
                    if i3>0 :
                        St[i1]=St2[:i3]+St2[i3+1:l2]
                    continue
                St1 = ''
                for i1 in range(l1-1):
                    if i1 < Kol_Ps: St1 = St1 + St[Ps[i1]] + ';'
                    else: St1 = St1 + St[i1] + ';'
                    continue
                St1 = St1 + St[l1-1] + '\n'
                Npc= int(i/100000)
                Tt = time.time()
                if Npc > Npc1 : Npc1 = Npc; print(format((Tt - Ct),'.2f'), i, l1, St[4])
                Fw1.write(St1)
            #    Fw1_1.write(St1)
            continue
        Kol_str = i - 1
    Fw1.close()
    Tt0 = time.time()
    print('Количество записей в файле : ', F1, Kol_str)
    Sw1='Количество записей в файле : '+ F1+'  '+str(Kol_str )+'\n'
    Fw4.write(Sw1)
    with open(File_N, encoding='utf-8', newline='') as Tr1:
        S0 = Tr1.readline(); l0 = len(S0)
        S02 = (S0.split(';')); l02 = len(S02)
        j = 0; Nprc=0
        for S1 in Tr1:
            S00 = S1
            #if Fn_3 >400:
            Nprc1=int(100*j/Kol_str)

            if Nprc1 != Nprc :
                Tt1 = time.time(); Ts = format((Tt1-Tt0),'.1f')
                print(Ts, Nprc1, '%', Fn_3, 'Категорий', end='\r')
                Nprc =Nprc1
            j = j + 1
            l1 = len(S1)
            S2 = (S1.split(';')); l2 = len(S2)
            if l2 < 11: break
            Sr2 = S2[Np-1]; Sr = S2[Np-1]
            Sr21 = Sr2; Sr2 = Sr21; Sr20 = Sr2
            Sr1 = Sr.split('/'); l3 = len(Sr1)
            Sr2 = Sr1[l3-1]
            # if l3 > 4: Sr2 = Sr1[l3-2] + '_' + Sr2
            # if l3 > 2: Sr2 = Sr1[1] + '_' + Sr2
            if l3>1 :
                Sr2  = ''
                for i1 in range(1, l3) :
                    if i1 == 1 : Sr2=Sr1[1]
                    else:
                        Sr2=Sr2+'_'+Sr1[i1]
                    continue

            Fsr2 = Sr2 + '.csv'
            Fsr3 = Fsr2.replace(':', '-')
            Fsr3 = Tdr + Fsr3
            il3 = 0; il2 = 0

            for il2 in range(Fn_3+1):
                if il2 == Fn_3:
                    Tr2 = open(Fsr3, 'w', encoding='utf-8')
                    Tr2.write(S0); Tr2.write(S00)
                    Fn_1[il2] = Sr2.replace(':', '-')
                    Fn_2[il2] = 1
                    Fn_8[il2] =j
                    Tr2.close()
                    Fn_3 = Fn_3 + 1
                    break
                if Fn_1[il2] == Sr2:
                    Tr2 = open(Fsr3, 'a', encoding='utf-8')
                    Tr2.write(S00)
                    Fn_2[il2] = Fn_2[il2] + 1
                    Fn_8[il2] =j
                    Tr2.close()
                    # print(j, Fn_3, Fn_2[il2], Sr2)
                    break
            # if Fn_1[il2] == Sr2:
                continue
            continue
# Запись в файл списка всех файлов с кол-вом строк

        with open(Frz4, 'w', encoding='utf-8', newline='') as Tr2:
            Tr2Sr = csv.writer(Tr2, dialect='excel', delimiter=';')

            for il2 in range(Fn_3):
                if len(Fn_1[il2]) < 2:
                    break
                Tr2Str = [str(il2+1), str(Fn_2[il2]), Fn_1[il2], str(Fn_8[il2])]
    
                Tr2Sr.writerow(Tr2Str)
                # print(il2, Tr2Str)
                Sw2= str(il2+1)+'  '+ str(Fn_2[il2])+'  '+ Fn_1[il2]+'  '+ str(Fn_8[il2])+'\n'
                Fw4.write(Sw2)

                continue
        Tr2.close()
    Kol_Kat = Fn_3

    Zg_0 = ''; Zg_1 = [''] * 30
    for i in range(Dl_Sel):
        Fn_1[i] = ''; Fn_2[i] = 0
        Fn_4[i] = 0; Fn_5[i] = 0
        continue
    Fn_3 = 0

    S3 = [0] * 5; S2 = ['0'] * 6
    S4 = [0] * 91; S5 = [' '] * 3
    Vr = [''] * 30; Vrp = [''] * 30
    Vrn = [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 12, 13, 11, 14, 15, 16, 20, 20, 20]

    N1 = 1; N2 = 120
    j = 0
# Столбцы результата
    Zn = 19
# Столбцы счета
    Zng = 8
# Столбец Seller
    N_Sl = 10

# Заголовок
    Zg_10 = ['', '', '', 'Объем рынка ', 'Объем упущ. выручки ',
             'Потенциал рынка', 'Общее кол-во', 'Средний рейтинг',
             'Ср.Кол-во отзывов ', 'Кол-во товаров  ', 'Кол-во пос-ков ',
             'Ср.выручка 1 постав.', 'Выручка ТОП постав.',
             'Доля выручки ТОП постав.', 'Ср.ст-ть товара',
             'Процент пост-kов с продажами', 'Процент товаров с продажами',
             'Кол-во товаров с продажами', '', '', '', '']
    Zg_11 = ['', '', '', 'Revenue', 'Lost profit', 'Reven.pot',
             '  Sales     ', 'Com.Val', ' Comments', 'Name', '       ',
             '        ', '', '', '', '', 'Name, Sales', '', '', '', '']
    Zg_12 = ['Алгоритм(рабочая колонка)', '', '', 'sum(W) ', 'sum(S)',
             'sum(R)', 'sum(V)', 'sum(B)/сount(E)', 'sum(O)/сount(E)',
             ' count(E)', 'количество (count) уникальных значений в списке(M) ',
             'sum(W)/count_uniq_seller ',
             '1. Сортировка по убыванию uniq_seller по соответствующей ему sum(W)',
             'sum(TOP30 revenue uniq_seller)/sum(W)', 'sum(Q)/сount(E)',
             '1. count_uniq_seller', '', '', '', '', '']

    Zg_2 = ['Revenue', 'Lost profit', 'Revenue potential', 'Sales',
            'Comments Valuation', 'Comments', 'Lost profit', 'Final price',
            '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
    Zg_3 = [0] * 30
# Поставщики
    Zg_Sl = 'Seller'
    Rez = [0] * 30; Ri = [0] * 30
    Ct0 = ' '; Ct2 = ' '; Ct5 = ' '
    Pec = [''] * 25

# Задание кодировки вывода

    if Nspf == 0:
        Tr4 = open(File_N2, 'w', encoding='utf-8', newline='')
        Tr4_1 = open(File_N2_1, 'w', encoding='cp1251', newline='')
    else:
        Tr4 = open(File_N2, 'a', encoding='utf-8', newline='')
        Tr4_1 = open(File_N2_1, 'a', encoding='cp1251', newline='')
    Tr4Sr = csv.writer(Tr4, dialect='excel', delimiter=';')
    Tr4Sr_1 = csv.writer(Tr4_1, dialect='excel', delimiter=';')
    if Nspf == 0:
        Tr4Sr.writerow(Zg_10)
        Tr4Sr.writerow(Zg_11)
        Tr4Sr.writerow(Zg_12)

        Tr4Sr_1.writerow(Zg_10)
        Tr4Sr_1.writerow(Zg_11)
        Tr4Sr_1.writerow(Zg_12)
    
    Fn5 = 0; Kol_stt = 0; Prc0 = 0

    with open(Fisx, 'r', encoding='utf-8', newline='') as Tr1:
        SrTr1 = csv.reader(Tr1, dialect='excel', delimiter=';')
        for S0 in SrTr1:
            Fn5 = Fn5 + 1
            l0 = len(S0)
            S02 = S0; l02 = len(S02)
            S022 = S02[2]; L02 = len(S022) - 1
            S023 = S0[2]
            S021 = S0[1]
            S03 = Tdr + S023 + '.csv'
            if len(S03) < 2: break
            Tr3 = open(S03, encoding='utf-8')
            Kol_stt = Kol_stt + int(S021)
            Prc1 = int((Kol_stt / Kol_str) * 100)
            if Prc1 > Prc0 :
                print(Prc1, '% ', Fn5)
                Sw3=str(Prc1)+ '% '+ str(Fn5) +'\n'
                Fw4.write(Sw3)
                Prc0 = Prc1
            for i3 in range(Dl_Sel):
                Fn_4[i3] = 0; Fn_5[i3] = 0
                continue

            Sz_0 = Tr3.readline()
            S04 = Sz_0.split(';'); l02 = len(S04)

            # for i1 in range(Zng):
            #    for i2 in range(l02-1):
            #        if Zg_2[i1] == S04[i2]:
            #            Zg_3[i1] = i2
            #        if Zg_Sl == S04[i2]:
            #            N_Sl = i2
            #        continue
            #    continue

            Zg_3 = [20, 16, 15, 19, 1, 12, 16,14]
            Fn10 = S02[0]; Fn11 = int(S02[1])

            Fn3 = 0; Fn4 = 0; Fn41 = 0; Fn6 = 0; Fn7 = 0
            Ng = 0; i5 = 0
            
            for i1 in range(Zng):
                Rez[i1] = 0
                continue

                # Чтение категории

            for S3 in Tr3:
                S04 = S3.split(';'); l02 = len(S04)
                Zg04 = S04[Np-1]
                Sr1 = Zg04.split('/')
                Ct0 = Sr1[0]

                l3 = len(Sr1)
                
                # if l3>4:    print(l3,' ',Sr1)
                Sr10 = Sr1[0]
                if l3 == 1: Ct2 = Sr1[0]
                if l3 > 1: Ct2 = Sr1[1]
                if l3 > 0: Ct5 = Sr1[l3 - 1]

                Sr24 = Sr1[l3 - 1]

                if l3 > 2: Sr2 = Sr1[1] + '_' + Sr24

                for i1 in range(Zng):
                    Rii = S04[Zg_3[i1]]
                    Ri[i1] = Rii.replace(',', '.')
                    Rez[i1] = Rez[i1] + float(Ri[i1])
                    if i1 == 0: Wr0 = float(Ri[i1])
                    if i1 == 3: Wr1 = int(Ri[i1])
                    if i1 == 4: Wr4 = float(Ri[i1])
                    continue

                if Wr1 > 0: Fn4 = Fn4 + 1; Fn7 = Fn7 + 1
                if Wr4 > 0.1: Fn6 = Fn6 + 1
                
                il3 = 0; il2 = 0
                Sr2 = S04[N_Sl]
                if len(Sr2) == 0: Sr2 = '     '

                # print(Sr2)

                for il2 in range(Fn3 + 1):
                    if il2 == Fn3:
                        Fn_1[il2] = Sr2; Fn_2[il2] = 1
                        
                        if Fn3 > Dl_Sel-2 :
                            print('Велико количество поставщиков')
                            break
                        Fn3 = Fn3 + 1
                        Fn_4[il2] = Wr0; Fn_5[il2] = Wr1
                        break
                    if Fn_1[il2] == Sr2:
                        Fn_2[il2] = Fn_2[il2] + 1
                        Fn_4[il2] = Fn_4[il2] + Wr0
                        Fn_5[il2] = Fn_5[il2] + Wr1
                        break
                    continue
                continue
                        
            Kol_Post = Fn3
            # print(Fn3)
            Vfn = 0; Vfn1 = 0

            for ik1 in range(Fn3 ):
                if Fn_5[ik1] > 0:
                    Vfn = Vfn + 1
                    Vfn1 = Vfn1 + Fn_5[ik1]
                continue
            Vfn1 = round(Vfn1 / (Fn3 + .1))

            for ik1 in range(Fn3 - 1):
                for ik2 in range(Fn3 - 1):
                    if Fn_4[ik2] < Fn_4[ik2 + 1]:
                        Fa1 = Fn_1[ik2]; Fa2 = Fn_2[ik2]
                        Fa4 = Fn_4[ik2]; Fa5 = Fn_5[ik2]
                        Fn_1[ik2] = Fn_1[ik2 + 1]
                        Fn_2[ik2] = Fn_2[ik2 + 1]
                        Fn_4[ik2] = Fn_4[ik2 + 1]
                        Fn_5[ik2] = Fn_5[ik2 + 1]
                        Fn_1[ik2 + 1] = Fa1; Fn_2[ik2 + 1] = Fa2
                        Fn_4[ik2 + 1] = Fa4; Fn_5[ik2 + 1] = Fa5
                    continue
                continue
            
            #for il2 in range(Fn3):
             #   print(Fn_1[il2],'   ', Fn_2[il2],'        ', Fn_4[il2],'   ', Fn_5[il2] )
              #  continue

            Nvb = N_Top
            if N_Top > Fn3: Nvb = int(Fn3 / 3)
            if Nvb < 1 : Nvb=1

            Prf = 0
            for ik1 in range(Nvb):
                Prf = Prf + Fn_4[ik1]
                continue

            Vfn2 = 0
            for il2 in range(Fn3):
                if Fn_5[il2] > 0: Vfn2 = Vfn2 + 1
                continue

            Vr[0] = S023; Fn12 = Fn11
            if Fn11 == 0: Fn12 = 1
            # print((Rez[4]), Fn12)
            if Fn6 == 0: Fn6 = 1
            Rez[4] = Rez[4] / Fn6
            Rez[5] = Rez[5] / Fn12
            Rez[7] = Rez[7] / Fn12
            for i1 in range(Zng):
                if i1 == 4 or i1 == 5: Rp = format(Rez[i1], '.3f')
                else: Rp = str(round(Rez[i1]))
                Vr[i1 + 1] = Rp
                continue
            Vr[7] = str(Fn11)
            Vr[Zng] = str(Fn_3)
            Vr[Zng + 1] = str(Fn3)
            Fn31 = Fn3

            Rp = Rez[0] / Kol_Post
            # print(Rp, Rez[0], Kol_Post)
            Vr[Zng + 2] = str(Rp)
            Rp = Rez[7] 
            Vr[Zng + 3] = format(Rp, '.2f')
            Vr[Zng + 4] = format(Prf, '.2f')
            Vr[Zng + 5] = format(100 * Prf / (Rez[0] + .1), '.2f')
            Vr[Zng + 6] = format(100 * Vfn2 / (Fn3 + .1), '.2f')
            Vr[Zng + 7] = format(100 *( Fn4 / (Fn12)), '.2f')
            Vr[Zng + 8] = str(Fn7)
            for i1 in range(Zn - 1):
                Rii = Vr[i1 + 1]
                Vr[i1 + 1] = Rii.replace('.', ',')
                continue
            # print(Vr)

            Pec[0] = Ct0; Pec[1] = Ct2; Pec[2] = Ct5
            Stp = ''
            Stp = Stp + Ct0 + ';'
            Stp = Stp + Ct2 + ';'
            Stp = Stp + Ct5 + ';'

            for i1 in range(1, Zn):
                Stp = Stp + Vr[Vrn[i1]] + ';'
                Pec[i1 + 2] = Vr[Vrn[i1]]
                continue
            Stp = Stp + '\n'
        # Tr4.write(Stp)

            Tr4Sr.writerow(Pec)
            Tr4Sr_1.writerow(Pec)
            continue
            
            for i3 in range(Dl_Sel):
                Fn_1[i3] = 0; Fn_2[i3] = 0
                Fn_4[i3] = 0; Fn_5[i3] = 0
                continue

    #    Tr4Sr.writerow('\n')
    #    Tr4Sr_1.writerow('\n')
        print()
    Tt =  time.time()
    print(Tt - Ct)
    Fw4.write(format((Tt-Ct),'.2f'))
    Tr4.close()
