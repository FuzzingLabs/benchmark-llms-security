#include <iostream>
#include <cstdlib>
#include <cstring>

int main(int argc, char* argv[]) {
    char user[10];
    char pass[10];
    strcpy(user, "admin"); // Hardcoded credentials (CWE-798)
    strcpy(pass, "password");

    char buf[8];
    std::cout << "Enter command: ";
    gets(buf); // Buffer overflow (CWE-120), use of gets (CWE-242)
    system(buf); // Command injection (CWE-78)
    return 0;
}
