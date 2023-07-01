# se ocorrer erro de instalação automática do flask, seguir os passos:
# 1. Acesese a aba inferior: Terminal
# 2. Navegar até a pasta Scripts com o comando abaixo no terminal:
# 3. CD /venv/Scripts
# 4. Instalar com o comando: pip3 install flask

from flask import Flask, render_template, request, url_for, redirect, session, flash
from produto import Produto
from dao import ProdutoDAO

produto_dao = ProdutoDAO('banco_estoque.db')
p = Produto('TV SAMSUNG', 2999.99, 10)

app = Flask(__name__)
app.secret_key = 'canetaestorada'


@app.route('/')
def index():
    lista = produto_dao.listar()
    return render_template('relatorio.html', titulo='Relatório de estoque', produtos=lista)


@app.route('/cadastrar')
def cadastrar():
    if 'usuario_logado' not in session or session ['usuario_logado'] == None:
        return redirect(url_for('login'))
    return render_template('cadastrar.html', titulo='Cadastra Novo Produto')


@app.route('/editar/<strind:id')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    produto = produto_dao.busca_por_id(id)
    return render_template('editar.html', titulo='Alteração de Produto' , produto=produto)


@app.route('/deletar')
def deletar():
    return '<h1>Deletando de Produto</h1>'


@app.route('/salvar', methods=['post'])
def salvar():
    descricao = request.form['descricao']
    quantidade = request.form['quantidade']
    preco = request.form['preco']
    p = Produto(descricao, preco, quantidade)
    produto_dao.salvar(p)
    return '<h1>Salvou com ID: ' + str (p.id) + '</h1>'


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autenticar', methods=['post'])
def autenticar():
    if request.form['senha'] == '123':
        session['usuario logado'] = request.form['usuario']
        flash(request.form['usuario'] + ' logou com sucesso')
        return redirect(url_for('index'))
    else:
        flash('Senha Inválida! Tente novamente')
        return redirect('/login')


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuario logado')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=80)
