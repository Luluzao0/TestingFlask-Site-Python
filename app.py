from flask import Flask, render_template, request, redirect, url_for, flash
from models import db

app = Flask(__name__)
app.secret_key = 'xN$$j56%{)~]ADn_{2-_{O'

@app.route('/')
def homepage():  # put application's code here
    return render_template("homepage.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        #conecta ao banco e insere os dados:
        cursor = db.cursor()
        cursor.execute('INSERT INTO usuario(nome, email, senha) VALUES (%s, %s, %s)', (nome, email, senha))
        db.commit()
        cursor.close()

        return render_template("usuario_cadastrado.html")
    else:
        return "Método inválido"

@app.route('/usuarios')
def usuarios():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM usuario")
    usuarios = cursor.fetchall()
    cursor.close()

    return render_template('usuarios.html', usuarios=usuarios)

#caso tenha problemas em criar a tabela e o erro indicado for DDL disable -> crie outra branch

@app.route('/verificar_login', methods=['POST'])
def verificar_login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        # Conecta ao banco de dados e verifica as credenciais
        cursor = db.cursor()
        cursor.execute('SELECT * FROM usuario WHERE email = %s AND senha = %s', (email, senha))
        usuario = cursor.fetchone()
        cursor.close()

        if usuario:
            # Login bem-sucedido, redirecione para a página de sucesso ou faça o que for necessário
            flash('Login bem-sucedido!', 'success')  # Exibe uma mensagem de sucesso
            return render_template("login-realizado-com-sucesso.html")
        else:
            # Login falhou, exiba uma mensagem de erro
            flash('Credenciais inválidas. Tente novamente.', 'error')
            return "ERROR"
    else:
        return "Método inválido"

"""
@app.route('/tabela-usuario')
def criar_tabela_usuario():
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuario (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            senha VARCHAR(255) NOT NULL
        )
    ''')
    cursor.close()
    return 'Tabela de usuário criada com sucesso'
"""

if __name__ == '__main__':
    app.run(debug=True)
