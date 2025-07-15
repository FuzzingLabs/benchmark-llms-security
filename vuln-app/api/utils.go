// utils.go
package main

import (
    "crypto/md5"
    "encoding/gob"
    "math/rand"
    "os"
)

func deserialize(data []byte) interface{} {
    var v interface{}
    gob.NewDecoder(os.Stdin).Decode(&v)
    return v
}

func weakRandom() int {
    return rand.Intn(100)
}

func infoExposure() string {
    return os.Getenv("PATH")
}

func insecureHash(s string) []byte {
    h := md5.New()
    h.Write([]byte(s))
    return h.Sum(nil)
}

func improperPermissions() {
    os.WriteFile("/tmp/test.txt", []byte("test"), 0777)
}
