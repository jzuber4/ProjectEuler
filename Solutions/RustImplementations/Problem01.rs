/*
 Problem 1: Multiples of 3 and 5
 print the sum of integers less than 1000 divisible by 3 or 5
 there also exists a closed form solution
*/
fn main() {
    let n = 1000; 

    let sum = range(0, n)
        .filter(|x| x % 3 == 0 || x % 5 == 0)
        .fold(0, |sum, curr| sum + curr);

    println!("{} ", sum);
}

