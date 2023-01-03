use std::io;
 
fn input() -> Vec<i32> {
    let mut vec: Vec<i32> = Vec::new();
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).expect("Failed to read line");
    for num in buffer.split_whitespace() {
        vec.push(num.parse::<i32>().unwrap());
    }
    vec
}
 
fn main() {
    let t = input();
    let mut t = t[0];
    while t > 0 {
        t -= 1;
        let mut a = input();
        a.sort();
        println!("{}", a[1]);
    }
}