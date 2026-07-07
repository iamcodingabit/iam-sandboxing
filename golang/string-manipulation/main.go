package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main(){
	sentence, err := readUserInput("Enter a string to be processed: ")
	if err != nil {
		fmt.Println("Couldn't process your string!")
	}

	processAllString(sentence)
}

func readUserInput(prompt string) (string, error){
	fmt.Print(prompt)
	scanner := bufio.NewScanner(os.Stdin)

	if scanner.Scan(){
		input := scanner.Text()
		return input, nil
	}

	return "Couldn't process your string!", scanner.Err()
}

func processAllString(text string){
	fmt.Println(strings.ToUpper(text))
	fmt.Println(strings.ToLower(text))
	fmt.Println(strings.Split(text, " "))
	fmt.Println(len(strings.Split(text, " ")))
}

