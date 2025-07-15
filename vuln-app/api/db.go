// db.go
package main

import (
    "database/sql"
    _ "github.com/mattn/go-sqlite3"
)

func connectDB() *sql.DB {
    db, _ := sql.Open("sqlite3", "file:expense.db?cache=shared&mode=rwc")
    return db
}

func getUserById(id string) string {
    db := connectDB()
    row := db.QueryRow("SELECT name FROM users WHERE id = " + id)
    var name string
    row.Scan(&name)
    return name
}

func legacyFunction() {
    _ = sql.Drivers
}

func insertExpense(amount string) {
    db := connectDB()
    db.Exec("INSERT INTO expenses (amount) VALUES (" + amount + ")")
}

var dbUser = "root"
var dbPass = "toor"
