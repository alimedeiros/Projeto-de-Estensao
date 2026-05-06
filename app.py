from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Simulação do Banco de Dados (Futuramente pode ser substituído por comandos SQL)
# Dados focados no Jardim Três Marias e arredores.
ecopontos_bd = [
    {
        "id": 1,
        "nome": "Ecoponto 24 de Agosto",
        "endereco": "Rua Coração Sertanejo, 41 - Conj. Hab. Fazenda, São Paulo - SP",
        "materiais": "Eletroeletrônicos, Entulho, Computadores, Monitores, Teclados",
        "horario": "Seg-Sáb: 06:00 às 22:00 / Dom: 06:00 às 18:00"
    },
    {
        "id": 2,
        "nome": "Ecoponto Jardim São Paulo",
        "endereco": "Rua Utaro Kanai, 374 - Conj. Hab. Juscelino Kubitscheck, São Paulo - SP",
        "materiais": "Pilhas e Baterias de Telemóvel",
        "horario": "Seg-Sáb: 06:00 às 22:00 / Dom: 06:00 às 18:00"
    },
    {
        "id": 3,
        "nome": "Ecoponto Nascer do Sol",
        "endereco": "Rua Nascer do Sol, 356 - Conj. Hab. Santa Etelvina II, São Paulo - SP",
        "materiais": "Pequenos Eletrónicos, Telemóveis Antigos, Cabos",
        "horario": "Seg-Sáb: 06:00 às 22:00 / Dom: 06:00 às 18:00"
    },
    {
        "id": 4,
        "nome": "Ecoponto Inácio Monteiro",
        "endereco": "Rua Regresso Feliz, 1190 - Conj. Hab. Inácio Monteiro, São Paulo - SP",
        "materiais": "Eletroeletrônicos, Entulho, Volumosos e Recicláveis",
        "horario": "Seg-Sáb: 06:00 às 22:00 / Dom: 06:00 às 18:00"
    },
    {
        "id": 5,
        "nome": "Ecoponto Setor G (Barro Branco)",
        "endereco": "Rua Alfonso Asturaro, 733 - Conj. Hab. Barro Branco II, São Paulo - SP",
        "materiais": "Eletroeletrônicos, Cabos e Recicláveis",
        "horario": "Seg-Sáb: 06:00 às 22:00 / Dom: 06:00 às 18:00"
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