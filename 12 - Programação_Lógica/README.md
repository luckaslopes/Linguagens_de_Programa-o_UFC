# Quebra-Cabeça Lógico: Posições e Cores 

## Visão Geral do Projeto

Este repositório apresenta a modelagem de um pequeno **problema lógico** utilizando uma sintaxe inspirada em Prolog, uma linguagem de programação lógica declarativa. O objetivo é demonstrar como problemas baseados em restrições e relacionamentos podem ser expressos de forma declarativa, permitindo que um "motor lógico" encontre as soluções.

O problema é um quebra-cabeça de arranjo onde precisamos deduzir a cor e a posição de três objetos, dadas algumas pistas.

---

## O Problema: Quebra-Cabeça de Posições e Cores

Temos três objetos (`Carro`, `Casa`, `Árvore`), três cores (`Vermelho`, `Azul`, `Verde`) e três posições (`1`, `2`, `3`). Precisamos atribuir uma cor e uma posição **únicas** a cada objeto, satisfazendo as seguintes pistas:

**Objetos:**
* Carro
* Casa
* Árvore

**Cores:**
* Vermelho
* Azul
* Verde

**Posições:**
* 1 (Esquerda)
* 2 (Meio)
* 3 (Direita)

**Pistas (Restrições Lógicas):**
1.  O Carro não está na posição 3.
2.  A Casa é Azul **ou** está na posição 1.
3.  O objeto na posição 2 é Verde.
4.  O objeto Vermelho não é a Árvore.
5.  Cada objeto tem uma cor e uma posição que não se repetem.

---

## A Solução (Modelagem Lógica)

A solução é apresentada em uma sintaxe que simula os fatos e regras de Prolog. Embora não seja executável diretamente como um código Python ou Java, ela serve como uma representação clara do problema lógico. Se fosse um interpretador Prolog real, poderíamos consultar o sistema para encontrar a solução.

O arquivo `quebra_cabeca_logico.pl` contém essa modelagem. Ele define as relações (`predicados`) e as restrições (`cláusulas`) que descrevem o que sabemos sobre o problema.

---

## Estrutura do Repositório

* `README.md`: Este arquivo, detalhando o problema, a solução e como interpretá-la.
* `quebra_cabeca_logico.pl`: O arquivo contendo a modelagem lógica do quebra-cabeça.

---

## Como Ler a Modelagem Lógica (`quebra_cabeca_logico.pl`)

No arquivo `.pl`, você encontrará "fatos" (declarações de verdade) e "regras" (condições para que algo seja verdade).

* **`posicao(Objeto, Cor, Posicao).`**: Este seria um predicado principal para a solução, afirmando que `Objeto` tem `Cor` e está na `Posicao`.
* **Restrições**: Cada pista é traduzida em uma ou mais regras ou negações.
    * Ex: `nao_esta_na_posicao(carro, 3).` (O Carro não está na posição 3).
    * Ex: `ou(cor(casa, azul), posicao(casa, 1)).` (Casa é Azul OU está na posição 1).
* **Unicidade**: A garantia de que cores e posições não se repetem é fundamental em problemas de restrição e seria expressa por predicados como `diferente(X, Y)`.

Se você tivesse um interpretador Prolog (como o SWI-Prolog), você carregaria este arquivo e faria uma "consulta" para encontrar os valores de `Objeto`, `Cor` e `Posicao` que satisfazem todas as regras.

---

## Conceitos de Programação Lógica Abordados

* **Fatos (Facts)**: Declarações básicas sobre o conhecimento no domínio do problema (ex: `cor_disponivel(vermelho)`).
* **Regras (Rules)**: Conclusões que podem ser inferidas a partir de fatos ou outras regras (ex: `solucao(CarroCor, CarroPos, CasaCor, CasaPos, ArvoreCor, ArvorePos) :- ...`).
* **Variáveis Lógicas**: Representadas por letras maiúsculas (ex: `CarroCor`, `Posicao`). Elas são "desconhecidas" até que o motor lógico as "instancie" com valores que satisfaçam as restrições.
* **Unificação**: O processo pelo qual o motor lógico tenta casar as variáveis com valores para satisfazer os predicados.
* **Backtracking**: Se uma tentativa de unificação falha, o motor logic volta e tenta outras combinações, buscando uma solução.
* **Programação por Restrições**: A essência de problemas como este, onde a solução é encontrada ao satisfazer um conjunto de condições.

---

## Potencial de Expansão

Este modelo básico pode ser expandido para:
* Quebra-cabeças maiores e mais complexos.
* Sistemas de diagnóstico (dadas as evidências, qual a causa?).
* Sistemas de recomendação.
* Planejamento e agendamento.

---
