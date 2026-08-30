ITEM 1: Identifique relações de herança entre as classes;

Hierarquia de Pessoas:

**Classe Base:** Pessoa.
**Subclasse Direta:** Funcionário (herda de Pessoa).
**O que herda:** Herda os atributos nome e idade de Pessoa. Além disso, adiciona seus próprios atributos: salario e carga_hsoraria.

Subclasses de Funcionário: Garçom Chefe de cozinha e Gerente (herdam de Funcionário).
**O que herdam:** Todos eles herdarão nome, idade, salario e carga_horaria. Cada classe também implementa seus métodos específicos (anotar_pedido(), preparar() e demitir(), respectivamente).

Hierarquia de Restaurante:

***Classe Base:**Restaurante.
**Subclasse:** Pizzaria (herda de Restaurante).
**O que herda:** Ela herdará os atributos nome, endereco e telefone. Também adiciona o atributo específico rodizio.

Hierarquia de Comidas:

**Classe Base:** Iguaria (comida).
**Subclasses:** Pizza e Bolo (herdam de Iguaria).
**O que herdam:** Ambas herdarão os atributos nome e preco. A subclasse Pizza adiciona o atributo borda_recheada e a subclasse Bolo adiciona o atributo formato.

ITEM 2: Modelagem da relação entre a classe Restaurante e a classe IguariaTipo de Relação:

**Tipo de Relação:** A relação entre as classes é tipicamente de Agregação (ou Composição, dependendo das regras de negócio do sistema). Isso ocorre porque um restaurante "tem" ou "oferece" iguarias, compondo o seu menu de opções.

**Implementação (Novos Atributos):** Para implementar essa relação, a classe Restaurante poderia receber um novo atributo chamado cardapio (ou menu). O tipo desse atributo seria uma lista (array ou coleção) de objetos do tipo Iguaria.  

Novas Classes Sugeridas:

**Classe Cardapio:** Para tornar a modelagem mais robusta e eficiente, sugere-se criar a classe Cardapio para encapsular a lista de iguarias. Ela forneceria métodos específicos de gerenciamento, como adicionar, remover ou buscar iguarias, e a classe Restaurante teria uma relação de 1 para 1 com ela.  

**Classe Pedido:** Uma classe de transação essencial que serviria para ligar o restaurante, o cliente (ou a mesa) e a lista de objetos Iguaria que foram solicitadas naquele momento.  

ITEM 3: Indicação e justificativa dos tipos para os argumentos
 
**argumento1 (utilizado em Garçom.anotar_pedido(argumento1)):**
**Tipo sugerido:** Uma lista de instâncias da classe Iguaria ou um objeto de uma nova classe chamada Pedido.

**Justificativa:** O garçom tem a função de anotar aquilo que o cliente vai comer, e um pedido normalmente contém um ou múltiplos itens. Passar um objeto da classe Pedido (que já conteria a lista de iguarias e a mesa) é a abordagem mais adequada na orientação a objetos. 

**argumento2 (utilizado em Chefe de cozinha.preparar(argumento2)):**
**Tipo sugerido:** Instância da classe Pedido ou da classe base Iguaria.

**Justificativa:** O chefe de cozinha precisa preparar exatamente o que foi solicitado. O sistema poderia enviar o objeto Pedido inteiro para a fila da cozinha, ou iterar sobre ele e enviar cada objeto Iguaria individualmente para o método de preparo.

**argumento3 (utilizado em Gerente.demitir(argumento3)):**
**Tipo sugerido:** Instância da classe Funcionário (ou um tipo primitivo como string/inteiro representando um ID ou CPF, dependendo da implementação).

**Justificativa:** A ação de demitir afeta diretamente um funcionário da empresa. Passar o próprio objeto Funcionário garante que o gerente manipule a entidade correta para alterar o seu status no sistema.  

