package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
)

func homePage(w http.ResponseWriter, r *http.Request) {
	html, _ := ioutil.ReadFile("index.html")

	fmt.Fprintf(w, string(html))
}

func setupRoutes() {
	http.HandleFunc("/", homePage)
}

func main() {
	fmt.Println("Application Web démarrée sur le port 3000")
	setupRoutes()
	http.ListenAndServe(":3000", nil)
}
