#include <stdio.h>
#include <string.h>
#include <stdlib.h>

unsigned char xor_key[] = {0x21, 0x42, 0x63, 0x84, 0xA5};
char encrypted[] = "QysX88RNLhDbxlUkGLfLQnIHt8F+dg3g+hI6U/aWRR0FtNd+JBbq+k8dE/aVR3MX+Q==";

static const char b64_table[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

int b64_index(char c) {
    const char *p = strchr(b64_table, c);
    return p ? p - b64_table : -1;
}

void decode_base64(const char *in, unsigned char *out) {
    int val = 0, valb = -8;
    while (*in) {
        int idx = b64_index(*in++);
        if (idx == -1) continue;
        val = (val << 6) + idx;
        valb += 6;
        if (valb >= 0) {
            *out++ = (char)((val >> valb) & 0xFF);
            valb -= 8;
        }
    }
    *out = '\0';
}

int main() {
    char input[128];
    printf("Enter flag: ");
    fgets(input, sizeof(input), stdin);
    input[strcspn(input, "\n")] = 0;

    unsigned char dec[128];
    decode_base64(encrypted, dec);

    for (int i = 0; i < strlen(input); i++) {
        if ((input[i] ^ xor_key[i % 5]) != dec[i]) {
            puts("Wrong.");
            return 0;
        }
    }
    puts("Correct!");
    return 0;
}
