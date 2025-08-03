import threading
import time

def tarefa(nome, limite):
    for i in range(1, limite + 1):
        print(f"Thread {nome}: {i}")
        time.sleep(0.5)

def main():
    threads = []
    for i in range(1, 4):
        t = threading.Thread(target=tarefa, args=(f"T{i}", 5))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Todas as threads terminaram.")

if __name__ == "__main__":
    main()
