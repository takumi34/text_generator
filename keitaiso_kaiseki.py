from natto import MeCab

import os
import csv 
import random
import pandas as pd


fp = open("sakaguchi_sakura.txt") #坂口安吾『桜の森の満開の下』（１９４７）、青空文庫<http://www.aozora.gr.jp/cards/001095/files/42618_21410.html>
doc = fp.read()

nm = MeCab("-Ochasen") #茶筅形式に出力フォーマットを変更

list_keitaiso = [i.split() for i in nm.parse(doc).splitlines()]

fp2= open('sakura_keitaiso.csv', 'ab') 
 
with open('sakura_keitaiso.csv','a') as fp2:
    writer = csv.writer((fp2), lineterminator="\n")
    for i in range(0,len(list_keitaiso)):
        writer.writerow(list_keitaiso[i]) #CSVファイルに書き出し


df = pd.read_csv('sakura_keitaiso.csv',names=('a','b','c','d','e','f'))
meishi = list(df[df['d']=='名詞-一般']['a'])
doushi = list(df[(df['d']=='動詞-自立') & (df['f']=='連用タ接続') ]['a'])


num1 = random.randint(0,len(doushi)-1)

num2 = random.randint(1,len(meishi)-1)


print(str(meishi[num2]) +"が" + str(doushi[num1]) + "たから遅れちゃうじゃー♪") #テキスト生成
 
