package main

import "fmt"

const (
	Good = iota
	Bad
	Evil
)

func one() { fmt.Println("You chose option 1!")}
func two() { fmt.Println("You chose option 2!")}
func three() { fmt.Println("NOO you chose 3, how could you!?")}

var operations = map[string]func(){
	"one": one,
	"two": two,
	"three": three,
}

func main(){
	

	var operation string

	fmt.Print("Choose your option: ")
	fmt.Scan(&operation)
}
