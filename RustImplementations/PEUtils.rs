pub struct Fibonacci {
    a: int,
    b: int,
}

impl Fibonacci {
    pub fn new() -> Fibonacci {
        Fibonacci {a: 0, b: 1}
    }
}

impl Iterator<int> for Fibonacci {
    fn next(&mut self) -> Option<int> {
        // never returns None, since Fibonacci series 
        // doesn't terminate

        // save original a 
        let old_a = self.a;
        // move to next term
        let temp = self.a + self.b;
        self.a = self.b;
        self.b = temp;

        Some(old_a)
    }
}



pub struct PrimeNumbers {
    index : uint,
    prime_numbers : Vec<uint>, 
    next_size : uint,
    highest : uint,
}

impl PrimeNumbers {
    pub fn new() -> PrimeNumbers {
        PrimeNumbers {
            index: 0u,
            prime_numbers: vec![2u],
            next_size: 2u,
            highest: 3u,
        }
    }

    fn expand_primes(&mut self) {
        let mut is_prime = Vec::from_elem(self.next_size, true);

        for p in self.prime_numbers.iter() {
            // calculate starting point 
            let mut curr = (self.highest / *p) * *p;
            if curr < self.highest {
                curr += *p;
            };

            // eliminate all multiples
            while curr < self.highest + is_prime.len() {
                is_prime.as_mut_slice()[curr - self.highest] = false;
                curr = curr + *p;
            }
        }

        // add all found primes to list
        for (index, _) in is_prime.iter()
            .enumerate()
            .filter(|&(_, x)| *x) {
                    self.prime_numbers
                        .push(index + self.highest);
        }

        // increase starting index
        self.highest += self.next_size;
        // double size of sieve
        self.next_size *= 2;
    }
}

impl Iterator<uint> for PrimeNumbers {
    fn next(&mut self) -> Option<uint> {
        // infinite prime numbers, never returns None

        // end of cached numbers, find more
        if self.index == self.prime_numbers.len() {
            self.expand_primes();
        }

        // return number from cache, increment index
        self.index += 1u;
        Some(*self.prime_numbers.get(self.index - 1))
    }
}

pub fn prime_factors(n : u64) -> Vec<uint> {
    let mut primes = PrimeNumbers::new();

    let mut factors = vec![];
    let mut n = n.clone();
    while n > 1 {
        let p = primes.next().clone().unwrap() as u64;
        if p * p > n {
            factors.push(n as uint);
            break;
        }
        
        while n % p == 0 {
            factors.push(p as uint);
            n /= p;
        }
    }

    factors
}

