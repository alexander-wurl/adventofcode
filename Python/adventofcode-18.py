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
        value = EvalExpressionWithPrecedences(d)
        ret += value

    return ret

# main

#t1 = "1 + 2 * 3 + 4 * 5 + 6" # 71 OK
#print( EvalExpressionWithPrecedences(t1) )

#t2 = "1 + (2 * 3) + (4 * (5 + 6))" # 51 OK
#print( EvalExpressionWithPrecedences(t2) )

#t3 = "(2 * 3) + (4 * (5 + 6))" # 50 OK
#print( EvalExpressionWithPrecedences(t3) )

#t4 = "(2 * 3)" # 6 OK
#print( EvalExpressionWithPrecedences(t4) )

#t5 = "2 * 3 + (4 * 5)" #26 OK
#print( EvalExpressionWithPrecedences(t5) )

#t6 = "5 + (8 * 3 + 9 + 3 * 4 * 3)" #437 OK
#print( EvalExpressionWithPrecedences(t6) )

#t7 = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))" # 12240 OK
#print( EvalExpressionWithPrecedences(t7) )

#t8 = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2" # 13632 OK
#print( EvalExpressionWithPrecedences(t8) )

#t9 = "8 * (9 * 7 * 5 + (9 + 8 * 4)) * 9 + (9 * 9 * (3 * 8 + 4) * 9)" #  47988 FALSCH
#print( EvalExpressionWithPrecedences(t9) )

print("solution for part 1: {}".format(part1()))
