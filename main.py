import tkinter
from tkinter import *
from tkinter import ttk

# Importando Pillow
from PIL import Image, ImageTk

################ CORES ######################
cor0 = "#444466"   # Preta
cor1 = "#FEFFFF"   # Branca
cor2 = "#6F9FBD"   # Azul

fundo_dia = "#6CC4CC"
fundo_tarde = "#484F60"
fundo_noite = "#BFB86D"
fundo = fundo_dia

janela = Tk()
janela.title('')
janela.geometry('320x350')
janela.configure(bg=fundo)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

# Criando Frames
frame_top = Frame(janela, width=320, height=50, bg=cor1, pady=0, padx=0)
frame_top.grid(row=1, column=0)

frame_corpo = Frame(janela, width=320, height=300, bg=fundo, pady=12, padx=0)
frame_corpo.grid(row=2, column=0 ,sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

# Configurando Frame Top
e_local = Entry(frame_top, width=20, justify='left', font=("", 14), highlightthickness=1, relief='solid')
e_local.place(x=15, y=10)

b_ver = Button(frame_top, text='Ver Clima',bg=cor1, fg=cor2, font=("Ivy 9 bold"), relief='raised', overrelief=RIDGE)
b_ver.place(x=250, y=10)

# Configurando Frame Corpo
l_cidade = Label(frame_corpo, text='Ver Clima', anchor='center', bg=fundo, fg=cor1, font=("Arial 14"))
l_cidade.place(x=10, y=4)

l_data = Label(frame_corpo, text='Ver Clima', anchor='center', bg=fundo, fg=cor1, font=("Arial 10"))
l_data.place(x=10, y=54)

l_humidade = Label(frame_corpo, text='Ver Clima', anchor='center', bg=fundo, fg=cor1, font=("Arial 45"))
l_humidade.place(x=10, y=104)

l_h_simbolo = Label(frame_corpo, text='Ver Clima', anchor='center', bg=fundo, fg=cor1, font=("Arial 10 bold"))
l_h_simbolo.place(x=85, y=110)

l_h_nome = Label(frame_corpo, text='Ver Clima', anchor='center', bg=fundo, fg=cor1, font=("Arial 8"))
l_h_nome.place(x=85, y=140)

l_pressao = Label(frame_corpo, text='Ver Clima', anchor='center', bg=fundo, fg=cor1, font=("Arial 10"))
l_pressao.place(x=10, y=184)

l_velocidade = Label(frame_corpo, text='Ver Clima', anchor='center', bg=fundo, fg=cor1, font=("Arial 10"))
l_velocidade.place(x=10, y=214)

imagem = Image.open('img/dia.png')
imagem = imagem.resize((130, 130))
imagem = ImageTk.PhotoImage(imagem)

icon = Label(frame_corpo, image=imagem, bg=fundo)
icon.place(x=160, y=50)

l_discricao = Label(frame_corpo, text='Ver Clima', anchor='center', bg=fundo, fg=cor1, font=("Arial 10"))
l_discricao.place(x=170, y=190)

janela.mainloop()