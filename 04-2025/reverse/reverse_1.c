#include <stdio.h>
#include <string.h>

int check_flag(const char *input) {
    if (strlen(input) != 43) return 0;
    int valid = 1;
    valid &= input[26] == 'h';
    valid &= ((input[15] ^ 0x42) == (115));
    valid &= ((input[0] ^ 0x42) == (32));
    valid &= ((input[6] ^ 0x42) == (46));
    valid &= ((input[27] ^ 0x42) == (113));
    valid &= input[35] == 'r';
    valid &= input[36] == '_';
    valid &= input[2] == 't';
    valid &= ((input[3] ^ 0x42) == (53));
    valid &= ((input[9] ^ 0x42) == (33));
    valid &= input[25] == 't';
    valid &= input[34] == '0';
    valid &= input[39] == '_';
    valid &= input[23] == 't';
    valid &= input[8] == '_';
    valid &= input[22] == '0';
    valid &= input[13] == 't';
    valid &= input[32] == 'g';
    valid &= input[33] == '_';
    valid &= input[14] == 'h';
    valid &= input[42] == '}';
    valid &= input[12] == '{';
    valid &= input[4] == 'a';
    valid &= input[38] == 's';
    valid &= ((input[21] ^ 0x42) == (44));
    valid &= input[19] == 's';
    valid &= input[17] == '_';
    valid &= input[29] == 'f';
    valid &= ((input[30] ^ 0x42) == (46));
    valid &= input[31] == '4';
    valid &= input[1] == 'i';
    valid &= input[24] == '_';
    valid &= input[20] == '_';
    valid &= input[37] == '1';
    valid &= input[7] == 's';
    valid &= input[40] == '1';
    valid &= ((input[18] ^ 0x42) == (115));
    valid &= input[16] == 's';
    valid &= input[41] == 't';
    valid &= input[11] == 'f';
    valid &= input[10] == 't';
    valid &= input[28] == '_';
    valid &= input[5] == 'l';
    return valid;
}

int main() {
    char buf[128];
    printf("Enter flag: ");
    fgets(buf, sizeof(buf), stdin);
    buf[strcspn(buf, "\n")] = '\0';

    if (check_flag(buf)) {
        puts("Correct!");
    } else {
        puts("Wrong.");
    }
    return 0;
}
