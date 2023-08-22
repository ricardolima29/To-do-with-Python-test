from tkinter import *
from tkinter import messagebox

from bd import *


################# definindo algumas cores ##############

co0 = "#000000"  # preta
co1 = "#59656F"  
co2 = "#f8f8f2"  # branca
co3 = "#0074eb"  # azul
co4 = "#f04141"  # vermelho
co5 = "#59b356"  # verde
co6 = "#cdd1cd"  # cizenta
co7 = "#282a36"  # Background Dracula 
co8 = "#44475a"  # sub-Background Dracula

################# Criando Janela principal ##############

janela = Tk()
# to prevent the window size from being changed
janela.resizable(width=FALSE, height=FALSE)
janela.geometry('1000x450')
janela.title('To-do')
janela.configure(background=co8)


### dividindo a janela em 2 frames, esquerdo e direito ########
frame_esquerda = Frame(janela, width=450, height=200, bg=co7, relief="flat",)
frame_esquerda.grid(row=0, column=0, sticky=NSEW)
frame_direita = Frame(janela, width=450, height=250, bg=co7,  relief="flat",)
frame_direita.grid(row=0, column=1, sticky=NSEW)

##### dividindo o frame esquerdo em duas partes,cima e baixo ######
frame_e_cima = Frame(frame_esquerda, width=500,
                     height=200, bg=co7, relief="flat",)
frame_e_cima.grid(row=0, column=0, sticky=NSEW)
frame_e_baixo = Frame(frame_esquerda, width=500,
                      height=500, bg=co7, relief="flat",)
frame_e_baixo.grid(row=1, column=0, sticky=NSEW)

##### criando botões no frame frame_e_cima  ########
b_novo = Button(frame_e_cima, text="+ Novo", width=20, height=1, bg=co3, fg="#f8f8f2",
                font="5", anchor="center", relief=RAISED)
b_novo.grid(row=0, column=0,  sticky=NSEW, pady=1)

b_remover = Button(frame_e_cima, text="Remover", width=20, height=1, bg=co4,
                   fg="#f8f8f2", font="5", anchor="center", relief=RAISED)
b_remover.grid(row=0, column=1,  sticky=NSEW, pady=1)

b_atualizar = Button(frame_e_cima, text="Atualizar", width=20, height=1, bg=co5, fg="#f8f8f2",
                     font="5", anchor="center", relief=RAISED)
b_atualizar.grid(row=0, column=2,  sticky=NSEW, pady=1)

######### Adicionando Label e Listbox no frame a direita ########
label = Label(frame_direita, text="Tarefas", width=25, height=1, pady=7,
    padx=10, relief="flat", anchor=W, font=('Courier  15 bold'), bg=co7, fg="#f8f8f2")
label.grid(row=0, column=0,  sticky=NSEW, pady=1)

listbox = Listbox(frame_direita, font=('Arial  9 bold'), width=1)
listbox.grid(row=1, column=0, columnspan=2,  sticky=NSEW, pady=5)

########## adicionando algumas tarefas na Listbox ##########
#tarefas = ["Pagar conta", "Comer", "Jogar VAVA", "dormir"]
#for item in tarefas:
#    listbox.insert(END, item)

    # Inserir tarefas
#with con:
#   cur = con.cursor()


# Inserir tarefas
def inserir(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO tarefa (nome) VALUES (?)"
        cur.execute(query, i)

# Selecionar tarefas
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM tarefa")
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Selecionar tarefas
def selecionar():
    lista_tarefas = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM tarefa")
        rows = cur.fetchall()
        for row in rows:
            lista_tarefas.append(row)
    return lista_tarefas
 
# Deletar tarefas
with con:
    cur = con.cursor()
    cur.execute("DELETE FROM tarefa WHERE id = 3")

# Deletar tarefas
def deletar(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM tarefa WHERE id=?"
        cur.execute(query, i)

# Atualizar tarefas
with con:
    cur = con.cursor()
    cur.execute("UPDATE tarefa SET nome='fazer leitura' WHERE id=2")

# Atualizar tarefas
def atualizar(i):
    with con:
        cur = con.cursor()
        query = "UPDATE tarefa SET nome=? WHERE id=?"
        cur.execute(query, i)


#### função main #####
def main(a):
    ############## novo #############
    if a == 'novo':
        for widget in frame_e_baixo.winfo_children():
            widget.destroy()

        #### função adicionar ###
        def adicionar():
            tarefa_entry = entry.get()
            inserir([tarefa_entry])
            mostrar()
        lb = Label(frame_e_baixo, text="Insira uma nova tarefa", width=80, height=20, pady=15, bg=co8,fg="#f8f8f2")
        lb.grid(row=0, column=0, sticky=NSEW)

        entry = Entry(frame_e_baixo, width=15,)
        entry.grid(row=1, column=0, sticky=NSEW)
        b_adicionar = Button(frame_e_baixo, text="Adicionar", width=10, height=1, bg=co8,pady=10, fg="#f8f8f2", font="8", relief=RAISED, overrelief=RIDGE, command=adicionar)
        b_adicionar.grid(row=2, column=0, sticky=NSEW, pady=15)


    ############## Atualizar ########
    if a == 'atualizar':
        for widget in frame_e_baixo.winfo_children():
            widget.destroy()

        def on():
            lb = Label(frame_e_baixo, text="Atualize a tarefa", width=80, height=20,bg=co8, pady=20,fg="#f8f8f2")
            lb.grid(row=0, column=0, sticky=NSEW)
            entry = Entry(frame_e_baixo, width=15)
            entry.grid(row=1, column=0, sticky=NSEW)

            tarefas = selecionar()
            cs = listbox.curselection()[0]
            s_palavra = listbox.get(cs)
            entry.insert(0, s_palavra)

            ### função atualizar ####
            def alterar():
                for item in tarefas:
                    if s_palavra == item[1]:
                        nova = [entry.get(), item[0]]
                        atualizar(nova)
                        entry.delete(0, END)

                mostrar()

            b_atualizar = Button(frame_e_baixo, text="Atualizar", width=10, height=1, bg=co8,pady=10, fg="#f8f8f2", font="8", relief=RAISED, overrelief=RIDGE, command=alterar)
            b_atualizar.grid(row=2, column=0, sticky=NSEW, pady=15)


        on()


############## Remove #############
def remover():
    cs = listbox.curselection()[0]
    s_palavra = listbox.get(cs)
    tarefas = selecionar()
    for item in tarefas:
        if s_palavra == item[1]:
            deletar([item[0]])

    mostrar()



##### criando botões no frame frame_e_cima  ########
b_novo = Button(frame_e_cima, text="+ Novo", width=10, height=1, bg=co3, fg="white",
                font="5", anchor="center", relief=RAISED, command=lambda: main('novo'))
b_novo.grid(row=0, column=0,  sticky=NSEW, pady=1)

b_remover = Button(frame_e_cima, text="Remover", width=10, height=1, bg=co4,
                   fg="white", font="5", anchor="center", relief=RAISED,command=remover)
b_remover.grid(row=0, column=1,  sticky=NSEW, pady=1)

b_atualizar = Button(frame_e_cima, text="Atualizar", width=10, height=1, bg=co5, fg="#f8f8f2",
                     font="5", anchor="center", relief=RAISED, command=lambda: main('atualizar'))
b_atualizar.grid(row=0, column=2,  sticky=NSEW, pady=1)

######### Adicionando Label e Listbox no frame a direita ########
label = Label(frame_direita, text="Tarefas", width=30, height=1, pady=7,
    padx=10, relief="flat", anchor=W, font=('Courier  20 bold'), bg=co7, fg="#ff79c6")
label.grid(row=0, column=0,  sticky=NSEW, pady=1)

listbox = Listbox(frame_direita, font=('Arial  9 bold'), width=1,height=20,bg=co7,fg="#f8f8f2")
listbox.grid(row=1, column=0, columnspan=2,  sticky=NSEW, pady=5)




############## Mostrar tarefas na Listbox #############
def mostrar():
    listbox.delete(0, END)
    tarefas = selecionar()
    for item in tarefas:
        listbox.insert(END, item[1])
mostrar()


janela.mainloop()