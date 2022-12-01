from tkinter import *
from tkinter.ttk import Treeview
import sqlite3
from tkinter import messagebox
import tkinter as tk
from tkinter import END, ttk

amarelo='#ffdd00'
cinza='#D9D9D9'
preto='#000000'
branco='#ffffff'


class cadastro:
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry('1200x650')
        self.janela.title('Gestão de Alunos')
        self.janela.resizable(False, False)

        self.frame0 = Frame(self.janela, bg=amarelo)
        self.frame0.place(x=0, y=0, width=1200, height=650)

    # <------------ Tela para Cadastro de Alunos ------------> #

    def tela_cadastrar_aluno(self):
        #frames
        self.frame_cadastro_alunos = Frame(self.frame0, bg=branco)
        self.frame_cadastro_alunos.place(x=100, y=50, w=1000, h=550)

        self.frame_barra = Frame(self.frame_cadastro_alunos, bg=preto)
        self.frame_barra.place(x=250, y=150, w=600, h=1)

        self.frame_barra = Frame(self.frame_cadastro_alunos, bg=preto)
        self.frame_barra.place(x=250, y=230, w=600, h=1)

        self.frame_barra = Frame(self.frame_cadastro_alunos, bg=preto)
        self.frame_barra.place(x=250, y=310, w=600, h=1)

        #textos
        self.titulo_cadastrar_alunos = Label(self.frame_cadastro_alunos, text='Cadastrar Aluno', font='bold 20', bg=branco)
        self.titulo_cadastrar_alunos.place(x=380, y=20)

        self.informação_nome = Label(self.frame_cadastro_alunos, text='Nome do Aluno:', font='inter 15', bg=branco)
        self.informação_nome.place(x=100, y=120)

        self.informação_turma = Label(self.frame_cadastro_alunos, text='Turma do Aluno:', font='inter 15', bg=branco)
        self.informação_turma.place(x=100, y=200)

        self.informação_turno = Label(self.frame_cadastro_alunos, text='Turno do Aluno:', font='inter 15', bg=branco)
        self.informação_turno.place(x=100, y=280)

        #entrys
        self.entrada_nome = Entry(self.frame_cadastro_alunos, bg=branco, fg=preto, font='inter 12', borderwidth=0)
        self.entrada_nome.place(x=250, y=120, w=600, h=30)

        self.entrada_turma = Entry(self.frame_cadastro_alunos, bg=branco, fg=preto, font='inter 12', borderwidth=0)
        self.entrada_turma.place(x=250, y=200, w=600, h=30)

        self.entrada_turno = Entry(self.frame_cadastro_alunos, bg=branco, fg=preto, font='inter 12', borderwidth=0)
        self.entrada_turno.place(x=250, y=280, w=600, h=30)

        #botões
        self.botao_cadastrar_aluno = Button(self.frame_cadastro_alunos, text='Cadastrar Aluno', fg=preto, font='inter 15', command=self.cadastrar_alunos)
        self.botao_cadastrar_aluno.place(x=300, y=400)

        self.botao_ver_alunos_cadastrados = Button(self.frame_cadastro_alunos, text='Alunos Cadastrados', fg=preto, font='inter 15', command=self.ir_tela_ver_alunos)
        self.botao_ver_alunos_cadastrados.place(x=530, y=400)

        # <------------ Tela para ver Alunos Cadastrados ------------> #

    def alunos_cadastrados(self):
        #frames
        self.frame_alunos_cadastrados = Frame(self.frame0, bg=branco)
        self.frame_alunos_cadastrados.place(x=100, y=50, w=1000, h=550)

        #treeview
        global dados
        #configuração do que vai ter
        self.treeview_alunos_cadastrados = Treeview(self.frame_alunos_cadastrados, columns=('Aluno', 'Turma', 'Turno'), show='headings')
        self.treeview_alunos_cadastrados.column('Aluno', minwidth=0, width=300)
        self.treeview_alunos_cadastrados.column('Turma', minwidth=0, width=100)
        self.treeview_alunos_cadastrados.column('Turno', minwidth=0, width=100)
        #configuração de textos
        self.treeview_alunos_cadastrados.heading('Aluno', text='Aluno')
        self.treeview_alunos_cadastrados.heading('Turma', text='Turma')
        self.treeview_alunos_cadastrados.heading('Turno', text='Turno')
        #configuração de dimensões
        self.treeview_alunos_cadastrados.place(x=55, y=30, w=880, h=400)
        self.ver_alunos()

        #botões
        self.botao_voltar_para_tela_de_cadastro = Button(self.frame_alunos_cadastrados, text='Voltar à tela de cadastro', fg=preto, font='inter 15', command=self.ir_tela_cadastro_alunos)
        self.botao_voltar_para_tela_de_cadastro.place(x=360, y=470)

        self.botao_editar_aluno_cadastrado = Button(self.frame_alunos_cadastrados, text='Editar Aluno', fg=preto, font='inter 15', command=self.editar_aluno_cadastrado)
        self.botao_editar_aluno_cadastrado.place(x=600, y=470)

        self.botao_editar_aluno_cadastrado = Button(self.frame_alunos_cadastrados, text='Excluir Aluno', fg=preto, font='inter 15', command=self.excluir_aluno_cadastrado)
        self.botao_editar_aluno_cadastrado.place(x=800, y=470)

    def limpar_janela(self):
        self.frame0.destroy
        self.frame0 = Frame(self.janela, bg=amarelo)
        self.frame0.place(x=0, y=0, width=1200, height=650)

    def ir_tela_ver_alunos(self):
        self.limpar_janela()
        self.alunos_cadastrados()

    def ir_tela_cadastro_alunos(self):
        self.limpar_janela()
        self.tela_cadastrar_aluno()

    def cadastrar_alunos(self):
        self.banco_de_dados()
        valor1 = self.entrada_nome.get()
        valor2 = self.entrada_turma.get()
        valor3 = self.entrada_turno.get()

        if valor1 == 'Nome' or valor2 == 'Turma' or valor3 == '':
            messagebox.showerror('Controle de Alunos', 'Os campos não podem estar em branco.')
        else:
            self.cursor.execute(
                "INSERT INTO ALUNOS VALUES(:NOME_entry, :TURMA_entry, :TURNO_entry)",
                {
                    'NOME_entry': valor1,
                    'TURMA_entry': valor2,
                    'TURNO_entry': valor3,
                })

            self.dados.commit()
            self.dados.close()
            messagebox.showinfo('Controle_de_Alunos', 'Aluno Cadastrado')

            self.entrada_nome.delete(0, END)
            self.entrada_turma.delete(0, END)
            self.entrada_turno.delete(0, END)

    def selecionar_aluno(self, event):
        self.banco_de_dados()
        global valor_one
        global valor_two
        global valor_tri
        global valor_four
        global valor_five

        self.select = self.treeview_alunos_cadastrados.focus()
        values = self.treeview_alunos_cadastrados.item(self.select, 'values')
        valor_one = values[0]
        valor_two = values[1]
        valor_tri = values[2]
        self.cursor = self.dados.cursor()

    def ver_alunos(self):
        self.banco_de_dados()
        self.cursor.execute('SELECT * FROM ALUNOS')
        self.lista = self.cursor.fetchall()
        count = 0
        for infos in self.lista:
            if count % 2 == 0:
                self.treeview_alunos_cadastrados.insert('', 'end', values=(infos[0], infos[1], infos[2]))
            else:
                self.treeview_alunos_cadastrados.insert('', 'end', values=(infos[0], infos[1], infos[2]))
            count += 1
        self.dados.commit()
        self.treeview_alunos_cadastrados.bind("<ButtonRelease-1>", lambda e: self.selecionar_aluno(e))

    def editar_aluno_cadastrado(self):
        self.banco_de_dados()
        self.cursor.execute("UPDATE ALUNOS SET NOME=?, TURMA=?, TURNO=?, WHERE NOME=?",
                            (self.entrada_nome.get(), self.entrada_turma.get(), self.entrada_turno.get()))
        self.dados.commit()
        messagebox.showinfo('Controle de Alunos', 'Cadastro de Aluno Alterado')
        self.ver_alunos()

    def excluir_aluno_cadastrado(self):
        self.banco_de_dados()
        self.cursor.execute('delete from ALUNOS where NOME=? and TURMA=? and TURNO=?', (valor_one, valor_two, valor_tri))
        self.dados.commit()
        self.ver_alunos()
        messagebox.showinfo('Controle de Alunos', 'Aluno Excluido')

    def banco_de_dados(self):
        self.dados = sqlite3.connect('Controle_de_Alunos.db')
        self.cursor = self.dados.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS ALUNOS(
        NOME,
        TURMA, 
        TURNO)""")

app = cadastro()
app.tela_cadastrar_aluno()
app.janela.mainloop()