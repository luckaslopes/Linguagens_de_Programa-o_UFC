# Gerenciamento de Memória em Diferentes Linguagens

Este projeto apresenta um estudo comparativo de como ocorre a gestão de memória em **Python** e **C**.

## Comparação entre Python e C

| Aspecto                     | Python                                              | C                                                      |
|-----------------------------|-----------------------------------------------------|--------------------------------------------------------|
| **Alocação de Memória**     | Automática (gerenciada pelo interpretador)          | Manual (malloc, calloc, realloc)                       |
| **Desalocação de Memória**  | Automática (coletor de lixo - garbage collector)    | Manual (free)                                          |
| **Controle do Desenvolvedor** | Baixo – quase todo gerenciamento é automático     | Alto – o programador é responsável por alocar e liberar memória |
| **Risco de Vazamento**      | Menor, pois o GC libera objetos não utilizados      | Maior, se esquecer de liberar memória alocada          |
| **Performance**             | Mais lenta devido à sobrecarga do GC                | Mais rápida e previsível (se bem gerenciado)           |
| **Segurança**               | Maior, pois evita acessos inválidos automaticamente | Menor – uso incorreto pode causar falhas ou vazamentos |

## Conclusão

- **Python:** facilita a vida do programador por gerenciar a memória automaticamente, mas pode ter sobrecarga de desempenho.
- **C:** dá mais controle e eficiência, mas exige atenção rigorosa para evitar erros e vazamentos de memória.
