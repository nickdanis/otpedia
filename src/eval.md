# EVAL

EVAL is the component that evaluates the candidates based on a specific ranking of CON. Given an ordering of constraints and a candidate set, EVAL filters the candidate set until only the candidate (or candidates) survives that is *most harmonic*, or optimal. Essentially, the candidate with the fewest violations for the given constraint ranking survives.