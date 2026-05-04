from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Simulação do Banco de Dados (Futuramente pode ser substituído por comandos SQL)
# Dados focados no Jardim Três Marias e arredores.
ecopontos_bd = [
    {
        "id": 1,
        "nome": "Ecoponto - Jardim Três Marias",
        "endereco": "Rua Exemplo do Bairro, 123, Jardim Três Marias, SP",
        "materiais": "Computadores, Monitores, Teclados",
        "horario": "Segunda a Sábado, 08:00 às 17:00"
    },
    {
        "id": 2,
        "nome": "Ponto de Recolha Supermercado Central",
        "endereco": "Av. Principal, 456, Jardim Três Marias, SP",
        "materiais": "Pilhas e Baterias de Telemóvel",
        "horario": "Todos os dias, 07:00 às 22:00"
    },
    {
        "id": 3,
        "nome": "Coleta Cidadã - Posto Poupatempo (Unidade Mais Próxima)",
        "endereco": "Av. de Acesso, 789, SP",
        "materiais": "Pequenos Eletrónicos, Telemóveis Antigos, Cabos",
        "horario": "Segunda a Sexta, 09:00 às 17:00"
    }
]

# Rota principal para carregar a página visual (HTML)
@app.route('/')
def home():
    return render_template('index.html')

# Rota da API (Fornece os dados em formato JSON para o JavaScript ler)
@app.route('/api/ecopontos')
def get_ecopontos():
    return jsonify(ecopontos_bd)

if __name__ == '__main__':
    app.run(debug=True)