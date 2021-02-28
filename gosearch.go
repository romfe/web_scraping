package main

import (
	"flag"
	"fmt"
)

var url = flag.String("u", "noUrl", "url to be analyzed")

func init() {
	flag.Parse()
}

func main() {
	fmt.Println(*url)
}
