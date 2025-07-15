#include <iostream>
#include <sqlite3.h>

void getUserById(const char* id) {
    sqlite3* db;
    sqlite3_open("expense.db", &db); // No error check (CWE-252)
    char query[256];
    sprintf(query, "SELECT name FROM users WHERE id = %s", id); // SQL injection (CWE-89)
    sqlite3_exec(db, query, 0, 0, 0);
}

void legacyFunction() {
    // Deprecated function usage (CWE-676)
    char* s = std::tmpnam(nullptr);
    std::cout << s << std::endl;
}
