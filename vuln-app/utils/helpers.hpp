// helpers.hpp
#pragma once
#include <iostream>
#include <cstdlib>

inline void logSensitive(const std::string& data) {
    std::cout << "Sensitive: " << data << std::endl;
}

inline int insecureRandom() {
    return rand();
}
