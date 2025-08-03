% quebra_cabeca_logico.pl
%
% Este arquivo modela um pequeno quebra-cabeça lógico de posições e cores
% usando uma sintaxe inspirada em Prolog.
%
% Para "executar" isso, você precisaria de um interpretador Prolog (ex: SWI-Prolog).
% Lá, você carregaria este arquivo e faria uma consulta como:
% ?- solucao(CarroC, CarroP, CasaC, CasaP, ArvoreC, ArvoreP).
%

% --- FATOS (Conhecimento Básico do Domínio) ---

% Objetos disponíveis
objeto(carro).
objeto(casa).
objeto(arvore).

% Cores disponíveis
cor_disponivel(vermelho).
cor_disponivel(azul).
cor_disponivel(verde).

% Posições disponíveis
posicao_disponivel(1).
posicao_disponivel(2).
posicao_disponivel(3).

% --- REGRAS (As Pistas do Quebra-Cabeça e Restrições de Unicidade) ---

% Predicado principal que define a solução do quebra-cabeça.
% Ele busca as cores e posições para cada objeto.
solucao(CarroCor, CarroPos, CasaCor, CasaPos, ArvoreCor, ArvorePos) :-
    % 1. Atribui uma cor e posição para cada objeto
    %    (Carro, Casa, Arvore) com as cores e posições disponíveis.
    cor_disponivel(CarroCor),
    posicao_disponivel(CarroPos),

    cor_disponivel(CasaCor),
    posicao_disponivel(CasaPos),

    cor_disponivel(ArvoreCor),
    posicao_disponivel(ArvorePos),

    % 2. Garante que cada objeto tem uma cor e posição únicas (restrições de unicidade)
    %    Todas as cores devem ser diferentes entre si.
    CarroCor \= CasaCor,
    CarroCor \= ArvoreCor,
    CasaCor \= ArvoreCor,

    %    Todas as posições devem ser diferentes entre si.
    CarroPos \= CasaPos,
    CarroPos \= ArvorePos,
    CasaPos \= ArvorePos,

    % 3. Aplica as pistas do quebra-cabeça:

    % Pista 1: O Carro não está na posição 3.
    CarroPos \= 3,

    % Pista 2: A Casa é Azul OU está na posição 1.
    (   CasaCor = azul
    ;   CasaPos = 1
    ),

    % Pista 3: O objeto na posição 2 é Verde.
    % Precisamos descobrir qual objeto está na posição 2.
    (   (CarroPos = 2, CarroCor = verde)
    ;   (CasaPos = 2, CasaCor = verde)
    ;   (ArvorePos = 2, ArvoreCor = verde)
    ),

    % Pista 4: O objeto Vermelho não é a Árvore.
    ArvoreCor \= vermelho,

    % 5. Opcional: Para controle, lista as associações Objeto-Cor-Posição
    % (útil em Prolog para ver a solução encontrada).
    % Este é mais para visualização da solução.
    true. % Apenas um predicado que sempre é verdadeiro para encerrar a cláusula.