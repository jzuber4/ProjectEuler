/*
 * Problem 6:
 * Find the difference of the sum of the numbers from 1 to 100 squared
 * and the sum of the squares of the numbers from 1 to 100 
 *
 */

fn main() {
    // closed form solutions from WolframAlpha
    let n = 100;
    let total = (n * (n + 1)) / 2;
    let sum_squared = total * total;
    let sum_of_squares = (n * (n + 1) * (2 * n + 1)) / 6;

    println!("{}", sum_squared - sum_of_squares);
}

