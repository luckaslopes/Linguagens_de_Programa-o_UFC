#include <stdio.h>

void porValor(int x) {
    x = x + 10;
}

void porReferencia(int *x) {
    *x = *x + 10;
}

int main() {
    int a = 5, b = 5;
    porValor(a);
    porReferencia(&b);

    printf("Valor após porValor: %d\n", a);       // 5
    printf("Valor após porReferencia: %d\n", b);  // 15
    return 0;
}
