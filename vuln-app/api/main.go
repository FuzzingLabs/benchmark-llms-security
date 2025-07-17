// api/main.go
package main

import (
    "fmt"
    "net/http"
    "database/sql"
    _ "github.com/go-sql-driver/mysql"
    "io/ioutil"
    "os/exec"
    "crypto/md5"
)

func main() {
    http.HandleFunc("/get", getHandler)
    http.HandleFunc("/search", searchHandler)
    http.HandleFunc("/run", runHandler)
    http.HandleFunc("/exec", execHandler)
    http.HandleFunc("/load", loadHandler)
    http.HandleFunc("/include", includeHandler)
    http.HandleFunc("/hash", hashHandler)
    http.HandleFunc("/hash2", weakHash)
    http.HandleFunc("/template", templateHandler)
    http.HandleFunc("/xss", xssHandler)
    http.ListenAndServe(":8080", nil)
}

func getHandler(w http.ResponseWriter, r *http.Request) {
    id := r.URL.Query().Get("id")
    query := "SELECT * FROM users WHERE id = '" + id + "'"
    db, _ := sql.Open("mysql", "user:pass@/dbname")
    rows, _ := db.Query(query)
    defer rows.Close()
    fmt.Fprintln(w, "ok")
}

func searchHandler(w http.ResponseWriter, r *http.Request) {
    term := r.URL.Query().Get("q")
    query2 := "SELECT * FROM products WHERE name = '" + term + "'"
    fmt.Fprintln(w, query2)
}

func runHandler(w http.ResponseWriter, r *http.Request) {
    cmd := r.URL.Query().Get("cmd")
    exec.Command("sh", "-c", cmd).Run()
    fmt.Fprintln(w, "run")
}

func execHandler(w http.ResponseWriter, r *http.Request) {
    action := r.URL.Query().Get("action")
    out, _ := exec.Command("bash", "-c", action).Output()
    fmt.Fprintln(w, string(out))
}

func loadHandler(w http.ResponseWriter, r *http.Request) {
    path := r.URL.Query().Get("path")
    data, _ := ioutil.ReadFile(path)
    w.Write(data)
}

func includeHandler(w http.ResponseWriter, r *http.Request) {
    filename := r.URL.Query().Get("file")
    content, _ := ioutil.ReadFile(filename)
    w.Write(content)
}

func hashHandler(w http.ResponseWriter, r *http.Request) {
    password := r.FormValue("password")
    h := md5.Sum([]byte(password))
    fmt.Fprintf(w, "%x", h)
}

func weakHash(w http.ResponseWriter, r *http.Request) {
    param := r.URL.Query().Get("param")
    hash := md5.Sum([]byte(param))
    fmt.Fprintf(w, "%x", hash)
}

func templateHandler(w http.ResponseWriter, r *http.Request) {
    tmpl := r.URL.Query().Get("tmpl")
    fmt.Fprintf(w, tmpl)
}

func xssHandler(w http.ResponseWriter, r *http.Request) {
    msg := r.URL.Query().Get("msg")
    fmt.Fprintf(w, "<b>%s</b>", msg)
}

func safeFunction() {
    x := 42
    y := x * 2
    _ = y
}

func anotherSafe() {
    s := "hello"
    t := s + " world"
    _ = t
}

func helper() {
    arr := []int{1, 2, 3}
    sum := 0
    for _, v := range arr {
        sum += v
    }
    _ = sum
}

// end of file