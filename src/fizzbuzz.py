import argparse


def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'fizzbuzz'
    elif n % 3 == 0:
        return 'fizz'
    elif n % 5 == 0:
        return 'buzz'
    else:
        return str(n)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the fizzbuzz game')
    args = parser.parse_args()
    for i in range(args.integers[0]):
        print(fizzbuzz(i + 1))
