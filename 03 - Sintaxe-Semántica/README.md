
# MiniCalc — Gramática e Análise Léxica

Este documento apresenta uma mini-gramática fictícia para a linguagem **MiniCalc**, uma linguagem simples de cálculos com variáveis, números inteiros e operações básicas.

---

## Gramática Sintática

A seguir, a definição sintática simplificada da linguagem MiniCalc em forma Backus-Naur Form (BNF) simplificada:

```
<programa> ::= <comando> | <comando> <programa>

<comando> ::= <declaracao> | <atribuicao> | <expressao>

<declaracao> ::= "var" <identificador> ";"

<atribuicao> ::= <identificador> "=" <expressao> ";"

<expressao> ::= <termo> | <expressao> "+" <termo> | <expressao> "-" <termo>

<termo> ::= <fator> | <termo> "*" <fator> | <termo> "/" <fator>

<fator> ::= <numero> | <identificador> | "(" <expressao> ")"

<identificador> ::= letra (letra | dígito)*

<numero> ::= dígito+
```

---

## Análise Léxica

A análise léxica é o processo de converter a sequência de caracteres do código fonte em uma sequência de tokens. Para MiniCalc, temos os seguintes tokens:

| Token          | Exemplo           | Descrição                        |
|----------------|-------------------|---------------------------------|
| `var`          | `var`             | Palavra reservada para declaração|
| `identificador`| `x`, `valor1`     | Nome de variáveis                |
| `número`       | `123`, `42`       | Valores numéricos inteiros       |
| `=`            | `=`               | Operador de atribuição           |
| `+`, `-`, `*`, `/` | `+`, `-`, `*`, `/` | Operadores aritméticos         |
| `;`            | `;`               | Delimitador de comando           |
| `(`, `)`       | `(`, `)`          | Parênteses para agrupamento      |

---

## Exemplos de código e análise léxica

### Código MiniCalc

```minicalc
var x;
x = 10;
var y;
y = x * (5 + 3);
```

### Sequência de tokens gerada

| Token          | Valor      |
|----------------|------------|
| `var`          | "var"      |
| `identificador`| "x"        |
| `;`            | ";"        |
| `identificador`| "x"        |
| `=`            | "="        |
| `número`       | "10"       |
| `;`            | ";"        |
| `var`          | "var"      |
| `identificador`| "y"        |
| `;`            | ";"        |
| `identificador`| "y"        |
| `=`            | "="        |
| `identificador`| "x"        |
| `*`            | "*"        |
| `(`            | "("        |
| `número`       | "5"        |
| `+`            | "+"        |
| `número`       | "3"        |
| `)`            | ")"        |
| `;`            | ";"        |

---

