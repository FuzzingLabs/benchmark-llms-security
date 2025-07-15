#include <fstream>
#include <cstdlib>
#include <ctime>
#include <iostream>

void infoExposure() {
    std::cout << getenv("PATH") << std::endl; // Information exposure (CWE-200)
}

void weakRandom() {
    srand(time(0));
    std::cout << rand() << std::endl; // Weak random (CWE-338)
}

void improperPermissions() {
    std::ofstream f("/tmp/test.txt");
    f << "test";
    f.close(); // Improper permissions (CWE-732)
}

void unsafeDeserialize() {
    // Simulate unsafe deserialization (CWE-502)
    char buf[100];
    std::cin >> buf;
}
