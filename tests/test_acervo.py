import pytest
from biblioteca.livro import Livro
from biblioteca.acervo import Acervo

# 1 - adicionar_livro() — adicionar um livro e verificar que total_livros() aumenta
def test_adicionar_livro_aumenta_total():
    # Setup: Criamos o acervo e um livro
    acervo = Acervo("Biblioteca Municipal")
    livro1 = Livro("Dom Casmurro", "Machado de Assis", "111-11")
    
    # Verificação inicial: o acervo deve começar vazio
    assert acervo.total_livros() == 0
    
    # Ação: Adicionamos o livro
    acervo.adicionar_livro(livro1)
    
    # Verificação final: o total deve aumentar para 1
    assert acervo.total_livros() == 1
    assert acervo.livros[0].titulo == "Dom Casmurro"


# 2 - buscar_por_titulo() — buscar por título parcial e por título com letras maiúsculas/minúsculas diferentes
def test_buscar_por_titulo_parcial_e_case_insensitive():
    # Setup: Criamos o acervo com dois livros que têm palavras parecidas
    acervo = Acervo("Biblioteca Municipal")
    livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "123-45")
    livro2 = Livro("Senhora", "José de Alencar", "678-90")
    acervo.adicionar_livro(livro1)
    acervo.adicionar_livro(livro2)
    
    # Teste A: Busca Case Insensitive (Maiúsculas e Minúsculas misturadas)
    resultado_exato = acervo.buscar_por_titulo("o SeNhOr DoS aNéIs")
    assert len(resultado_exato) == 1
    assert resultado_exato[0].autor == "J.R.R. Tolkien"
    
    # Teste B: Busca Parcial
    # A palavra "senhor" está contida tanto em "O Senhor dos Anéis" quanto em "Senhora"
    resultado_parcial = acervo.buscar_por_titulo("senhor")
    assert len(resultado_parcial) == 2