from PEUtils import Fibonacci

def main():
    f = Fibonacci()
    v = f.next()
    sum_val = 0
    while v < 4000000:
        if v % 2 == 0:
            sum_val += v
        v = f.next()

    print sum_val

main()

