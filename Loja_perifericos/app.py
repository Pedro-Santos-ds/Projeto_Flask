from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dados temporários para exemplo
produtos = [
    {"id": 1, "nome": "Mouse Gamer Pro X", "preco": 350.00, "categoria": "mouse"},
    {"id": 2, "nome": "Teclado Mecânico RGB", "preco": 420.00, "categoria": "teclado"},
    {"id": 3, "nome": "Headset 7.1 Surround", "preco": 599.90, "categoria": "headset"},
    {"id": 4, "nome": "Microfone Studio USB", "preco": 799.00, "categoria": "microfone"},
    {"id": 5, "nome": "Mousepad XL Speed", "preco": 129.90, "categoria": "mousepad"}
]
@app.route('/')
def index():
    return render_template('index.html', produtos=produtos)

@app.route('/cadastrar/lista', methods=['GET', 'POST'])
def cadastro_lista():
    if request.method == 'POST':
        novo_id = len(produtos) + 1
        novo_produto = {
            "id": novo_id,
            "nome": request.form['nome'],
            "preco": float(request.form['preco']),
            "categoria": request.form['categoria']
        }
        produtos.append(novo_produto)
        return redirect(url_for('index'))
    return render_template('cadastro_lista.html')

@app.route('/cadastrar/dict1', methods=['GET', 'POST'])
def cadastro_dict1():
    if request.method == 'POST':
        novo_id = len(produtos) + 1
        novo_produto = {
            "id": novo_id,
            "nome": request.form['nome'],
            "preco": float(request.form['preco']),
            "categoria": request.form['categoria'],
            "fabricante": request.form['fabricante'],
            "dpi": request.form['dpi']
        }
        produtos.append(novo_produto)
        return redirect(url_for('index'))
    return render_template('cadastro_dict1.html')

@app.route('/cadastrar/dict2', methods=['GET', 'POST'])
def cadastro_dict2():
    if request.method == 'POST':
        novo_id = len(produtos) + 1
        novo_produto = {
            "id": novo_id,
            "nome": request.form['nome'],
            "preco": float(request.form['preco']),
            "categoria": request.form['categoria'],
            "peso": request.form['peso'],
            "conexao": request.form['conexao'],
            "botoes": request.form['botoes']
        }
        produtos.append(novo_produto)
        return redirect(url_for('index'))
    return render_template('cadastro_dict2.html')

if __name__ == '__main__':
    app.run(debug=True)