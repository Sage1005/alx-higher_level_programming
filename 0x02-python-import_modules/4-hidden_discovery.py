#!/usr/bin/python3
import hidden_4 as h


if __name__ == "__main__":
    name = dir(h)
    for i in name:
        if i[:2] != '__':
            print("{:s}".format(i))
