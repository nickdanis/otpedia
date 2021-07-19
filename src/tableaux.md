# Tableaux

Much of the claims and argumentation for OT are demonstrated using tableaux (sg. tableau). A properly formatted tableau gives information both on the candidates and constraints, as well as some language-specific ranking information. There are two general types of tableaux, each eith their own purposes: violation tableaux (VTs) and comparative tableaux (CTs). 

## Violation Tableaux

A violation tableau shows the [constraints](constraints.md) as column headings and one [candidate](candidates.md) per row. The violation marks incurred by each candidate are shown in the corresponding cells either as a number of asterisks (e.g. \*\*\*).

<div class="ottab vt" title="Example VT with finger">

|         | /panpa/ | Max | Dep | Agree | Ident |
| ------- | ------- | --- | --- | ----- | ----- |
|         | panpa   |     |     | *     |       |
| &#9758; | pampa   |     |     |       | *     |
|         | papa    | *   |     |       |       |
|         | panapa  |     | *   |       |       |
|         | panaapa |     | **  |       |       |

</div>

The style in <lref> is extremely common, especially in work throughout the 1990s and early 2000s. It is also common to use an arrow instead of the finger icon to indicate the winner, and to use integers instead of asterisks to show violation counts. Thus, the following two tableaux are equivalent in information to <lref>, and differ only in their style of presentation.  

<div class="ottab vt" title="Example VT with arrow">

|     | /panpa/ | Max | Dep | Agree | Ident |
| --- | ------- | --- | --- | ----- | ----- |
|     | panpa   |     |     | *     |       |
| →   | pampa   |     |     |       | *     |
|     | papa    | *   |     |       |       |
|     | panapa  |     | *   |       |       |
|     | panaapa |     | **  |       |       |

</div>

<div class="ottab vt" title="Example VT with arrow and integer violation marks">

|     | /panpa/ | Max | Dep | Agree | Ident |
| --- | ------- | --- | --- | ----- | ----- |
|     | panpa   |     |     | 1     |       |
| →   | pampa   |     |     |       | 1     |
|     | papa    | 1   |     |       |       |
|     | panapa  |     | 1   |       |       |
|     | panaapa |     | 2   |       |       |

</div>

Usually, the columns are ordered left-to-right in a way that reflects their intended [ranking](rankings.md) for that language; however, VTs are **not** the best vehicle for conveying ranking information. **Any arguments about ranking should be made with CTs**, described in the next section. 

That being said, there are a number of other conventions for VTs relating to ranking. If there is a solid vertical rule between two constraint columns, that is (usually) meant to indicate that those two constraints are curically ordered with respect to each other (such that the constraint on the left must dominate the constraint on the right). Likewise, if there is a dashed line separating two columns, that means those two constraints are *not* crucially ordered with respect to each other. I don't follow this convention here, as it leads to ambiguity and it's tricky to format.

In any of the VTs above, for instance, if it is assumed that the intended ranking is the order of constraints as listed left-to-right, the optimal candidate can be found as follows: For the first constraint, which candidate (or set of candidates) receives the fewest violations? Then, for the next column, of these remaining candidates, which of *these* receives the fewest violations of this next constraint? THis filtration continues until there is a non-empty set that cannot be further differentiated. This set (usually a singleton set, but not necessarily) is the optimum. 

Additionally, an exclamation mark inside a VT indicates a *fatal violation*, or a particular violation mark that crucially separates two candidates. 

<div class="ottab vt" title="VT showing fatal violations">

|         | /ta/ | *a      |
| ------- | ---- | ------- |
| &#9758; | ta   | \*      |
|         | taa  | \*\*!   |
|         | taaa | \*\*!\* |

</div>

In dummy VT <lref>, all three candidates, [ta], [taa], and [taaa], incur one violation of \*a, so these violation marks effectively cancel out. However, [taa] has a second violation while [ta] does not (and likewise for [taaa]). The exclamation mark is placed right after this violation to show that it is *fatal*, or is the death knell for this candidate. It is not uncommon to also see all cells to the right of an exclamation mark shaded gray to indicate that this candidate is no longer a possible optimum. 

> Do not confuse a tableau with the analysis itself. Showing a tableau is helpful if done appropriately, but an analysis consists of clear definitions of GEN and CON, with arguments that all relevant candidates have been considered and all informative ranking conditions given. A tableau can help with these arguments, but it is not a substitution for these arguments. 

## Comparative Tableaux

Comparative tableaux are a transformation from VTs into an object that conveys explicit ranking information. In a CT, each row now represents a comparison between the winning candidate (optimum) and a particular loser, or a W~L pair. (The tilde in this context indicates that two forms are being explicitly compared.) Each row in a CT is an [elementary ranking condition](erc.md).

Instead of violation counts, the crucial information in a CT is now: does a particular constraint prefer the winner, or does it prefer the loser? Here, "prefer" refers to the number of violation marks assigned by a constraint. A constraint that assigns fewer marks to form A than to form B is said to prefer form A. 

Any VT with clear violation marks and intended winner can be turned into a CT in a few steps. The CT version of the VT from the previous section is shown below.

<div class="ottab ct" title="'Pure' CT">

| /panpa/       | Max | Dep | Agree | Ident |
| ------------- | --- | --- | ----- | ----- |
| pampa~panpa   |     |     | W     | L     |
| pampa~papa    | W   |     |       | L     |
| pampa~panapa  |     | W   |       | L     |
| pampa~panaapa |     | W   |       | L     |

</div>

Notice that the majority of information conveyed are just cells with either a W or an L. In the first column, the constraint Max is shown with a W in the row for [papa]. The candidate [papa] contains one instance of deletion, so when this is compared with the winner [pampa], which has 0 instances of deletion, Max prefers the winner, and thus a W is marked. No other candidates contain instances of deletion, so Max has no preference with respect to these. 

In the above tableau, the winner is shown on the first row, with violation marks still present. This is only for convenience and can be ommitted. A pure CT contains only Ws and Ls. However, in this representation, it might not be clear exactly *how* violations are assigned. A "hybrid" tableau style is popular that includes both the Ws and Ls of CTs, and the violation marks of VTs.

<div class="ottab hy" title="Hybrid CT">

| /panpa/ | Max   | Dep    | Agree  | Ident |
| ------- | ----- | ------ | ------ | ----- |
| pampa   |       |        |        | \*    |
| panpa   |       |        | W   \* | L     |
| papa    | W  \* |        |        | L     |
| panapa  |       | W \*   |        | L     |
| panaapa |       | W \*\* |        | L     |

</div>

In <lref>, the violation marks are shown explicitly as in a plain VT. The winner, or optimum, is now in the first row. Each subsequent row (labeled by lowercase letters) is a comparison between that losing candidate and the winning candidate in the first row. A hybrid CT thus shows explicit violation marks *and* clear ranking information, making it a very informative way to present the analysis. 

In this guide, I will show VTs using arrows and either numerals or asterists, and hybrid CTs with numerals. This closely (but not exactly) follows the conventions in {{#cite McCarthy2008}}. 

