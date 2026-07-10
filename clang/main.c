#include <stdio.h>

void printSecrets(int secret[]){
    for (int i = 0; i < 4; i++){
        printf("%d\n", secret[i]);
    }
}

int main() {
    int secret[5] = {4, 20, 61, 80};
    char firstName[] = "Wooop dee doo";
    printSecrets(secret);
    printf("%s\n", firstName);

    return 0;
}

