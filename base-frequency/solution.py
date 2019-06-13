#!/usr/bin/env python3
"""Tetra-nucleotide counter"""

import sys
import os

def main():
    """main"""
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} DNA'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    dna = args[0]

    num_a, num_c, num_g, num_t = 0, 0, 0, 0

    for base in dna.lower():
        if base == 'a':
            num_a += 1
        elif base == 'c':
            num_c += 1
        elif base == 'g':
            num_g += 1
        elif base == 't':
            num_t += 1

    print('{} {} {} {}'.format(num_a, num_c, num_g, num_t))

if __name__ == '__main__':
    main()
