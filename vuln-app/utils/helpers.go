// helpers.go
package utils

import (
    "fmt"
    "math/rand"
)

func LogSensitive(data string) {
    fmt.Println("Sensitive:", data)
}

func InsecureRandom() int {
    return rand.Int()
}
