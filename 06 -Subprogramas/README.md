# Subprogramas: Passagem de Parâmetros por Valor e por Referência

Este diretório contém exemplos práticos que demonstram a diferença entre **passagem de parâmetros por valor** e **por referência**, utilizando as linguagens **C**, **Python** e **JavaScript**.

---

## Conceitos

### Passagem por Valor
Quando um argumento é passado **por valor**, uma **cópia** do dado é enviada para a função. Alterações no parâmetro dentro da função **não afetam** a variável original.

### Passagem por Referência
Quando um argumento é passado **por referência**, a função recebe um **acesso direto ao local de memória** da variável. Alterações dentro da função **afetam diretamente** a variável original.

---

## Exemplos por Linguagem

### C

- `void porValor(int x)`: recebe um inteiro por valor, não altera o original.
- `void porReferencia(int *x)`: recebe um ponteiro (endereço), altera o original.

**Saída esperada:**
```
Valor após porValor: 5
Valor após porReferencia: 15
```

---

### Python

- `por_valor(x)`: recebe um inteiro (imutável), não altera o original.
- `por_referencia(lista)`: recebe uma lista (mutável), altera o conteúdo.

**Saída esperada:**
```
Valor após por_valor: 5
Valor após por_referencia: 15
```

---

### JavaScript

- `porValor(x)`: recebe um número (primitivo), não altera o original.
- `porReferencia(obj)`: recebe um objeto (referência), altera a propriedade.

**Saída esperada:**
```
Valor após porValor: 5
Valor após porReferencia: 15
```

---

## Como executar os exemplos

### C
```bash
gcc por_valor_referencia.c -o exemplo && ./exemplo
```

### Python
```bash
python3 por_valor_referencia.py
```

### JavaScript (Node.js)
```bash
node por_valor_referencia.js
```

---

