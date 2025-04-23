# Avaliação
class Avaliacao:
    def __init__(self, cliente, nota, comentario):
        self.cliente = cliente
        self.nota = nota
        self.comentario = comentario

    def __str__(self):
        return f"{self.cliente} - Nota: {self.nota} - {self.comentario}"

# Categoria
class Categoria:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome

# Produto
class Produto:
    def __init__(self, nome, preco, estoque, categoria):
        self.__nome = nome
        self.__preco = preco
        self.__estoque = estoque
        self.__categoria = categoria
        self.__avaliacoes = []

    def vender(self, quantidade):
        if quantidade <= self.__estoque:
            self.__estoque -= quantidade
        else:
            print(f"Estoque insuficiente para {self.__nome}.")

    def reabastecer(self, quantidade):
        self.__estoque += quantidade

    def adicionar_avaliacao(self, avaliacao):
        self.__avaliacoes.append(avaliacao)

    def visualizar_estoque(self):
        return f"{self.__nome}: {self.__estoque} unidades"

    def __str__(self):
        avaliacoes_str = "\n".join(str(a) for a in self.__avaliacoes) or "Sem avaliações."
        return (f"Produto: {self.__nome}\n"
                f"Preço: R$ {self.__preco:.2f}\n"
                f"Estoque: {self.__estoque}\n"
                f"Categoria: {self.__categoria}\n"
                f"Avaliações:\n{avaliacoes_str}")

# Loja
class Loja:
    def __init__(self, nome):
        self.nome = nome
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_estoque(self):
        for p in self.produtos:
            print(p.visualizar_estoque())

    def detalhes_produto(self, nome_produto):
        for p in self.produtos:
            if p._Produto__nome == nome_produto:
                print(p)
                return
        print("Produto não encontrado.")

# Programa principal
if __name__ == "__main__":
    # Categorias
    eletronicos = Categoria("Eletrônicos")
    livros = Categoria("Livros")

    # Produtos
    produto1 = Produto("Smartphone", 1500.0, 10, eletronicos)
    produto2 = Produto("Livro Python", 80.0, 5, livros)

    # Loja
    minha_loja = Loja("Loja Exemplo")
    minha_loja.adicionar_produto(produto1)
    minha_loja.adicionar_produto(produto2)

    # Vendas e reabastecimentos
    produto1.vender(2)
    produto2.reabastecer(3)

    # Avaliação
    avaliacao = Avaliacao("João", 5, "Excelente produto!")
    produto1.adicionar_avaliacao(avaliacao)

    # Visualizar estoque
    print("\nEstoque da loja:")
    minha_loja.listar_estoque()

    # Detalhes do produto
    print("\nDetalhes do produto:")
    minha_loja.detalhes_produto("Smartphone")
