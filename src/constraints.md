# Constraints

In strict-domination OT, constraints are functions from candidates to non-negative integers. Because a [candidate](candidates.md) is a triplet consisting of (input, output, correspondence), the constraint has access to this structure. Constraints that only consider the output structre are called **markedness** constraints, and constraints that refer to both the input and output structure (and the relation between them) are (usually) **faithfulness** constraints.[^1]

Constraints are said to be negative, meaning they assign violations based on the presence of structure. Intuitively, this  is like thinking "don't have this", rather than "do have that". Because constraints can assign multiple violations per candidate, their definitions should be given in a way that makes this counting clear. A good informal model for a constraint definition is *Assign a violation for every x such that...*. For example:

<div class="fig" title="NoCoda">

Assign a violation for every syllable node that dominates a Coda node.

</div>

Informal verions of this constraint might be phrased as *don't have a coda*, but this is ambiguous. If a candidate contains multiple codas, is it one violation total, or on per coda node? The definition in <lref> makes this clear. 


---

[^1]: Usually, because *anti-faithfulness* is also a thing: while faithfulness constraints penalize differences between input and output, anti-faithfulness constraints are useful when the output must differ in a particular way from the input. 


