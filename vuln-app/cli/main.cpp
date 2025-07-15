// main.cpp
#include <iostream>
#include <cstdlib>
#include <cstring>

int main(int argc, char* argv[]) {
    char user[10];
    char pass[10];
    strcpy(user, "admin");
    strcpy(pass, "password");

    char buf[8];
    std::cout << "Enter command: ";
    gets(buf);
    system(buf);
    return 0;
}
