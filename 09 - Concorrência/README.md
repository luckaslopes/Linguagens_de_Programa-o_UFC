# Concorrência em Python

Este projeto mostra um exemplo simples de **concorrência** usando threads em Python, além de explicar a diferença entre **threads** e **processos**.

## Diferença entre Threads e Processos

### Processos
- São instâncias independentes de um programa em execução.
- Cada processo possui sua própria memória.
- Comunicação entre processos (IPC) é mais custosa.
- Usado quando há necessidade de isolamento e tarefas pesadas (CPU-bound).

### Threads
- São unidades de execução dentro de um processo.
- Compartilham a mesma memória do processo principal.
- Comunicação entre threads é mais simples, mas requer cuidados (concorrência e locks).
- Muito úteis para tarefas de I/O ou operações que podem ocorrer simultaneamente.

## Vantagens e Desvantagens

- **Threads**: mais leves, rápidas para criar, porém mais sujeitas a problemas de concorrência (race conditions).
- **Processos**: mais isolados, mais seguros, mas consomem mais recursos.

## Exemplo incluído

O exemplo cria várias threads que executam uma tarefa de contagem de forma concorrente, mostrando como várias partes do código podem rodar ao mesmo tempo dentro do mesmo processo.

## Como executar

```bash
python concorrencia.py
```
