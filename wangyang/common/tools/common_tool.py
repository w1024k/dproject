# coding=utf-8
import random


def create_random_string(digits=10):
    chars = random.sample(
        ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e',
         'd', 'c', 'b', 'a', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], digits)
    return ''.join(chars)
