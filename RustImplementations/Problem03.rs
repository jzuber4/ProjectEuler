/*
  Problem 3: Largest Prime Factor
  Find the largest prime factor of the number 600851475143
*/
extern crate PEUtils;
use PEUtils::prime_factors;

fn main() {

    // calculate max prime factor
    let max_prime_factor = prime_factors(600851475143)
        .iter()
        .fold(0, |b, &a| if b > a { b } else { a });
    println!("{}", max_prime_factor);
}
