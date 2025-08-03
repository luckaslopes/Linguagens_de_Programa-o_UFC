# Rust: Pesquisa e Documentação

## Introdução
Rust é uma linguagem de programação moderna, criada pela Mozilla Research em 2010, cujo foco principal é **desempenho, segurança e concorrência**.  
Ela foi projetada para evitar erros comuns como *segfaults* e problemas de concorrência, oferecendo ao mesmo tempo velocidade próxima à de C e C++.

---

## Características Principais

### 1. Segurança de Memória
- Sistema de *ownership* e *borrowing* que evita problemas de ponteiros nulos e *data races* em tempo de compilação.
- Elimina a necessidade de um *garbage collector*.

### 2. Concorrência Segura
- Oferece abstrações para concorrência e paralelismo.
- O compilador garante que não haja condições de corrida (*race conditions*).

### 3. Desempenho
- Performance comparável a C/C++.
- Compilação para binários otimizados.

### 4. Ferramentas Modernas
- **Cargo**: gerenciador de pacotes e builds.
- **Rustup**: gerenciador de versões.
- Ecosistema de crates (bibliotecas) em `crates.io`.

---

## Onde é Usada
Rust é utilizada em diversas áreas, como:
- **Sistemas Operacionais** (partes do Linux estão sendo reescritas em Rust)
- **WebAssembly**
- **Criação de navegadores** (motor Servo da Mozilla)
- **Blockchain e Criptografia**
- **Aplicações de alto desempenho** (servidores, jogos)

---

## Comparação com Outras Linguagens

| Linguagem  | Pontos Fortes                           | Limitações                       |
|------------|-----------------------------------------|----------------------------------|
| Rust       | Segurança de memória sem GC, performance | Curva de aprendizado alta        |
| Go         | Simplicidade, concorrência com goroutines | Coleta de lixo pode impactar performance |
| Kotlin     | Produtividade, multiplataforma (JVM)     | Depende da JVM ou compilador nativo |
| TypeScript | Tipagem estática no JavaScript          | Performance limitada pelo JS     |

---

## Tendências e Comunidade
- **Rust está entre as linguagens mais amadas do Stack Overflow desde 2016**.
- Grandes empresas como **Amazon, Microsoft, Discord, Dropbox e Cloudflare** utilizam Rust em produção.
- A linguagem tem atraído desenvolvedores por sua combinação de segurança, velocidade e comunidade ativa.

---

## Exemplo de Código em Rust

```rust
fn main() {
    let nome = "Mundo";
    println!("Olá, {}!", nome);
}
