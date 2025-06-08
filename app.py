from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)

# Rota principal que redireciona para a página Caselândia
@app.route('/')
def home():
    return redirect('/caselandia')

# Página principal com o formulário de fidelidade
@app.route('/caselandia')
def caselandia():
    return render_template('caselandia.html')

# Rota que recebe o formulário preenchido e salva os dados
@app.route('/registrar_fidelidade', methods=['POST'])
def registrar_fidelidade():
    nome = request.form['nome']
    contato = request.form['contato']
    servico = request.form['servico']

    # Grava os dados em um arquivo CSV
    with open('fidelidade.csv', 'a', newline='', encoding='utf-8') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([nome, contato, servico])

    # Redireciona para o WhatsApp após cadastro
    return redirect('https://wa.me/5579991763141?text=Cadastro+realizado+com+sucesso%21')

# Inicializa o servidor Flask na porta fornecida pelo Render
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
