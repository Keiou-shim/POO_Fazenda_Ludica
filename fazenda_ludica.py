# --------------------------------------------------------------------------------
# 1. Abstração e Classe Base (Animal)
# --------------------------------------------------------------------------------

class Animal:
    """
    Classe base que abstrai as características e comportamentos comuns
    a todos os animais da fazenda.
    """
    def __init__(self, nome: str, idade: int):
        """
        Construtor para inicializar os atributos nome e idade.
        """
        self.nome = nome
        self.idade = idade

    def emitir_som(self) -> str:
        """
        Método genérico que será especializado (polimorfismo) nas subclasses.
        """
        return "O animal emite um som."

    def apresentar(self) -> str:
        """
        Retorna uma string de apresentação do animal.
        """
        return f"Olá, sou {self.nome} e tenho {self.idade} anos."

# --------------------------------------------------------------------------------
# 2. Herança e Especialização
# --------------------------------------------------------------------------------

class Cachorro(Animal):
    """
    Subclasse que herda de Animal, especializada para Cachorros.
    Adiciona o atributo 'raca' e sobrescreve 'emitir_som'.
    """
    def __init__(self, nome: str, idade: int, raca: str):
        # Chama o construtor da classe base (Animal)
        super().__init__(nome, idade)
        self.raca = raca

    # Polimorfismo: Sobrescrita do método emitir_som()
    def emitir_som(self) -> str:
        return "Au! Au!"

class Gato(Animal):
    """
    Subclasse que herda de Animal, especializada para Gatos.
    Adiciona o atributo 'cor_pelo' e sobrescreve 'emitir_som'.
    """
    def __init__(self, nome: str, idade: int, cor_pelo: str):
        # Chama o construtor da classe base (Animal)
        super().__init__(nome, idade)
        self.cor_pelo = cor_pelo

    # Polimorfismo: Sobrescrita do método emitir_som()
    def emitir_som(self) -> str:
        return "Miau!"

# --------------------------------------------------------------------------------
# 3. Encapsulamento (Proteção de Dados)
# --------------------------------------------------------------------------------

class Vaca(Animal):
    """
    Subclasse que herda de Animal, especializada para Vacas.
    Aplica Encapsulamento em '__producao_leite_litros'.
    """
    def __init__(self, nome: str, idade: int, producao_leite_litros: float):
        # Chama o construtor da classe base (Animal)
        super().__init__(nome, idade)
        # Atributo Privado (Encapsulamento)
        self.__producao_leite_litros = producao_leite_litros

    # Polimorfismo: Sobrescrita do método emitir_som()
    def emitir_som(self) -> str:
        return "Muuu!"

    # Método Getter Público
    def obter_producao_leite(self) -> float:
        """
        Retorna o valor do atributo privado de produção de leite.
        """
        return self.__producao_leite_litros

    # Método Setter Público
    def registrar_ordenha(self, litros: float):
        """
        Modifica o valor do atributo privado de produção de leite (ordenha diária).
        Aplica uma validação básica para garantir que a produção seja positiva.
        """
        if litros >= 0:
            self.__producao_leite_litros = litros
            print(f"Ordenha registrada! Nova produção de leite para {self.nome}: {litros:.1f} litros.")
        else:
            print("Erro: A produção de leite não pode ser negativa.")

# --------------------------------------------------------------------------------
# 4. Teste e Demonstração
# --------------------------------------------------------------------------------

if __name__ == "__main__":
    print("--- 4. Teste e Demonstração (Instanciação de Objetos) ---\n")

    # Criação de instâncias (Objetos)
    rex = Cachorro("Rex", 3, "Labrador")
    mimi = Gato("Mimi", 5, "Branco")
    mimosa = Vaca("Mimosa", 7, 25.5)

    animais = [rex, mimi, mimosa]

    print("--- Apresentação e Sons (Polimorfismo em Ação) ---\n")

    for animal in animais:
        # Chama o método apresentar()
        print(animal.apresentar())

        # Chama o método emitir_som() (O comportamento muda de acordo com a classe, o que é Polimorfismo)
        print(f"Som: {animal.emitir_som()}\n")

    print("--- Teste de Encapsulamento (Classe Vaca) ---\n")

    # 1. Imprimir a produção atual utilizando o método getter
    producao_inicial = mimosa.obter_producao_leite()
    print(f"Produção inicial de leite da {mimosa.nome}: {producao_inicial:.1f} litros.")

    # 2. Chamar o método setter para mudar a produção de leite
    nova_producao = 28.0
    mimosa.registrar_ordenha(nova_producao)

    # 3. Imprimir novamente a produção de leite para confirmar a mudança
    producao_final = mimosa.obter_producao_leite()
    print(f"Produção final de leite da {mimosa.nome} (após ordenha): {producao_final:.1f} litros.")