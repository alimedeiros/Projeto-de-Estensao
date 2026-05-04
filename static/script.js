document.addEventListener('DOMContentLoaded', () => {
    const listContainer = document.getElementById('ecopontos-list');
    const searchInput = document.getElementById('searchInput');
    let ecopontosData = [];

    // Função para ir buscar os dados ao Python (Flask)
    fetch('/api/ecopontos')
        .then(response => response.json())
        .then(data => {
            ecopontosData = data;
            displayEcopontos(ecopontosData);
        })
        .catch(error => console.error("Erro ao carregar os dados:", error));

    // Função para mostrar os dados no ecrã
    function displayEcopontos(ecopontos) {
        listContainer.innerHTML = ''; // Limpa a lista antes de mostrar
        
        if(ecopontos.length === 0) {
            listContainer.innerHTML = '<p>Nenhum local encontrado para este material.</p>';
            return;
        }

        ecopontos.forEach(ponto => {
            const card = document.createElement('div');
            card.className = 'card';
            card.innerHTML = `
                <h3>${ponto.nome}</h3>
                <p><strong>📍 Endereço:</strong> ${ponto.endereco}</p>
                <p><strong>♻️ Materiais:</strong> ${ponto.materiais}</p>
                <p><strong>🕒 Horário:</strong> ${ponto.horario}</p>
            `;
            listContainer.appendChild(card);
        });
    }

    // Função para filtrar pela barra de pesquisa
    searchInput.addEventListener('input', (e) => {
        const termoPesquisa = e.target.value.toLowerCase();
        
        const dadosFiltrados = ecopontosData.filter(ponto => {
            return ponto.materiais.toLowerCase().includes(termoPesquisa) || 
                   ponto.nome.toLowerCase().includes(termoPesquisa);
        });
        
        displayEcopontos(dadosFiltrados);
    });
});