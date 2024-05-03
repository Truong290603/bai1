#include <stdio.h>

int main() {
    printf("Cac so nguyen co 2 chu so va la boi cua 7:\n");

    // Duyet cac so tu 10 den 99
    for (int i = 10; i <= 99; i++) {
        // Kiem tra neu so do la boi cua 7
        if (i % 7 == 0) {
            printf("%d\n", i);
        }
    }

    return 0;
}
