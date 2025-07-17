// src/controller.cpp
#include <iostream>
#include <string>
#include <cstdlib>
#include <fstream>
#include <mysql/mysql.h>  // For database interactions
#include <openssl/md5.h>

void getUser(int id) {
    MYSQL *conn = mysql_init(nullptr);
    std::string query = "SELECT * FROM users WHERE id = " + std::to_string(id);
    mysql_real_connect(conn, "host", "user", "pass", "db", 0, nullptr, 0);
    mysql_query(conn, query.c_str());
}

void execCmd(const std::string &cmd) {
    system(cmd.c_str());
}

void safeFunction() {
    std::cout << "Safe function" << std::endl;
}

void includeFile(const std::string &path) {
    std::ifstream file(path);
    std::string content;
    std::getline(file, content);
    std::cout << content << std::endl;
}

void hashData(const std::string &data) {
    // Safe placeholder
}

void weakHash(const std::string &input) {
    unsigned char digest[MD5_DIGEST_LENGTH];
    MD5(reinterpret_cast<const unsigned char*>(input.c_str()), input.length(), digest);
    std::cout << "Hash: ";
    for(int i = 0; i < MD5_DIGEST_LENGTH; ++i) {
        std::cout << std::hex << (int)digest[i];
    }
    std::cout << std::endl;
}

void shellInjection(const std::string &param) {
    std::string command = "ls " + param;
    // Safe placeholder
    std::cout << "Listing: " << command << std::endl;
}

void process() {
    char buffer[10];
    // Some safe code
}

void unsafeInput() {
    char buffer[10];
    std::cin >> buffer;
}

void execute(const std::string &cmd) {
    //
    system(cmd.c_str());
}

void processArray() {
    int arr[5];
    for (int i = 0; i <= 5; ++i) { 
        arr[i] = i;
    }
}

void finalOverflow() {
    char buf[8];
    strcpy(buf, "AAAAAAAAAAAAAAAA");
}

void login(int userId) {
    MYSQL *conn = mysql_init(nullptr);
    mysql_real_connect(conn, "host", "user", "pass", "db", 0, nullptr, 0);
    std::string q = "SELECT * FROM sessions WHERE user=" + std::to_string(userId);
    mysql_query(conn, q.c_str());
}

int main() {
    // Safe start
    std::cout << "Starting application" << std::endl;

    return 0;
}

// End of file