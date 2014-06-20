/*
 * Problem 5: Smallest multiple
 * Find the smallest number that is evenly divisible by integers 1 through 20.
 */
extern crate PEUtils;
use PEUtils::prime_factors;

fn merge(xs : Vec<uint>, ys : Vec<uint>) -> Vec<uint> {
    // initialize vector - at least max of two input vector lengths
    let mut merged = Vec::with_capacity(std::cmp::max(xs.len(), ys.len()));

    // perform merging algorithm
    let mut index_x = 0;
    let mut index_y = 0;
    while index_x < xs.len() && index_y < ys.len() {
        match (xs.get(index_x), ys.get(index_y)) {
            (x, y) if x == y => { 
                merged.push(x.clone()); 
                index_x += 1; 
                index_y += 1; 
            },
            (x, y) if x < y => {
                merged.push(x.clone()); 
                index_x += 1; 
            },
            (_, y) => {
                merged.push(y.clone()); 
                index_y += 1; 
            },
        }
    }

    // add remaining elements, if applicable
    for i in range(index_x, xs.len()) {
        merged.push(xs.get(i).clone());
    }
    for i in range(index_y, ys.len()) {
        merged.push(ys.get(i).clone());
    }

    return merged;
}

fn main() {

    let mut factors : Vec<uint> = Vec::new();
    for i in range(1, 20) {
        factors = merge(factors, PEUtils::prime_factors(i as u64));
    }

    let val = factors.iter().fold(1, |b, &a| b * a);
    println!("{}", val);
}

