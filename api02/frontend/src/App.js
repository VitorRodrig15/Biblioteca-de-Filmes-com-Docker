import React, { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [filmes, setFilmes] = useState([]);

  useEffect(() => {
    fetch("/api")
      .then(res => res.json())
      .then(data => setFilmes(data))
      .catch(err => console.error("Erro ao buscar filmes:", err));
  }, []);

  return (
    <div className="App">
      <h1>📽️ Biblioteca de Filmes</h1>
      <div className="filmes-container">
        {filmes.map(filme => (
          <div className="filme-card" key={filme.id}>
            <h2>{filme.titulo}</h2>
            <p><strong>Título Original:</strong> {filme.titulo_original}</p>
            <p><strong>Diretor:</strong> {filme.diretor}</p>
            <p><strong>Gênero:</strong> {filme.genero}</p>
            <p><strong>Empresa:</strong> {filme.empresa}</p>
            <p><strong>Lançamento:</strong> {filme.data_lancamento}</p>
            <p><strong>Duração:</strong> {filme.duracao_minutos} min</p>
            <p><strong>Orçamento:</strong> ${filme.orcamento.toLocaleString()}</p>
            <p><strong>Bilheteria:</strong> ${filme.bilheteria.toLocaleString()}</p>
            <p><strong>Nota IMDb:</strong> {filme.nota_imdb}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;