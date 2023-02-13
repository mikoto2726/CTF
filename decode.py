#! /usr/bin/python3
import uu

# 抽出したデータ
b=b'begin 666 <data>\n51DQ!1U]&94QG4#-3:4%797I74$AU\n \nend\n'
# バイナリとして上記変数「b」を保存する
with open('aaa.dat', mode='w+b') as fp:
        fp.write(b)
# 出力したdatファイルを読み込んでuuでコード
uu.decode('aaa.dat', 'o.txt')