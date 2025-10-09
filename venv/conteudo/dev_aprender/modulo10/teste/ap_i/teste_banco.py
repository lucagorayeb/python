import sqlite3

con = sqlite3.connect('banco_de_teste.db')
sql = con.cursor()

# Criando a tabela jogadores para fazer o teste de CRUD
sql.execute("CREATE TABLE IF NOT EXISTS jogadores(Id_jogadores INTEGER PRIMARY KEY AUTOINCREMENT, Nome TEXT, Equipe TEXT);")
# Fazendo a inserção de dados na tabela para depois executar um crud 
sql.execute("INSERT INTO jogadores (Nome, Equipe) VALUES ('Philippe Coutinho', 'Vasco da gama'), ('Gabriel Pec', 'LAGalax'),('Douglas Luiz', 'Juventus');")

# Criando uma tabela de gerentes do banco de dados 
sql.execute("CREATE TABLE IF NOT EXISTS gerentes(Id_gerente INTEGER PRIMARY KEY AUTOINCREMENT, Nome TEXT, Email TEXT, Senha INT)")
# Inserindo dados na tabela gerentes
sql.execute("INSERT INTO gerentes (Nome, Email, Senha) VALUES ('Luca Siqueira Assis Gorayeb de Mello', 'lucagorayeb@gmail.com', 123456)")

# Fazendo select da tabela jogadores 
#print (sql.execute("SELECT * FROM jogadores").fetchall())
#print (sql.execute("SELECT * FROM gerentes").fetchall())

con.commit()