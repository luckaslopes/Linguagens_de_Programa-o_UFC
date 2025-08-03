# Exemplo de Programação Funcional em Python: Cálculo de Fatorial

## Visão Geral do Projeto

Este repositório apresenta uma implementação didática de **programação funcional em Python**, focando em dois pilares essenciais: **recursão** e **funções de alta ordem**. O problema escolhido para demonstração é o cálculo do fatorial de um número inteiro não negativo, um exemplo clássico que se adapta perfeitamente a esses paradigmas.

Nosso objetivo é ilustrar como esses conceitos podem levar a um código mais **declarativo, conciso e, muitas vezes, mais fácil de raciocinar** em comparação com abordagens imperativas tradicionais.

---

## O Problema: Cálculo de Fatorial ($n!$)

O fatorial de um número inteiro não negativo $n$, denotado como $n!$, é o produto de todos os inteiros positivos menores ou iguais a $n$.

**Definição Matemática:**
$n! = n \times (n-1) \times (n-2) \times \dots \times 1$

**Casos Especiais:**
* $0! = 1$ (por definição)
* $1! = 1$

**Exemplo:**
$5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$

---

## A Solução Funcional

Nossa abordagem funcional utiliza:

1.  **Recursão para `fatorial(n)`**: A função `fatorial` é definida de forma recursiva, onde a solução de um problema maior (fatorial de `n`) é expressa em termos de uma solução para um problema menor (fatorial de `n-1`), até atingir um caso base (`n=0`). Isso reflete a natureza matemática da definição de fatorial de forma elegante.

2.  **Função de Alta Ordem (`map`) para Processamento em Lotes**: Para demonstrar o poder das funções de alta ordem, incluímos uma função que calcula os fatoriais para uma **lista de números**. Utilizamos a função built-in `map`, que recebe a nossa função `fatorial` (como argumento!) e aplica-a a cada item da lista, retornando um iterador com os resultados. Isso promove a reutilização de código e um estilo mais funcional.

---

## Estrutura do Repositório

* `README.md`: Este arquivo, contendo a descrição do projeto, instruções e conceitos.
* `exemplo_funcional.py`: O código Python que implementa as funções `fatorial` (recursiva) e `calcular_fatoriais_para_lista` (usando `map`).

---

## Conceitos de Programação Funcional Abordados

* **Recursão**:
    * **Definição**: Uma técnica onde uma função resolve um problema chamando a si mesma com uma versão menor do mesmo problema.
    * **No Exemplo**: A função `fatorial(n)` demonstra um caso base (`n=0`) e um passo recursivo (`n * fatorial(n-1)`).
    * **Vantagens**: Clareza para problemas naturalmente recursivos, como o fatorial.

* **Funções de Alta Ordem (Higher-Order Functions)**:
    * **Definição**: Funções que podem receber outras funções como argumentos, retornar funções ou ambas.
    * **No Exemplo**: `map` é uma função de alta ordem que recebe `fatorial` como seu primeiro argumento. Isso permite aplicar a lógica de fatorial a uma coleção de dados de forma concisa.
    * **Vantagens**: Modularidade, reusabilidade, código mais expressivo e flexível.

* **Imutabilidade (Implícita)**:
    * Embora não explicitamente forçada em Python, a abordagem funcional incentiva a não modificação de dados após a criação. Nossas funções `fatorial` e `calcular_fatoriais_para_lista` produzem novos resultados sem alterar os valores de entrada, o que contribui para um código mais previsível e fácil de testar.

---

## Requisitos

* Python 3.6 ou superior (testado com Python 3.9+)

---


