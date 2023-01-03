package main


import (
	"bufio"	 
	"fmt"
	"os"
)

var r = bufio.NewReader(os.Stdin)
var w = bufio.NewWriter(os.Stdout)

func solve() {
	var n int
	fmt.Fscan(r,&n)
	var s string
	fmt.Fscan(r,&s)
	p := -1
	for _,v := range []byte(s) {
		if int(v) > p {
			p = int(v);
		}
	}
	fmt.Fprintln(w,p-96);

}
func max(a int , b int) int{
	if(a > b)  {
		return a;
	}
	return b;

}
func main(){
	defer w.Flush()
	var n int
	fmt.Fscan(r,&n)
	for i := 1; i <= n; i++ {
		solve()
	}
}