/*
 * Problem 07: 10001st prime
 * Finds the 10001st prime number
 */
extern crate PEUtils;
use PEUtils::PrimeNumbers;

fn main() {
    let n = 10001;
    // get 10001st element from generator
    let p = PrimeNumbers::new().nth(n - 1);

    println!("{}", p.unwrap());
}


