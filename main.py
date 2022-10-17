import tkinter
from tkinter import *
from tkinter import ttk

# Importando Pillow
from PIL import Image, ImageTk

import pytz
import requests
from datetime import datetime
import json
import pycountry_convert as pc

################ CORES ######################
cor0 = "#444466"  # Preta
cor1 = "#FEFFFF"  # Branca
cor2 = "#6F9FBD"  # Azul

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
frame_corpo.grid(row=2, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')


# Função que retorna as informáções
def informacao():
    chave = '1319a1fe5a6650905c4684c52b1ac9f6'
    cidade = e_local.get()
    api_link = "http://api.openweathermap.org/data/2.5/weather?appid=" + chave + "&q=" + cidade

    # Fazendo a chamada da API usando request
    r = requests.get(api_link)

    # Convertendo os dados presentes na variável r em dicionário
    dados = r.json()

    # Obtendo zona, pais e horas
    pais_codigo = dados['sys']['country']

    # ------Zona-------
    zona_fuso = pytz.country_timezones[pais_codigo]

    # ------Pais-------
    pais = pytz.country_names[pais_codigo]

    # ------Data------
    zona = pytz.timezone(zona_fuso[0])
    zona_horas = datetime.now(zona)
    zona_horas = zona_horas.strftime("%d %m %Y | %H:%M:%S %p")

    # ------Tempo------
    tempo = dados['main']['temp']
    pressao = dados['main']['pressure']
    humidade = dados['main']['humidity']
    velocidade = dados['wind']['speed']
    descricao = dados['weather'][0]['description']

    # Mudando informações

    def pais_para_continente(i):
        pais_alpha = pc.country_name_to_country_alpha2(i)
        pais_continente_codigo = pc.country_alpha2_to_continent_code(pais_alpha)
        pais_continente_nome = pc.convert_continent_code_to_continent_name(pais_continente_codigo)

        return pais_continente_nome

    continente = pais_para_continente(pais)

    # Passado informações nas Labels

    l_cidade['text'] = cidade + " - " + pais + " | " + continente
    l_data['text'] = zona_horas
    l_humidade['text'] = humidade
    l_h_simbolo['text'] = "%"
    l_h_nome['text'] = "Humidade"
    l_pressao['text'] = "Pressão : " + str(pressao)
    l_velocidade['text'] = "Velocidade do vento : " + str(velocidade)
    l_descricao['text'] = descricao

    # Logica para trocar o fundo


# Configurando Frame Top
e_local = Entry(frame_top, width=20, justify='left', font=("", 14), highlightthickness=1, relief='solid')
e_local.place(x=15, y=10)

b_ver = Button(frame_top, command=informacao, text='Ver Clima', bg=cor1, fg=cor2, font=("Ivy 9 bold"), relief='raised', overrelief=RIDGE)
b_ver.place(x=250, y=10)

# Configurando Frame Corpo
l_cidade = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=cor1, font=("Arial 14"))
l_cidade.place(x=10, y=4)

l_data = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=cor1, font=("Arial 10"))
l_data.place(x=10, y=54)

l_humidade = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=cor1, font=("Arial 45"))
l_humidade.place(x=10, y=104)

l_h_simbolo = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=cor1, font=("Arial 10 bold"))
l_h_simbolo.place(x=85, y=110)

l_h_nome = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=cor1, font=("Arial 8"))
l_h_nome.place(x=85, y=140)

l_pressao = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=cor1, font=("Arial 10"))
l_pressao.place(x=10, y=184)

l_velocidade = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=cor1, font=("Arial 10"))
l_velocidade.place(x=10, y=214)

imagem = Image.open('img/dia.png')
imagem = imagem.resize((130, 130))
imagem = ImageTk.PhotoImage(imagem)

icon = Label(frame_corpo, image=imagem, bg=fundo)
icon.place(x=160, y=50)

l_descricao = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=cor1, font=("Arial 10"))
l_descricao.place(x=170, y=190)

janela.mainloop()
