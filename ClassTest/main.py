"""
    Arquivos __init__.py servem para fazer com que o Python entenda que a pasta
    é modulo de biblioteca
"""

from classInit.teste import Teste

if __name__ == "__main__":
    teste = Teste()

    print(teste.write())
