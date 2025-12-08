import tkinter
from tkinter import ttk
import random
import winsound
#押されたボタンを保存するリスト
opened = []
#プレイヤーの変数
player = 1
root = tkinter.Tk()
root.title("神経衰弱")
root.geometry("800x800")
canvas  = tkinter.Canvas(root, width=800, height=800, bg="skyblue")
canvas.pack()
canvas_end = tkinter.Canvas(root, width=800, height=800, bg="skyblue")
canvas_end.pack_forget
#文字を保管する変数
letters = ["A","A","B","B","J","J","D","D","E","E","F","F","G","G","H","H","I","I"]
random.shuffle(letters)
#効果音の関数
def sound1():
    winsound.PlaySound("maou_se_8bit08.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
    b1()
def sound2():
    winsound.PlaySound("maou_se_8bit08.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
    b2()
def sound3():
    winsound.PlaySound("maou_se_8bit08.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
    b3()
def sound4():
    winsound.PlaySound("maou_se_8bit08.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
    b4()
def sound5():
    winsound.PlaySound("maou_se_8bit08.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
    b5()
def sound6():
    winsound.PlaySound("maou_se_8bit08.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
    b6()
def se1():
    winsound.PlaySound("maou_se_8bit08.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
    ub1()
def se2():
    winsound.PlaySound("maou_se_8bit08.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
    ub2()
def se3():
    winsound.PlaySound("maou_se_8bit08.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
    ub3()
def se4():
    winsound.PlaySound("maou_se_8bit08.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
    ub4()
def se5():
    winsound.PlaySound("maou_se_8bit08.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
    ub5()
def se6():
    winsound.PlaySound("maou_se_8bit08.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
    ub6()
def sse1():
    winsound.PlaySound("maou_se_8bit08.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
    bub1()
def sse2():
    winsound.PlaySound("maou_se_8bit08.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
    bub2()

def sse3():
    winsound.PlaySound("maou_se_8bit08.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
    bub3()

def sse4():
    winsound.PlaySound("maou_se_8bit08.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
    bub4()

def sse5():
    winsound.PlaySound("maou_se_8bit08.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
    bub5()

def sse6():
    winsound.PlaySound("maou_se_8bit08.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
    bub6()
# 押されたボタンを管理するリスト
buttons = 0
buttons = int(buttons)
#ボタンの関数
def b1():
    global buttons
    button1.config(image="",text=letters[0])
    opened.append(button1)#空の変数にボタンを入れる
    if len(opened)==2:
        root.after(1000, check_cards)

def b2():
    global buttons
    button2.config(image="",text=letters[1])
    opened.append(button2)
    if len(opened) == 2:
        root.after(1000, check_cards)
def b3():
    global buttons
    button3.config(image="",text=letters[2])
    opened.append(button3)
    if len(opened) == 2:
        root.after(1000, check_cards)

def b4():
    global buttons
    button4.config(image="",text=letters[3])
    opened.append(button4)
    if len(opened) == 2:
        root.after(1000, check_cards)

def b5():
    global buttons
    button5.config(image="",text=letters[4])
    opened.append(button5)
    if len(opened) == 2:
        root.after(1000, check_cards)

def b6():
    global buttons
    button6.config(image="",text=letters[5])
    opened.append(button6)
    if len(opened) == 2:
        root.after(1000, check_cards)

def ub1():
    global buttons
    ubutton1.config(image="",text=letters[6])
    opened.append(ubutton1)
    if len(opened) == 2:
        root.after(1000,check_cards)
def ub2():
    global buttons
    ubutton2.config(image="",text=letters[7])
    opened.append(ubutton2)
    if len(opened) == 2:
        root.after(1000, check_cards)

def ub3():
    global buttons
    ubutton3.config(image="",text=letters[8])
    opened.append(ubutton3)
    if len(opened) == 2:
        root.after(1000, check_cards)

def ub4():
    global buttons
    ubutton4.config(image="",text=letters[9])
    opened.append(ubutton4)
    if len(opened) == 2:
        root.after(1000, check_cards)

def ub5():
    global buttons
    ubutton5.config(image="", text=letters[10])
    opened.append(ubutton5)
    if len(opened) == 2:
        root.after(1000, check_cards)

def ub6():
    global buttons
    ubutton6.config(image="", text=letters[11])
    opened.append(ubutton6)
    if len(opened) == 2:
        root.after(1000, check_cards)

def bub1():
    global buttons
    bubutton1.config(image="",text=letters[12])
    opened.append(bubutton1)
    if len(opened) == 2:
        root.after(1000, check_cards)

def bub2():
    global buttons
    bubutton2.config(image="", text=letters[13])
    opened.append(bubutton2)
    if len(opened) == 2:
        root.after(1000, check_cards)

def bub3():
    global buttons
    bubutton3.config(image="",text=letters[14])
    opened.append(bubutton3)
    if len(opened) == 2:
        root.after(1000, check_cards)

def bub4():
    global buttons
    bubutton4.config(image="", text=letters[15])
    opened.append(bubutton4)
    if len(opened) == 2:
        root.after(1000, check_cards)

def bub5():
    global buttons
    bubutton5.config(image="",text=letters[16])
    opened.append(bubutton5)
    if len(opened) == 2:
        root.after(1000, check_cards)

def bub6():
    global buttons
    bubutton6.config(image="",text=letters[17])
    opened.append(bubutton6)
    if len(opened) == 2:
        root.after(1000, check_cards)


#二つのボタンを判定する関数
def check_cards():
    global buttons
    global player
    global player_score1
    global player_score2
    i1, i2 = opened
    if i1["text"] != i2["text"]:#ボタンのテクストが違ったら元に戻す
        i1.config(text="", image=back_card)
        i2.config(text="", image=back_card)
        if player == 1:
            player = 2
        else:
            player = 1
        opened.clear()
    elif i1["text"] == i2["text"]:#ボタンがそろった瞬間そのボタンを消す
        i1.destroy()
        i2.destroy()
        buttons += 2
        opened.clear()
        if player == 1:
            player_score1["text"] += 1
            player = 1
        else:
            player_score2["text"] += 1
            player = 2
    if buttons==18:
        print("はんのうはしてんだよな")
        result_win = tkinter.Label(canvas_end, text="結果",font=("Times New Roman",80),bg="skyblue")
        if player_score1["text"] > player_score2["text"]:
            result_win_text = "プレイヤー1の勝利"
            result_about = player_score1["text"]
        elif player_score2["text"] > player_score1["text"]:
            result_win_text = "プレイヤー2の勝利"
            result_about = player_score2["text"]
        else:
            result_win_text = "引き分け"
        result_win = tkinter.Label(canvas_end, text=result_win_text, font=("Times New Roman",40),bg="skyblue")
        result_win.place(x=200, y=200)
        result_about = tkinter.Label(canvas_end, text=result_about, font=("Times New Roman",70),bg="skyblue")
        result_about.place(x=400, y=300)
        canvas.pack_forget()
        canvas_end.pack()
        root.after(5000, window_closed)
def window_closed():
    root.destroy()
#赤色シートの配置
card_width=100
card_height=100
gap=20
for a in range(6):
    x1 = a*(card_width+gap)+50
    x2 = x1 + card_width
    canvas.create_rectangle(x1,50,x2,200,fill="red",outline="red",width=2)
for b in range(6):
    x1 = b*(card_width+gap)+50
    x2 = x1 + card_width
    canvas.create_rectangle(x1,250,x2,400,fill="red",outline="red",width=2)
for c in range(6):
    x1 = c*(card_width+gap)+50
    x2 = x1 + card_width
    canvas.create_rectangle(x1,450,x2,600,fill="red",outline="red",width=2)
#得点を表示するラベル
player_score1 = tkinter.Label(root, text=0, font=("Times New Roman",80),bg="skyblue")
player_score1.place(x=60, y=650)
player_score2 = tkinter.Label(root, text=0, font=("Times New Roman",80),bg="skyblue")
player_score2.place(x=660, y=650)
#画像を読み込む
back_card = tkinter.PhotoImage(file="New Piskel.png")
#ボタンの配置
button1 = tkinter.Button(root, image=back_card, font=("Times New Roman",40),bg="yellow",command=sound1)
button1.place(x=60,y=70) 
button2 = tkinter.Button(root, image=back_card, font=("Times New Roman",40),bg="yellow",command=sound2)
button2.place(x=180,y=70) 
button3 = tkinter.Button(root, image=back_card, font=("Times New Roman",40),bg="yellow",command=sound3)
button3.place(x=300,y=70) 
button4 = tkinter.Button(root, image=back_card, font=("Times New Roman",40),bg="yellow",command=sound4)
button4.place(x=420,y=70) 
button5 = tkinter.Button(root, image=back_card, font=("Times New Roman",40),bg="yellow",command=sound5)
button5.place(x=540,y=70) 
button6 = tkinter.Button(root, image=back_card, font=("Times New Roman",40),bg="yellow",command=sound6)
button6.place(x=660,y=70) 
ubutton1 = tkinter.Button(root, image=back_card, font=("Times New Roman",40),bg="yellow",command=se1)
ubutton1.place(x=60,y=270) 
ubutton2 = tkinter.Button(root, image=back_card, font=("Times New Roman",40),bg="yellow",command=se2)
ubutton2.place(x=180,y=270) 
ubutton3 = tkinter.Button(root, image=back_card, font=("Times New Roman",40),bg="yellow",command=se3)
ubutton3.place(x=300,y=270) 
ubutton4 = tkinter.Button(root, image=back_card, font=("Times New Roman",40),bg="yellow",command=se4)
ubutton4.place(x=420,y=270) 
ubutton5 = tkinter.Button(root, image=back_card, font=("Times New Roman",40),bg="yellow",command=se5)
ubutton5.place(x=540,y=270) 
ubutton6 = tkinter.Button(root, image=back_card, font=("Times New Roman",40),bg="yellow",command=se6)
ubutton6.place(x=660,y=270) 
bubutton1 = tkinter.Button(root, image=back_card, font=("Times New Roman",40),bg="yellow",command=sse1)
bubutton1.place(x=60,y=470) 
bubutton2 = tkinter.Button(root, image=back_card, font=("Times New Roman",40),bg="yellow",command=sse2)
bubutton2.place(x=180,y=470) 
bubutton3 = tkinter.Button(root, image=back_card, font=("Times New Roman",40),bg="yellow",command=sse3)
bubutton3.place(x=300,y=470) 
bubutton4 = tkinter.Button(root, image=back_card, font=("Times New Roman",40),bg="yellow",command=sse4)
bubutton4.place(x=420,y=470) 
bubutton5 = tkinter.Button(root, image=back_card, font=("Times New Roman",40),bg="yellow",command=sse5)
bubutton5.place(x=540,y=470) 
bubutton6 = tkinter.Button(root, image=back_card, font=("Times New Roman",40),bg="yellow",command=sse6)
bubutton6.place(x=660,y=470)

root.mainloop()