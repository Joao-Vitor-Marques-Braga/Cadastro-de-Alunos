from tkinter import *

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

    def cadastrar_aluno(self):
        #frames
        self.frame_cadastro_alunos = Frame(self.frame0, bg=branco)
        self.frame_cadastro_alunos.place(x=100, y=50, w=1000, h=550)

        #textos
        self.titulo_cadastrar_alunos = Label(self.frame_cadastro_alunos, text='Cadastrar Aluno', font='bold 20', bg=branco)
        self.titulo_cadastrar_alunos.place(x=380, y=20)

        self.informação_nome = Label(self.frame_cadastro_alunos, text='Nome do Aluno:', font='inter 15', bg=branco)
        self.informação_nome.place(x=100, y=120)

        self.informação_turma = Label(self.frame_cadastro_alunos, text='Turma do Aluno:', font='inter 15', bg=branco)
        self.informação_turma.place(x=100, y=200)

        self.informação_turno = Label(self.frame_cadastro_alunos, text='Turma do Aluno:', font='inter 15', bg=branco)
        self.informação_turno.place(x=100, y=280)

        #entrys
        self.entrada_nome = Entry(self.frame_cadastro_alunos, bg=branco, fg=preto)

app = cadastro()
app.cadastrar_aluno()
app.janela.mainloop()