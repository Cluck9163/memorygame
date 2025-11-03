import tkinter
#押されたボタンを保存するリスト
opened = []
#ボタンの関数
def b1():
    button1["text"] = "A"
    opened.append(button1["text"])#空の変数にボタンを入れる
def b2():
    button2["text"] = "B"
    opened.append(button2["text"])
def b3():
    button3["text"] = "D"
def b4():
    button4["text"] = "A"
def b5():
    button5["text"] = "B"
def b6():
    button6["text"] = "D"
#二つのボタンを判定する関数
def check_cards():
    i1, i2 = opened
    if i1["text"] != i2["text"]:
        i1["text"] = "C"
        i2["text"] = "C"
        opened.clear()
         
#ウィンドウ、キャンバス
root = tkinter.Tk()
root.title("神経衰弱")
root.geometry("800x700")
canvas  = tkinter.Canvas(root, width=800, height=700, bg="skyblue")
canvas.pack()
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
#ボタンの配置
button1 = tkinter.Button(root, text="C", font=("Times New Roman",40),bg="yellow",command=b1)
button1.place(x=60,y=70) 
button2 = tkinter.Button(root, text="C", font=("Times New Roman",40),bg="yellow",command=b2)
button2.place(x=180,y=70) 
button3 = tkinter.Button(root, text="C", font=("Times New Roman",40),bg="yellow",command=b3)
button3.place(x=300,y=70) 
button4 = tkinter.Button(root, text="C", font=("Times New Roman",40),bg="yellow",command=b4)
button4.place(x=420,y=70) 
button5 = tkinter.Button(root, text="C", font=("Times New Roman",40),bg="yellow",command=b5)
button5.place(x=540,y=70) 
button6 = tkinter.Button(root, text="C", font=("Times New Roman",40),bg="yellow",command=b6)
button6.place(x=660,y=70) 
ubutton1 = tkinter.Button(root, text="C", font=("Times New Roman",40),bg="yellow")
ubutton1.place(x=60,y=270) 
ubutton2 = tkinter.Button(root, text="C", font=("Times New Roman",40),bg="yellow")
ubutton2.place(x=180,y=270) 
ubutton3 = tkinter.Button(root, text="C", font=("Times New Roman",40),bg="yellow")
ubutton3.place(x=300,y=270) 
ubutton4 = tkinter.Button(root, text="C", font=("Times New Roman",40),bg="yellow")
ubutton4.place(x=420,y=270) 
ubutton5 = tkinter.Button(root, text="C", font=("Times New Roman",40),bg="yellow")
ubutton5.place(x=540,y=270) 
ubutton6 = tkinter.Button(root, text="C", font=("Times New Roman",40),bg="yellow")
ubutton6.place(x=660,y=270) 
bubutton1 = tkinter.Button(root, text="C", font=("Times New Roman",40),bg="yellow")
bubutton1.place(x=60,y=470) 
bubutton2 = tkinter.Button(root, text="C", font=("Times New Roman",40),bg="yellow")
bubutton2.place(x=180,y=470) 
bubutton3 = tkinter.Button(root, text="C", font=("Times New Roman",40),bg="yellow")
bubutton3.place(x=300,y=470) 
bubutton4 = tkinter.Button(root, text="C", font=("Times New Roman",40),bg="yellow")
bubutton4.place(x=420,y=470) 
bubutton5 = tkinter.Button(root, text="C", font=("Times New Roman",40),bg="yellow")
bubutton5.place(x=540,y=470) 
bubutton6 = tkinter.Button(root, text="C", font=("Times New Roman",40),bg="yellow")
bubutton6.place(x=660,y=470)
#opened変数のボタンが二つになったら関数を呼ぶ
if opened == 2:
    root.after(1000, check_cards)
root.mainloop()