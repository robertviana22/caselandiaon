from flask import Flask, render_template, request, redirect
import csv
import os
import urllib.parse  # IMPORTANTE: para codificar o texto da mensagem

app = Flask(__name__)

@app.route('/')
def home():
    return redirect('/caselandia')

@app.route('/caselandia')
def caselandia():
    return render_template('caselandia.html')

@app.route('/registrar_fidelidade', methods=['POST'])
def registrar_fidelidade():
    nome = request.form['nome']
    contato = request.form['contato']
    servico = request.form['servico']

    # Salva os dados no CSV
    with open('fidelidade.csv', 'a', newline='', encoding='utf-8') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([nome, contato, servico])

    # Cria e codifica a mensagem para o WhatsApp
    mensagem = f"Olá! Meu nome é {nome} e acabei de me cadastrar.\nServiço ou produto: {servico}"
    mensagem_codificada = urllib.parse.quote(mensagem)

    # Redireciona para o WhatsApp com a mensagem codificada
    return redirect(f"https://wa.me/5579991763141?text={mensagem_codificada}")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
