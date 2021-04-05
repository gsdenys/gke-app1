package main

import (
	"net/http"
	"text/template"

	"github.com/gorilla/mux"
)

var templates *template.Template

func html(w http.ResponseWriter, r *http.Request) {
	templates.ExecuteTemplate(w, "index.html", nil)
}

// func css(w http.ResponseWriter, r *http.Request) {
// 	templates.ExecuteTemplate(w, "index.css", nil)
// }

func main() {
	templates = template.Must(template.ParseGlob("templates/index.html"))
	r := mux.NewRouter()

	r.HandleFunc("/", html).Methods("GET")
	// r.HandleFunc("/css", css).Methods("GET")

	http.Handle("/", r)
	http.ListenAndServe(":3000", nil)
}
