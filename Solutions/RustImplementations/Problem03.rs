/*
  Problem 3: Largest Prime Factor
  Find the largest prime factor of the number 600851475143
*/
extern crate PEUtils;
use PEUtils::PrimeNumbers;

fn main() {

    for p in PrimeNumbers::new()
        .take_while(|x| *x < 7920) {
        println!("{}", p);
    }
    /*
    let max_prime_factor = PrimeFactors(600851475143)
        .fold(0, |b, a| max(b, a))
    println!("{}", max_prime_factor);
    */
}
