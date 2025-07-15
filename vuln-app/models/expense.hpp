// expense.hpp
#pragma once
#include <string>

class Expense {
public:
    std::string id;
    std::string amount;
    Expense(std::string i, std::string a) : id(i), amount(a) {}
};
