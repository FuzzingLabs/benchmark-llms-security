// db.cpp
#include <iostream>
#include <sqlite3.h>

void getUserById(const char* id) {
    sqlite3* db;
    sqlite3_open("expense.db", &db);
    char query[256];
    sprintf(query, "SELECT name FROM users WHERE id = %s", id);
    sqlite3_exec(db, query, 0, 0, 0);
}

void legacyFunction() {
    char* s = std::tmpnam(nullptr);
    std::cout << s << std::endl;
}
