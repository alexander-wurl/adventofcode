#!/usr/bin/env python

import re

import helper

# returns evaluated expression (string), regular precedences will be ignored
def EvalExpressionWithoutPrecedences(s) -> int:

    # add bracket for each value found in string
    expression = ""
    number_brackets = len(re.findall("\d+", s))
    for _ in range(0, number_brackets):
        expression += "("

    # surround each value with brackets for left to right precedence
    ss = s.split(" ")
    for e in ss:
        expression += str(e + ")") if (bool(re.match("\(*\d+\)*", e))) else str(e)

    return eval(expression)

def EvalExpressionWithPrecedences(s) -> int:

    # find inner term surrounded with brackets
    inner_terms = re.findall("\(([^()]*)\)", s)

    for term in inner_terms:
        # evaluate and replace value with former term
        value = EvalExpressionWithPrecedences( term )
        s = s.replace("(" + term + ")", str(value))

    # find outer term surrounded with brackets
    outer_terms = re.findall("\(([^()]*)\)", s)

    for term in outer_terms:
        # evaluate and replace value with former term
        value = EvalExpressionWithPrecedences( term )
        s = s.replace("(" + term + ")", str(value))

    return EvalExpressionWithoutPrecedences(s)

def part1() -> int:
    data = helper.getData("18")
    ret = 0

    for d in data:
        ret += EvalExpressionWithPrecedences(d)

    return ret

# main

print("solution for part 1: {}".format(part1()))
