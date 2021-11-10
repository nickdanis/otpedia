# Elementary Ranking Condition (ERC)

Once data is represented in a [comparative tableau](tableaux.md), ranking information is readily accessible as a set of **elementary ranking conditions**, or ERCs. The entire grammar (i.e., all necessary ranking information) can and should be given by the right set of ERCs. 

An ERC is a single row in a comparative tableau. In logical terms, an ERC is a proposition that must be true in the final grammar for the given analysis. The grammar can the be expressed as an **ERC set**, where there are no contradictions between any two ERCs. Recall that a CT shows information about whether a particular constraint prefers the winning candidate or some losing candidate. Therefore, for the intended output to be the winner, a ranking must have every winner-preferring constraint dominate all loser-preferring constraint. Observe the following dummy CT:

<div class="ottab ct" title="Example ERC set">

| /input/      | C1  | C2  | C3  |
| ------------ | --- | --- | --- |
| winner~cand1 | W   | L   | L   |
| winner~cand2 | W   | W   | L   |
| winner~cand3 | e   | L   | W   |

</div>

Notice that in row d, C1 assigns 'e'. This means that it makes no distiinction between the winner and cand3; the violations it assigns to both are equal. This is usually indicated by a blank sell (to avoid clutter), but when discussing the finer points of ERC logic it is better to show this e explicitly.

Each row in this CT is a valid ERC and can thus be "translated" into an English sentence:

<div class="ottab ct" title="Example ERC set">

| /input/      | C1  | C2  | C3  | ERC translation                                   |
| ------------ | --- | --- | --- | ------------------------------------------------- |
| winner~cand1 | W   | L   | L   | "C1 must dominate C2 **and** C1 must dominate C3" |
| winner~cand2 | W   | W   | L   | "C1 must dominate C3 **or** C2 must dominate C3." |
| winner~cand3 | e   | L   | W   | "C3 must dominate C2."                            |

</div>

The question that remains is: what is the set of constraint orders (or rankings) that satisfies **all** of these propositions? Note that some are compound propositions, joined with *and* or *or*. 

There is in fact one total order that satisfies the ERC set in <lref>: C1 ≫ C3 ≫ C2. The ERC in row a is satisfied because C1 dominates all other constraints. The ERC in row c is satisfied because C3 dominates C2. And crucially, the ERC in row b is satisfied because C1 dominates C3. The sub-proposition "C2 must dominate C3" is not satisfied, but this is acceptable because it is part of a disjunction. The statement as a whole is still true because the left side of the disjunction *is* satisfied. (And for reference, *or* in ERC logic is inclusive.)

> Consider the other possible total orders for this set of three constraints. Can you find for each one how the ERC set is not satisfied?

## Operations over ERC values

Because ERCs can be translated into propositions over *and* and *or*, logical properties of these operators can be straightfowardly applied to individual ERCs as well. Since ERCs are logical propositions, the following operations help find logical entailments between ERCs. 

### L-retraction

Given an ERC E, replacing any L in this ERC with E results in a new ERC F such that E entails F. What this means in practice is as follows. 

<div class="ottab ct" title="Example ERC set">

| /input/      | C1  | C2  | C3  | ERC translation                                   |
| ------------ | --- | --- | --- | ------------------------------------------------- |
| winner~cand1 | W   | L   | L   | "C1 must dominate C2 **and** C1 must dominate C3" |

</div>

In <lref>, the ERC WLL is shown, along with its translation. If, for instance, the second L in WLL is replaced with e, the resulting ERC is WLe, which is translated as follows:

* C1 must dominate C2. 

From here, the logic is simple:

1. Assume P = "C1 must dominate C2"
2. Assume Q = "C1 must dominate C3"
3. WLL = P & Q (def. ERC)
4. WLe = P (def. ERC)
5. If P & Q, then P (def. '&')
6. Therefore, if WLL, then WLe (substutition)

### W-extension

On the disjunctive side, a similar argument can be made: given an ERC E, replacing any e with W will result in an ERC F such that E entails F. Below is the third ERC from the original example CT from this section.

<div class="ottab ct" title="Example ERC set">

| /input/      | C1  | C2  | C3  | ERC translation        |
| ------------ | --- | --- | --- | ---------------------- |
| winner~cand3 | e   | L   | W   | "C3 must dominate C2." |

</div>

In the ERC eLW, if e is replaced with W, the resulting ERC is WLW, which has the following translation:

* C1 must dominate C2 or C3 must dominate C2.

Again, to show that eLW entails WLW is straightforward:

1. Assume P = "C1 must dominate C2"
2. Assume Q = "C3 must dominate C2"
3. eLW = Q (def. ERC)
4. WLW = P or Q (def. ERC)
5. If Q, then P or Q (def. 'or')
6. Therefore, if eLW, then WLW (substitution)

The pragmatics of 5 are a little more obscure ("if you are a cat, then you are a cat or you are a dog" is logically true), but the logic is sound. 

To see if one individual ERC A entails another individual ERC B, look for a chain of L-retractions and W-extensions to get from one to the other. If such a path exists, ERC A entails ERC B. 

### Fusion

Fusion is an operation over W, L, and e that determins what information is entailed by a *set* of ERCs. If A and B are ERCs, then the fusion is A◦B. To calculate the fusion of an ERC set, apply the following position-by-position (constraint by constraint) to the ERC set:

<div class="fig" title="Def. Fusion, where X = W, L, or e:"> 

| Operation     | Comment                  |
| ------------- | ------------------------ |
| X◦X = X       | X fused with itself is X |
| X◦L = L◦X = L | X fused with L is L      |
| X◦e = e◦X = X | X fused with e is X      |

</div>

To repeat the example from {{#cite Prince2002}}:9, two ERCs are shown along with their fusion in the CT below.

<div class="ottab ct" title="ERC Fusion">

|     | C1  | C2  | C3  |
| --- | --- | --- | --- |
| A   | W   | L   | e   |
| B   | e   | W   | L   |
| A◦B | W   | L   | L   |

</div>

The fusion operations are applied individually per each column, so taking the definition above, each of the following apply (essentially the above tableau, transposed):

1. C1: W◦e = W
2. C2: L◦W = L
3. C3: e◦L = L

The resulting ERC is WLL, meaning that in an ERC set where both ERCs A and B are true, then it must also be the case that the resulting ERC A◦B is also true. Indivudally, neither A or B says anything jointly about C1 and C3. If we visualize the Hasse diagram for A and B, it's clear to see why A◦B hold, knowing that the domination relation is transitive, but we can also prove this via fusion without leaving our ERCs. Also beware that A◦B is **less informative** than A and B together; the fustion does not tell us anything about how C2 and C3 relate to each other, which B tells us exactly this. Thus, the fustion of two ERCs A and B is not **everything** that is entailed by A and B, but the results of fusion will be **something** entailed by A and B. 