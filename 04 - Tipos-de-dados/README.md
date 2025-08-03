
# Comparação de Tipagem entre Linguagens de Programação

Este documento apresenta uma comparação básica da tipagem em três linguagens de programação populares: **Python**, **Java** e **JavaScript**. 

## 1. Python — Tipagem Dinâmica e Forte

- **Dinâmica:** O tipo das variáveis é inferido em tempo de execução.
- **Forte:** Não permite operações entre tipos incompatíveis sem conversão explícita.

### Exemplo em Python

```python
x = 10        # x é um inteiro
print(type(x)) # <class 'int'>

x = "texto"   # agora x é uma string, sem erro
print(type(x)) # <class 'str'>

# Operação inválida:
# print(10 + "5")  # TypeError: unsupported operand type(s)
print(10 + int("5"))  # Correto, converte string para inteiro antes
```

---

## 2. Java — Tipagem Estática e Forte

- **Estática:** Os tipos são declarados explicitamente e verificados em tempo de compilação.
- **Forte:** Não permite operações entre tipos incompatíveis sem conversão explícita.

### Exemplo em Java

```java
int x = 10;        // Declarar variável do tipo inteiro
System.out.println(x);

x = "texto";       // Erro de compilação: tipos incompatíveis

// Concatenar string e número
String y = "5";
int z = 10;
System.out.println(z + Integer.parseInt(y));  // 15
```

---

## 3. JavaScript — Tipagem Dinâmica e Fraca

- **Dinâmica:** Tipo das variáveis definido em tempo de execução.
- **Fraca:** Permite coerção automática entre tipos, o que pode causar comportamentos inesperados.

### Exemplo em JavaScript

```javascript
let x = 10;
console.log(typeof x); // "number"

x = "texto";
console.log(typeof x); // "string"

// Coerção automática:
console.log(10 + "5");  // "105" (concatenação de string)

console.log(10 * "5");  // 50  (converte string para número automaticamente)
```

---

## Resumo das diferenças

| Característica         | Python            | Java                | JavaScript         |
|-----------------------|-------------------|---------------------|--------------------|
| Tipagem               | Dinâmica          | Estática            | Dinâmica           |
| Força da tipagem      | Forte             | Forte               | Fraca              |
| Declaração de tipo    | Não explícita     | Explícita           | Não explícita      |
| Conversão automática  | Não               | Não                 | Sim (coerção)      |
| Erros de tipo         | Em tempo de execução | Em tempo de compilação | Em tempo de execução|

---

