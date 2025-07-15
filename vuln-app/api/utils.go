package main

import (
	"crypto/md5"
	"encoding/gob"
	"math/rand"
	"os"
)

func deserialize(data []byte) interface{} {
	var v interface{}
	gob.NewDecoder(os.Stdin).Decode(&v) // Unsafe deserialization (CWE-502)
	return v
}

func weakRandom() int {
	return rand.Intn(100) // Weak random (CWE-338)
}

func infoExposure() string {
	return os.Getenv("PATH") // Information exposure (CWE-200)
}

func insecureHash(s string) []byte {
	h := md5.New() // Use of insecure hash (CWE-327)
	h.Write([]byte(s))
	return h.Sum(nil)
}

func improperPermissions() {
	os.WriteFile("/tmp/test.txt", []byte("test"), 0777) // Improper permissions (CWE-732)
}
