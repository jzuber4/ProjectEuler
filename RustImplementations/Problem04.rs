/*
 Problem 4: Largest Palindrome Product
 Find the largest palindrome number that is a product of two three digit numbers
*/

// returns whether the input val is a palindrome number
// in base 10
fn is_palindrome(val : int) -> bool {
    // zip the string with its reverse, compare pairs
    for (normal, reverse) in val.to_str().as_slice().chars()
        .zip(val.to_str().as_slice().chars().rev()) {
        if normal != reverse {
            return false;
        };
    }
    // all match
    true
}

fn main() {
    // highest palindrome of three digit numbers
    // most likely has factors in high range
    let mut max_val = 0;
    for i in range(900, 1000) {
        for j in range(i, 1000) {
            let v = i * j;
            if is_palindrome(v) {
                max_val = if v > max_val {
                    v
                } else {
                    max_val
                }
            }
        }
    }
    println!("{}", max_val);
}
