from django.shortcuts import render

# Create your views here.

# coding: UTF-8 #日本語を用いるため
import random

deck = [1,2,3,4,5,6,7] #トランプカード
n1 = deck.pop(random.randint(0,len(deck)-1)) #最初の数を決める。random.randint(0,len(deck)-1))でランダムなインデックスを指定。deck.popでリストから数字を抜き出しリストが前につめられる。
print("最初の数は{}です".format(n1))

up = "up"
down = "down"
stay = "stay"

while len(deck) != 0:
    S = input("up,down,stayのいずれかを入力してください:") #プレーヤーがup,down,stayのどれを宣言したかをSに代入
    n2 = deck.pop(random.randint(0,len(deck)-1)) #プレーヤがめくるカード。
    print("あなたが引いたカードは{}です".format(n2))

    if S == up:
        if n1+2 <= n2:
            print("クリア")
        elif n1-1 <= n2 <= n1+1:
            print("ステイミス！2倍飲め！")
        else:
            print("飲め！")
    elif S == down:
        if n2 <= n1-2:
            print("クリア")
        elif n1-1 <= n2 <= n1+1:
            print("ステイミス！2倍飲め！")
        else:
            print("飲め！")
    elif S == stay:
        if n1-1 <= n2 <= n1+1:
            print("クリア") 
        else:
            print("ステイミス！2倍飲め！")
    print("")
    n1=n2
    

print("ゲーム終了！")