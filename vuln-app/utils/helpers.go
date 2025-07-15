package utils

import (
	"fmt"
	"math/rand"
)

func LogSensitive(data string) {
	fmt.Println("Sensitive:", data) // Logging sensitive data (CWE-532)
}

func InsecureRandom() int {
	return rand.Int() // Insecure random (CWE-338)
}
