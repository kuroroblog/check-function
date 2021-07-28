################################################
# <前提条件>
# ・コードは上から順に実行される。
################################################

################################################
# <実行順序>
# 1. pattern1()関数が実行されます。(def pattern1, def pattern2, def pattern3, def argsSample1, def argsSample2は、定義しているのであって、呼び出さないと実行されない。def pattern1, def pattern2, def pattern3, def argsSample1, def argsSample2を関数と呼ぶ。)
# 2. pattern1()内のprint文が実行される。pattern1が出力される。
# 3. pattern1()の戻り値をprint文で出力する。戻り値を設定しないため、Noneが出力される。
# 4. pattern2()関数が実行されます。
# 5. pattern2()内のprint文が実行される。pattern2が出力される。
# 6. pattern2()の戻り値をprint文で出力する。return文は宣言されているが、戻り値は設定されてないため、Noneが出力される。
# 7. pattern3()関数が実行されます。
# 8. pattern3()内のprint文が実行される。pattern3が出力される。
# 9. pattern3()の戻り値をprint文で出力する。戻り値としてhogeが設定されているため、hogeが出力される。
# 10. argsSample1(name)関数が実行されます。(第一引数としてpiyoの値をnameへ格納する。)
# 11. argsSample1(name)内のprint文が実行される。nameへpiyoの値が格納されているので、piyoが出力される。
# 12. argsSample1(name)の戻り値をprint文で出力する。戻り値を設定しないため、Noneが出力される。
# 13. argsSample2(name1, name2)関数が実行されます。(第一引数としてaaaの値をname1へ、第二引数としてbbbの値をname2へ格納する。)
# 14. argsSample2(name1, name2)内のprint文が実行される。name1へaaa, name2へbbbの値が格納されているので、aaa bbbが出力される。
# 15. argsSample2(name1, name2)の戻り値をprint文で出力する。戻り値を設定しないため、Noneが出力される。
################################################

# 引数なし
# 引数とは? : https://wa3.i-3-i.info/word1442.html
# returnを使って戻り値を設定しない場合、省略できる。
# 戻り値とは? : https://e-words.jp/w/%E6%88%BB%E3%82%8A%E5%80%A4.html
def pattern1():
    # printについて : https://note.nkmk.me/python-print-basic/
    print('pattern1')

# 引数なし
# 引数とは? : https://wa3.i-3-i.info/word1442.html
# returnを使って戻り値を設定しない場合でもreturnと記述できる。(処理はpattern1と変わらない)
# 戻り値とは? : https://e-words.jp/w/%E6%88%BB%E3%82%8A%E5%80%A4.html
def pattern2():
    # printについて : https://note.nkmk.me/python-print-basic/
    print('pattern2')
    return

# 引数なし
# 引数とは? : https://wa3.i-3-i.info/word1442.html
# returnを使って戻り値を設定する場合、return 戻り値とする。
# 戻り値とは? : https://e-words.jp/w/%E6%88%BB%E3%82%8A%E5%80%A4.html
def pattern3():
    # printについて : https://note.nkmk.me/python-print-basic/
    print('pattern3')
    # returnの戻り値の設定の仕方はその他にもたくさんある。
    # 参考 : https://note.nkmk.me/python-function-return-multiple-values/
    return 'hoge'

# name : 第一引数
# 引数とは? : https://wa3.i-3-i.info/word1442.html
# returnを使って戻り値を設定しない場合、省略できる。
# 戻り値とは? : https://e-words.jp/w/%E6%88%BB%E3%82%8A%E5%80%A4.html
def argsSample1(name):
    # printについて : https://note.nkmk.me/python-print-basic/
    print(name)

# 第一引数 : name1
# 第二引数 : name2
# 引数とは? : https://wa3.i-3-i.info/word1442.html
# returnを使って戻り値を設定しない場合、省略できる。
# 戻り値とは? : https://e-words.jp/w/%E6%88%BB%E3%82%8A%E5%80%A4.html
def argsSample2(name1, name2):
    # printについて : https://note.nkmk.me/python-print-basic/
    print(name1, name2)

print(pattern1())
print(pattern2())
print(pattern3())
print(argsSample1('piyo'))
print(argsSample2('aaa', 'bbb'))
