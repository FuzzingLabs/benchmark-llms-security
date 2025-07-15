// utils.cpp
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <iostream>

void infoExposure() {
    std::cout << getenv("PATH") << std::endl;
}

void weakRandom() {
    srand(time(0));
    std::cout << rand() << std::endl;
}

void improperPermissions() {
    std::ofstream f("/tmp/test.txt");
    f << "test";
    f.close();
}

void unsafeDeserialize() {
    char buf[100];
    std::cin >> buf;
}
