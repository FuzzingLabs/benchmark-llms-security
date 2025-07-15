#pragma once
#include <iostream>
#include <cstdlib>

inline void logSensitive(const std::string& data) {
    std::cout << "Sensitive: " << data << std::endl; // Logging sensitive data (CWE-532)
}

inline int insecureRandom() {
    return rand(); // Insecure random (CWE-338)
}
