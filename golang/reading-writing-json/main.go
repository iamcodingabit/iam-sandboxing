package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"os"
)

type Video_game[] struct {
	Title string `json:"title"`
	Status string `json:"status"`
}

func main(){
	file, _ := os.ReadFile("video-games.json")

	var video_game Video_game
	json.NewDecoder(bytes.NewBuffer(file)).Decode(&video_game)

	for i := range len(video_game) {
		fmt.Printf("%s, %s\n", video_game[i].Title, video_game[i].Status)
	}
}