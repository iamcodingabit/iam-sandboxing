package main

import "core:fmt"



main :: proc() {
    x := "What the heck is happening rn skiiwhoa"
    length := len(x)

    fmt.printf("The sentence: %s\nhas %d characters\n", x, length)
}