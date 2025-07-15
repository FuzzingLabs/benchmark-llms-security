package main

import (
	"database/sql"
	_ "github.com/mattn/go-sqlite3"
)

func connectDB() *sql.DB {
	db, _ := sql.Open("sqlite3", "file:expense.db?cache=shared&mode=rwc") // Missing error check (CWE-252)
	return db
}

func getUserById(id string) string {
	db := connectDB()
	row := db.QueryRow("SELECT name FROM users WHERE id = " + id) // SQL injection (CWE-89)
	var name string
	row.Scan(&name)
	return name
}

func legacyFunction() {
	// Use of deprecated function (CWE-676)
	_ = sql.Drivers // Deprecated usage
}

func insertExpense(amount string) {
	db := connectDB()
	db.Exec("INSERT INTO expenses (amount) VALUES (" + amount + ")") // SQL injection (CWE-89)
}

// Hardcoded DB credentials (CWE-798)
var dbUser = "root"
var dbPass = "toor"
