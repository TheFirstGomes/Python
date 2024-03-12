from tkinter import * 
from tkinter import messagebox
import tkinter

#Colors ----------------------------
cor0 = "#444466"   #Preta
cor1 = "#feffff"   #Branca
cor2 = "#004338"   #

#Create Windows ---------------------
windows = Tk()
windows.geometry("530x205")
windows.configure(bg=cor1)

#Set Windows ----------------------------------------------------
tela = Label(windows, bg=cor0, bd=1, width=40, height=10)
tela.grid(row=0, column=0)

frame_direita = Frame(windows, bg=cor1)
frame_direita.grid(row=0, column=1, padx=5)

frame_baixo = Frame(windows, bg=cor1)
frame_baixo.grid(row=1, column=0, columnspan=2, pady=15)

# Function Scale ------------------------------------------------------------------------------------------------------------------------------
def escala(valor):
    r = slide_red.get()
    g = slide_green.get()
    b = slide_blue.get()

    rgb = f'{r}, {g}, {b}'
    
    hexadecimal = "#%02x%02x%02x" % (r, g, b)

    #Alterando o fundo da tela ------------------------------------------------------------------------------------------------------------------
    tela['bg'] = hexadecimal

    #Alterando a entry --------------------------------------------------------------------------------------------------------------------------
    enter_color.delete(0, END)
    enter_color.insert(0, hexadecimal)

# Function Click --------------------------------------------------------------------------------------------------------------------------------
def onClick():
    #Informar
    tkinter.messagebox.showinfo("Cor", "A cor foi copiada")
    #Criar o botão de copiar
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(enter_color.get())
    clip.destroy()

#Set Frame Direita --------------------------------------------------
left_red= Label(frame_direita, text="Red", width=7, bg=cor1, fg="red", anchor="nw", font=("Times New Roman" ,12, "bold"))
left_red.grid(row=0, column=0)
slide_red=Scale(frame_direita, from_=0, to=255, length=150, bg=cor1, fg="red", orient=HORIZONTAL, command=escala)
slide_red.grid(row=0, column=1)

left_green= Label(frame_direita, text="Green", width=7, bg=cor1, fg="green", anchor="nw", font=("Times New Roman" ,12, "bold"))
left_green.grid(row=1, column=0)
slide_green=Scale(frame_direita, from_=0, to=255, length=150, bg=cor1, fg="green", orient=HORIZONTAL, command=escala)
slide_green.grid(row=1, column=1)

left_blue= Label(frame_direita, text="Blue", width=7, bg=cor1, fg="blue", anchor="nw", font=("Times New Roman" ,12, "bold"))
left_blue.grid(row=2, column=0)
slide_blue=Scale(frame_direita, from_=0, to=255, length=150, bg=cor1, fg="blue", orient=HORIZONTAL, command=escala)
slide_blue.grid(row=2, column=1)

#Set Frame Baixo --------------------------------------------------
label_rgb= Label(frame_baixo, text="CÓDIGO HEX : ", bg=cor1, font=("Ivy" ,10, "bold"))
label_rgb.grid(row=0, column=0, padx=5)

enter_color = Entry(frame_baixo, width=12, font=("Ivy", 12, "bold"), justify=CENTER)
enter_color.grid(row=0, column=1, padx=5)

# button for copy -----------------------------------------------------------------------------------------------------------------------------
btt_copy= Button(frame_baixo, text="Copiar a cor", bg=cor1, font=("Ivy" ,8, "bold"), relief=RAISED, overrelief=RIDGE, command=onClick)
btt_copy.grid(row=0, column=2, padx=5)

# app nome -----------------------------------------------------------------------------------------------------------------------------
label_app_nome= Label(frame_baixo, text="Seletor de Cores", bg=cor1, font=("Ivy" ,12, "bold"))
label_app_nome.grid(row=0, column=3, padx=40)

#Start ----------------------------------------------------------------------
windows.mainloop()
