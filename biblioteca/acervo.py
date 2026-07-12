class Acervo:
    """Gerencia o conjunto de livros de uma biblioteca."""

    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        """Adiciona um livro ao acervo."""
        self.livros.append(livro)

    def total_livros(self):  # BUG-ESTILO: CORRIGIDO!
        """Retorna o total de livros no acervo."""
        return len(self.livros)

    def buscar_por_titulo(self, titulo):
        """Busca livros pelo titulo
        (sem diferenciar maiusculas/minusculas)."""
        return [
            i for i in self.livros if titulo.lower() in i.titulo.lower()
        ]  # Mudança da variável de 'l' para 'i'.

    def buscar_por_autor(self, autor):
        """Busca livros pelo nome do autor."""
        return [
            i for i in self.livros if autor.lower() in i.autor.lower()
        ]  # BUG: CORRIGIDO!

    def livros_disponiveis(self):
        """Retorna lista de livros disponiveis para emprestimo."""
        return [i for i in self.livros if i.disponivel]

    def livros_emprestados(self):
        """Retorna lista de livros atualmente emprestados."""
        return [i for i in self.livros if not i.disponivel]
    