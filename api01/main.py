import typing
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Filme(BaseModel):
    id: int
    titulo: str
    titulo_original: str
    data_lancamento: str   # formato da data: "YYYY-MM-DD"
    duracao_minutos: int
    orcamento: int         # valor em dólares
    bilheteria: int        # valor em dólares
    nota_imdb: float
    empresa: str
    genero: str
    diretor: str

DB: typing.List[Filme] = [
    Filme(
        id=1,
        titulo="Matrix",
        titulo_original="The Matrix",
        data_lancamento="1999-03-31",
        duracao_minutos=136,
        orcamento=63000000,
        bilheteria=466000000,
        nota_imdb=8.7,
        empresa="Warner Bros",
        genero="Sci-Fi",
        diretor="Lana Wachowski, Lilly Wachowski"
    ),
    Filme(
        id=2,
        titulo="A Origem",
        titulo_original="Inception",
        data_lancamento="2010-07-16",
        duracao_minutos=148,
        orcamento=160000000,
        bilheteria=836000000,
        nota_imdb=8.8,
        empresa="Warner Bros",
        genero="Sci-Fi",
        diretor="Christopher Nolan"
    ),
    Filme(
        id=3,
        titulo="Toy Story",
        titulo_original="Toy Story",
        data_lancamento="1995-11-22",
        duracao_minutos=81,
        orcamento=30000000,
        bilheteria=373000000,
        nota_imdb=8.3,
        empresa="Pixar",
        genero="Animação",
        diretor="John Lasseter"
    ),
    Filme(
        id=4,
        titulo="Vingadores: Era de Ultron",
        titulo_original="Avengers: Age of Ultron",
        data_lancamento="2015-05-01",
        duracao_minutos=141,
        orcamento=365000000,
        bilheteria=1405000000,
        nota_imdb=7.3,
        empresa="Marvel Studios",
        genero="Ação",
        diretor="Joss Whedon"
    ),
    Filme(
        id=5,
        titulo="Homem-Aranha 3",
        titulo_original="Spider-Man 3",
        data_lancamento="2007-05-04",
        duracao_minutos=139,
        orcamento=258000000,
        bilheteria=895000000,
        nota_imdb=6.2,
        empresa="Sony Pictures",
        genero="Ação",
        diretor="Sam Raimi"
    ),
    Filme(
        id=6,
        titulo="A Cor Púrpura",
        titulo_original="The Color Purple",
        data_lancamento="1985-12-18",
        duracao_minutos=154,
        orcamento=15000000,
        bilheteria=142000000,
        nota_imdb=7.8,
        empresa="Warner Bros",
        genero="Drama",
        diretor="Steven Spielberg"
    ),
    Filme(
        id=7,
        titulo="12 Anos de Escravidão",
        titulo_original="12 Years a Slave",
        data_lancamento="2013-11-08",
        duracao_minutos=134,
        orcamento=22000000,
        bilheteria=187700000,
        nota_imdb=8.1,
        empresa="Regency Enterprises",
        genero="Drama",
        diretor="Steve McQueen"
    ),
    Filme(
        id=8,
        titulo="Kill Bill: Volume 1",
        titulo_original="Kill Bill: Vol. 1",
        data_lancamento="2003-10-10",
        duracao_minutos=111,
        orcamento=30000000,
        bilheteria=180900000,
        nota_imdb=8.1,
        empresa="Miramax",
        genero="Ação",
        diretor="Quentin Tarantino"
    ),
    Filme(
        id=9,
        titulo="Bastardos Inglórios",
        titulo_original="Inglourious Basterds",
        data_lancamento="2009-08-21",
        duracao_minutos=153,
        orcamento=70000000,
        bilheteria=321500000,
        nota_imdb=8.3,
        empresa="Universal Pictures",
        genero="Guerra",
        diretor="Quentin Tarantino"
    ),
    Filme(
        id=10,
        titulo="Parasita",
        titulo_original="Parasite",
        data_lancamento="2019-05-30",
        duracao_minutos=132,
        orcamento=11400000,
        bilheteria=263000000,
        nota_imdb=8.6,
        empresa="CJ Entertainment",
        genero="Drama",
        diretor="Bong Joon-ho"
    )
]

@app.get("/api", response_model=typing.List[Filme])
def listar_filmes():
    return DB