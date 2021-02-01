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

    # surround each value with brackets
    ss = s.split(" ")
    for e in ss:
        expression += str(e + ")") if (bool(re.match("\(*\d+\)*", e))) else str(e)
   
    return eval(expression)    

def EvalExpressionWithPrecedences(s) -> int:

    # consider + and * expressions with 2 terms
    expressions = re.findall("\(\d* [+*] \d*\)", s)

    while ( len(expressions) > 0 ):

        for pe in expressions:
            s = s.replace(pe, str(eval(pe)))
        
        expressions = re.findall("\(\d* \+ \d*\)", s)

    # if brackets still exist
    if (re.findall("\(", s)):
        
        # find inner term surrounded with brackets
        inner_terms = re.findall("\(([^())]+)\)", s)

        # may be to do with more than one inner term ...
        for term in inner_terms:
            # evaluate and replace value with former term
            s = s.replace(term, str(EvalExpressionWithPrecedences( term )))

        # return recombined string
        return EvalExpressionWithoutPrecedences(s)

    else:
        return EvalExpressionWithoutPrecedences(s)

def part1() -> int:
    data = helper.getData("18")
    ret = 0

    for d in data:
        value = EvalExpressionWithPrecedences(d)
        print(d + " = {}".format(value))
        ret += value

    return ret

# main

#a = "1 + 2 * 3 + 4 * 5 + 6" # 71 OK
#print( EvalExpressionWithoutPrecedences(a) )

#b = "1 + (2 * 3) + (4 * (5 + 6))" # 51 OK
#print( EvalExpressionWithPrecedences(b) )

#b2 = "(2 * 3) + (4 * (5 + 6))" # 50 OK
#print( EvalExpressionWithPrecedences(b2) )

#b3 = "(2 * 3)" # 6 OK
#print( EvalExpressionWithPrecedences(b3) )

#c = "2 * 3 + (4 * 5)" #26 OK
#print( EvalExpressionWithPrecedences(c) )

#d = "5 + (8 * 3 + 9 + 3 * 4 * 3)" #437
#print( EvalExpressionWithPrecedences(d) )

#e = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))" # 12240 OK
#print( EvalExpressionWithPrecedences(e) )

#f = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2" # 13632 OK
#print( EvalExpressionWithPrecedences(f) )

print("solution for part 1: {}".format(part1()))
