# Elementary Ranking Condition (ERC)

Once data is represented in a [comparative tableau](tableaux.md), ranking information is readily accessible as a set of **elementary ranking conditions**, or ERCs. The entire grammar (i.e., all necessary ranking information) can and should be given by the right set of ERCs. 

An ERC is a single row in a comparative tableau. In logical terms, an ERC is a proposition that must be true in the final grammar for the given analysis. The grammar can the be expressed as an **ERC set**, where there are no contradictions between any two ERCs. Recall that a CT shows information about whether a particular constraint prefers the winning candidate or some losing candidate. Therefore, for the intended output to be the winner, a ranking must have every winner-preferring constraint dominate all loser-preferring constraint. Observe the following dummy CT:

<div class="ottab ct" title="Example ERC set">

| /input/ | C1  | C2  | C3  |
| ------- | --- | --- | --- |
| cand1   | W   | L   | L   |
| cand2   | W   | W   | L   |
| cand3   |     | L   | W   |

</div>

Each row in this CT is a valid ERC and can thus be "translated" into an English sentence:

1. row a: C1 must dominate C2 **and** C1 must dominate C3
2. row b: C1 must dominate C3 **or** C2 must dominate C3.
3. row c: C3 must dominate C2. 

The question that remains is: what is the set of constraint orders (or rankings) that satisfies **all** of these propositions? Note that some are compound propositions, joined with *and* or *or*. 

There is in fact one total order that satisfies the ERC set in <lref>: C1 ≫ C3 ≫ C2. The ERC in row a is satisfied because C1 dominates all other constraints. The ERC in row c is satisfied because C3 dominates C2. And crucially, the ERC in row b is satisfied because C1 dominates C3. The sub-proposition "C2 must dominate C3" is not satisfied, but this is acceptable because it is part of a disjunction. The statement as a whole is still true because the left side of the disjunction *is* satisfied. (And for reference, *or* in ERC logic is inclusive.)

> Consider the other possible total orders for this set of three constraints. Can you find for each one how the ERC set is not satisfied?