package main


import (
	"bufio"
	"fmt"
	"os"	 
	"sort"
)

var r = bufio.NewReader(os.Stdin)
var w = bufio.NewWriter(os.Stdout)

func solve() {
	// var a,b,c int
	a := make([]int,3)
	fmt.Fscan(r,&a[0],&a[1],&a[2])
	sort.Ints(a)
	
	fmt.Fprintln(w,a[1])
}
func main(){
	defer w.Flush()
	var n int
	fmt.Fscan(r,&n)
	for i := 1; i <= n; i++ {
	    solve()
	}
	
}