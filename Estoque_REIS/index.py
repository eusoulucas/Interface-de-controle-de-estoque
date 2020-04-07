#import the libraries
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import database

def crud_produtos():

	def mostra_prod():
		classe = lista_classes.get(ACTIVE)
		for item in database.ponta1.execute("SELECT Nome FROM Produtos WHERE Classe = ?", classe):
			lista_produtos.insert(END, item)
	
	def listando_classe():
		classes = database.ponta1.execute("SELECT Classe FROM Produtos")

		lista = []
		lista2 = []

		for item in classes:
			lista.append(item)

		lista_classes.delete(0,1000)

		for i in range(len(lista)):
			if lista[i] in lista2:
				i = i + 1
			else:
				lista2.append(lista[i])
				i = i + 1

		for classe in lista2:
			lista_classes.insert(END, classe)

	def add_produto():

		def adicionar():
			nomep = nomep_en.get()
			classe = classe_en.get()
			tamanho = tamanho_en.get()
			preco = preco_en.get()
			quantidade = quantidade_en.get()
			marca = marca_en.get()

			if(nomep == "" and classe == "" and quantidade == "" and tamanho == "" and preco == "" and marca == ""):
				messagebox.showerror(title = 'Erro de preenchimento', message = 'Preencha todos os campos')
			else:
				database.ponta1.execute("""
				INSERT INTO Produtos(Nome, Classe, Tamanho, Preco, Quantidade, Marca)
				VALUES(?, ?, ?, ?, ?, ?)
				""", (nomep, classe, tamanho, preco, quantidade, marca))
				database.coneccao_products.commit()
				messagebox.showinfo(title = 'Informação de inventario', message = 'Produto adicionado com sucesso!')
				listando_classe()

		janela_add = Tk()
		janela_add.geometry('400x400')
		janela_add.title("Adicionar produtos")
		janela_add.attributes('-alpha', 0.95)
		janela_add.iconbitmap(default = 'logoicone.ico')
		
		titulo_lb = Label(janela_add, text = 'Formulário', bg = 'black', fg = 'white', font = 'Arial 13')
		titulo_lb.place(x ='0', rely = '0.05', relwidth = '1')

		nomep_lb = Label(janela_add, text = 'Nome:', font = 'Arial 11')
		nomep_lb.place(relx = '0.07', rely = '0.155')
		nomep_en = Entry(janela_add, font = 'Arial 11')
		nomep_en.place(relx = '0.3', rely = '0.15', relwidth = '0.6')

		classe_lb = Label(janela_add, text = 'Classe:', font = 'Arial 11')
		classe_lb.place(relx = '0.07', rely = '0.255')
		classe_en = Entry(janela_add, font = 'Arial 11')
		classe_en.place(relx = '0.3', rely = '0.25', relwidth = '0.6')

		tamanho_lb = Label(janela_add, text = 'Tamanho:', font = 'Arial 11')
		tamanho_lb.place(relx = '0.07', rely = '0.355')
		tamanho_en = Entry(janela_add, font = 'Arial 11')
		tamanho_en.place(relx = '0.3', rely = '0.35', relwidth = '0.6')

		preco_lb = Label(janela_add, text = 'Preço:', font = 'Arial 11')
		preco_lb.place(relx = '0.07', rely = '0.455')
		preco_en = Entry(janela_add, font = 'Arial 11')
		preco_en.place(relx = '0.3', rely = '0.45', relwidth = '0.6')

		quantidade_lb = Label(janela_add, text = 'Quantidade:', font = 'Arial 11')
		quantidade_lb.place(relx = '0.07', rely = '0.555')
		quantidade_en = Entry(janela_add, font = 'Arial 11')
		quantidade_en.place(relx = '0.3', rely = '0.55', relwidth = '0.6')

		marca_lb = Label(janela_add, text = 'Marca:', font = 'Arial 11')
		marca_lb.place(relx = '0.07', rely = '0.655')
		marca_en = Entry(janela_add, font = 'Arial 11')
		marca_en.place(relx = '0.3', rely = '0.65', relwidth = '0.6')

		confirm_bt = Button(janela_add, text = 'Adicionar', bg = 'black', fg = 'white', font = 'Arial 11',
			command = adicionar)
		confirm_bt.place(x = '0', rely = '0.85', relwidth = '1', relheight = '0.07')

	def del_produto():
		produto = lista_produtos.get(ACTIVE)
		database.ponta1.execute("DELETE FROM Produtos WHERE Nome = ?", produto)
		database.coneccao_products.commit()
		listando_classe()
		lista_produtos.delete(0,1000)
		mostra_prod()

	def edit_produto():

		def editar():
			nomep = nomep_en.get()
			classe = classe_en.get()
			tamanho = tamanho_en.get()
			preco = preco_en.get()
			quantidade = quantidade_en.get()
			marca = marca_en.get()

			produto = lista_produtos.get(ACTIVE)

			if(nomep == "" and classe == "" and quantidade == "" and tamanho == "" and preco == "" and marca == ""):
				messagebox.showerror(title = 'Erro de preenchimento', message = 'Preencha todos os campos')
			else:
				database.ponta1.execute("""
				UPDATE Produtos
				SET Nome = ?, Classe = ?, Tamanho = ?, Preco = ?, Marca = ?, Quantidade = ?
				WHERE Nome = ?
				""", (nomep, classe, tamanho, preco, marca, quantidade, produto[0]))
				database.coneccao_products.commit()
				messagebox.showinfo(title = 'Informação de inventario', message = 'Produto editado com sucesso!')
				listando_classe()
				lista_produtos.delete(0,1000)
				mostra_prod()

		janela_add = Tk()
		janela_add.geometry('400x400')
		janela_add.title("Editar produtos")
		janela_add.attributes('-alpha', 0.95)
		janela_add.iconbitmap(default = 'logoicone.ico')
		
		titulo_lb = Label(janela_add, text = 'Formulário', bg = 'black', fg = 'white', font = 'Arial 13')
		titulo_lb.place(x ='0', rely = '0.05', relwidth = '1')

		nomep_lb = Label(janela_add, text = 'Nome:', font = 'Arial 11')
		nomep_lb.place(relx = '0.07', rely = '0.155')
		nomep_en = Entry(janela_add, font = 'Arial 11', exportselection = '1')
		nomep_en.place(relx = '0.3', rely = '0.15', relwidth = '0.6')

		classe_lb = Label(janela_add, text = 'Classe:', font = 'Arial 11')
		classe_lb.place(relx = '0.07', rely = '0.255')
		classe_en = Entry(janela_add, font = 'Arial 11')
		classe_en.place(relx = '0.3', rely = '0.25', relwidth = '0.6')

		tamanho_lb = Label(janela_add, text = 'Tamanho:', font = 'Arial 11')
		tamanho_lb.place(relx = '0.07', rely = '0.355')
		tamanho_en = Entry(janela_add, font = 'Arial 11')
		tamanho_en.place(relx = '0.3', rely = '0.35', relwidth = '0.6')

		preco_lb = Label(janela_add, text = 'Preço:', font = 'Arial 11')
		preco_lb.place(relx = '0.07', rely = '0.455')
		preco_en = Entry(janela_add, font = 'Arial 11')
		preco_en.place(relx = '0.3', rely = '0.45', relwidth = '0.6')

		quantidade_lb = Label(janela_add, text = 'Quantidade:', font = 'Arial 11')
		quantidade_lb.place(relx = '0.07', rely = '0.555')
		quantidade_en = Entry(janela_add, font = 'Arial 11')
		quantidade_en.place(relx = '0.3', rely = '0.55', relwidth = '0.6')

		marca_lb = Label(janela_add, text = 'Marca:', font = 'Arial 11')
		marca_lb.place(relx = '0.07', rely = '0.655')
		marca_en = Entry(janela_add, font = 'Arial 11')
		marca_en.place(relx = '0.3', rely = '0.65', relwidth = '0.6')

		confirm_bt = Button(janela_add, text = 'Editar', bg = 'black', fg = 'white', font = 'Arial 11',
			command = editar)
		confirm_bt.place(x = '0', rely = '0.85', relwidth = '1', relheight = '0.07')


	def sobre_prod():
		pass

	janela_inv = Tk()
	janela_inv.title('Inventário')
	janela_inv.geometry("700x600")
	janela_inv.attributes('-alpha', 0.95)
	janela_inv.iconbitmap(default = 'logoicone.ico')

	frame_classes = Frame(janela_inv, bg = 'black')
	frame_classes.place(relx = '0', rely = '0', relwidth = '0.3', relheight = '1')

	label_classes = Label(frame_classes, text = 'Classes', font = 'Arial 13', bg = 'white')
	label_classes.place(relx = '0', rely = '0.05', relwidth = '1')

	frame_produtos = Frame(janela_inv, bg = 'white')
	frame_produtos.place(relx = '0.3', rely = '0', relwidth = '0.7', relheight = '1')

	label_produtos = Label(frame_produtos, text = 'Produtos', font = 'Arial 13', bg = 'black', fg = 'white')
	label_produtos.place(relx = '0', rely = '0.05', relwidth = '1')

	lista_classes = Listbox(frame_classes, bg = 'white', fg = 'black', font = 'Arial 12', relief = 'groove',
		selectmode = 'SINGLE', selectbackground = 'gray', yscrollcommand = 'TRUE')
	lista_classes.place(relx = '0.09', rely = '0.12', relwidth = '0.8', relheight = '0.75')

	listando_classe()
	
	lista_produtos = Listbox(frame_produtos, bg = 'black', fg = 'white', font = 'Arial 12',
		selectmode = 'SINGLE', selectbackground = 'gray')
	lista_produtos.place(relx = '0.09', rely = '0.12', relwidth = '0.8', relheight = '0.75')

	bt_addprod = Button(frame_produtos, bg = 'black', fg = 'white', text = "Adicionar", 
	 	font = 'Arial 11', command = add_produto)
	bt_addprod.place(relx = '0.05', rely = '0.9', relwidth = '0.24', relheight = '0.06')

	bt_delprod = Button(frame_produtos, bg = 'black', fg = 'white', text = "Deletar", 
	 	font = 'Arial 11', command = del_produto)
	bt_delprod.place(relx = '0.30', rely = '0.9', relwidth = '0.24', relheight = '0.06')

	bt_editprod = Button(frame_produtos, bg = 'black', fg = 'white', text = "Editar", 
	 	font = 'Arial 11', command = edit_produto)
	bt_editprod.place(relx = '0.55', rely = '0.9', relwidth = '0.24', relheight = '0.06')

	bt_info = Button(frame_produtos, bg = 'black', fg = 'white', text = "Sobre", 
	 	font = 'Arial 11', command = sobre_prod)
	bt_info.place(relx = '0.8', rely = '0.9', relwidth = '0.15', relheight = '0.06')

	bt_mostraprod = Button(frame_classes, text = "Abrir classe", bg = 'white', fg = 'black',
	 	font = 'Arial 11', command = mostra_prod)
	bt_mostraprod.place(relx = '0.08', rely = '0.901', relwidth = '0.85', relheight = '0.055')

def logar():
	usuario = usuario_en.get()
	senha = senha_en.get()

	database.ponta.execute('''
		SELECT * FROM Usuarios
		WHERE (usuario = ? and senha = ?)
		''', (usuario, senha))

	verificar = database.ponta.fetchone()

	if(usuario in verificar and senha in verificar):
		janela_main.destroy()
		crud_produtos()
	else:
		messagebox.showerror(title = "Informação de login", message = "Dados incorretos ou usuário inexistente")	

def registrar():
	def voltar():
		#removendo widgets
		botao_registrar.place(rely = '1000')
		botao_voltar.place(rely = '1000')
		nome_lb.place(relx = '1000')
		nome_en.place(relx = '1000')
		mail_lb.place(relx = '1000')
		mail_en.place(relx = '1000')

		#voltando os outros botoes
		botao_login.place(rely = '0.52', relx = '0.2')
		botao_registro.place(rely = '0.65', relx = '0.2')

	def registrardb():
		nome = nome_en.get()
		usuario = usuario_en.get()
		senha = senha_en.get()
		mail = mail_en.get()
		
		if(nome == "" and mail == "" and senha == "" and usuario == ""):
			messagebox.showerror(title = 'Erro de registro', message = 'Preencha todos os campos')
		else:
			database.ponta.execute("""
			INSERT INTO Usuarios(Nome, Email, Usuario, Senha)
			VALUES(?, ?, ?, ?)
			""", (nome, mail, usuario, senha))
			database.coneccao_user.commit()
			messagebox.showinfo(title = 'Informação de Registro', message = 'Conta criada com sucesso!')

	# gambiarra pra remover botôes
	botao_login.place(relx = '1000000')
	botao_registro.place(relx = '1000000')

	#inserindo widgets de cadastro
	nome_lb = Label(login, text = 'Nome:', bg = 'black', fg = 'white', font = ("Century Ghotic", 12))
	nome_lb.place(relx = '0.07', rely = '0.1')

	nome_en = ttk.Entry(login)
	nome_en.place(relx = '0.17', rely = '0.11', relwidth = '0.35')

	mail_lb = Label(login, text = 'E-Mail:', bg = 'black', fg = 'white', font = ("Century Ghotic", 12))
	mail_lb.place(relx = '0.06', rely = '0.54')

	mail_en = ttk.Entry(login)
	mail_en.place(relx = '0.17', rely = '0.55', relwidth = '0.35')

	#inserindo botões do cadastro
	botao_registrar = ttk.Button(login, text = 'Salvar', command = registrardb)
	botao_registrar.place(rely = '0.67', relx = '0.2')

	botao_voltar = ttk.Button(login, text = 'Voltar', command = voltar)
	botao_voltar.place(rely = '0.80', relx = '0.2')

janela_main = Tk()
janela_main.title('LE Sistemas - Painel de Acesso')
janela_main.geometry('600x300')
janela_main.configure(bg = 'white')
janela_main.attributes('-alpha', 0.95)
janela_main.iconbitmap(default = 'logoicone.ico')

logo = PhotoImage(file = 'logo.png')

logo_reis = Frame(janela_main)
logo_reis.place( relheight = '1', relwidth = '0.45')

login = Frame(janela_main, bg = 'black')
login.place(relx = '0.45', relheight = '1', relwidth = '1')

logo_lb = Label(logo_reis, image = logo)
logo_lb.place(relx = '0.2', rely = '0.2')

usuario_lb = Label(login, text = 'Usuário:', bg = 'black', fg = 'white', font = ("Century Ghotic", 12))
usuario_lb.place(relx = '0.05', rely = '0.25')

usuario_en = ttk.Entry(login)
usuario_en.place(relx = '0.17', rely = '0.26', relwidth = '0.35')

senha_lb = Label(login, text = 'Senha:', bg = 'black', fg = 'white', font = ("Century Ghotic", 12))
senha_lb.place(relx = '0.06', rely = '0.4')

senha_en = ttk.Entry(login, show = '*')
senha_en.place(relx = '0.17', rely = '0.41', relwidth = '0.35')

botao_login = ttk.Button(login, text = 'Log in', command = logar)
botao_login.place(rely = '0.52', relx = '0.2')

botao_registro = ttk.Button(login, text = 'Registrar', command = registrar)
botao_registro.place(rely = '0.65', relx = '0.2')

janela_main.mainloop()