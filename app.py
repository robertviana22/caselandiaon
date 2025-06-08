from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/caselandia')
def caselandia():
    return render_template('caselandia.html')

@app.route('/registrar_fidelidade', methods=['POST'])
def registrar_fidelidade():
    nome = request.form['nome']
    contato = request.form['contato']
    servico = request.form['servico']

    with open('fidelidade.csv', 'a', newline='', encoding='utf-8') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([nome, contato, servico])

    return redirect('https://wa.me/5579991763141?text=Cadastro+realizado+com+sucesso%21')
if __name__ == '__main__':
   import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
