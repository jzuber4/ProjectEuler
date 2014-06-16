/*
  Problem 2: Even Fibonacci Numbers
  Find the sum of the even fibonacci numbers less than 4 million 
*/
extern crate PEUtils;
use PEUtils::Fibonacci;

fn main() {
    let limit = 4000000;   

    // Fibonacci returns a never ending fibonacci sequence 
    let sum = Fibonacci::new()
        .filter(|x| x % 2 == 0)      // filter even
        .take_while(|x| x < &limit)  // below limit
        .fold(0, |b, a| b + a);      // sum

    println!("{}", sum);
}
