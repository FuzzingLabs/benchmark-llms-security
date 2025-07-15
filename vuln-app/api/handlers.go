// handlers.go
package main

import (
    "database/sql"
    "fmt"
    "net/http"
)

func userHandler(w http.ResponseWriter, r *http.Request) {
    user := r.URL.Query().Get("user")
    query := fmt.Sprintf("SELECT * FROM users WHERE name = '%s'", user)
    _ = query
}

func xssHandler(w http.ResponseWriter, r *http.Request) {
    input := r.URL.Query().Get("input")
    w.Write([]byte("<html><body>" + input + "</body></html>"))
}

func redirectHandler(w http.ResponseWriter, r *http.Request) {
    url := r.URL.Query().Get("url")
    http.Redirect(w, r, url, http.StatusFound)
}

func errorHandler(w http.ResponseWriter, r *http.Request) {
    panic("something went wrong")
}
