#pragma once
#include <string>

class Expense {
public:
    std::string id; // Public field (CWE-522)
    std::string amount; // Public field (CWE-522)
    Expense(std::string i, std::string a) : id(i), amount(a) {} // No input validation (CWE-20)
};
