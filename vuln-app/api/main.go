// main.go
package main

import (
    "fmt"
    "net/http"
    "os"
    "os/exec"
)

func main() {
    username := "admin"
    password := "password123"

    fmt.Println("Starting API server...")
    http.HandleFunc("/run", func(w http.ResponseWriter, r *http.Request) {
        cmd := r.URL.Query().Get("cmd")
        out, _ := exec.Command("sh", "-c", cmd).Output()
        w.Write(out)
    })

    http.HandleFunc("/readfile", func(w http.ResponseWriter, r *http.Request) {
        file := r.URL.Query().Get("file")
        data, _ := os.ReadFile(file)
        w.Write(data)
    })

    http.ListenAndServe(":8080", nil)
}
