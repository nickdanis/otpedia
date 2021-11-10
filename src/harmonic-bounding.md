# Harmonic bounding

A candidate is **harmonically bounded** if it can never be a winner under any constraint ranking. This means it is always worse than some other candidate (or candidates). In terms of violations, it's violation profile is a **superset** of some other candidate's (or candidates'). There are two types of harmonic bounding: simple and collective.

## Simple harmonic bounding

Observe the following example VT:

<div class="ottab vt" title="Harmonic bounding">

|     | /panpa/ | Max | Dep | Agree | Ident |
| --- | ------- | --- | --- | ----- | ----- |
|     | panpa   |     |     | *     |       |
| →   | pampa   |     |     |       | *     |
|     | papa    | *   |     |       |       |
|     | panapa  |     | *   |       |       |
|     | panaapa |     | **  |       |       |

</div>

The first four candidates each contain a single constraint violation. Candidate d contains a single violation of Dep as it contains an epenthesized vowel. Candidate e contains two epenthesized vowels, and thus two violations of Dep. However, adding this second epenthesized vowel does not benefit the candidate in any additional way beyond a single epenthesized vowel. For every constraint, candidate does **the same or worse** than candidate e, and thus **candidate e is harmonically bounded by candidate d**. 

Note that claims about harmonic bounding can only be made once CON is defined. If a constraint is later introduced that says something like HaveFourVowels, then candidate e is now better than candidate d with respect to this constraint, and is no longer bounded. However, this is the danger in "introducing" constraints later in your analysis; previous claims about ranking might no longer be valid. In giving an analysis, it is best to define CON at the start.

What happens in a comparative tableau when the simply bounded candidate is assumed to be the winner?

<div class="ottab hy" title="CT with bounded as winner">

| /panpa/ | Max | Dep | Agree | Ident |
| ------- | --- | --- | ----- | ----- |
| panaapa |     | **  |       |       |
| panpa   |     | L   | W *   |       |
| pampa   |     | L   |       | W *   |
| papa    | W * | L   |       |       |
| panapa  |     | L * |       |       |

</div>

Recall that for an [ERC](erc.md) to be satisfied, *every L must be dominated by some W*. The ERC in row d contains no Ws, and thus it can never be satisfied, and therefore [panaapa] can never be the winner. 

If we swap roles, and assume that the *bounder*, and not the bounded, is the winner, the bounded candidate also makes itself known:

<div class="ottab hy" title="CT with bounder as winner">

| /panpa/ | Max | Dep  | Agree | Ident |
| ------- | --- | ---- | ----- | ----- |
| panapa  |     | *    |       |       |
| panpa   |     | L    | W *   |       |
| pampa   |     | L    |       | W *   |
| papa    | W * | L    |       |       |
| panaapa |     | W ** |       |       |

</div>

In <lref>, the ERC in row d now contains a W, but no Ls. Thus, it *is* trivially satisfied, but it is not informative; there is no ranking information. This makes sense, as it *is* possible for [panapa] to be a winner (as the above is a consistent ERC set), but we can easily spot that the inclusion of [panaapa] as a candidate, under this definition of CON, isn't adding anything to the analysis. 

A simply-bounded candidate as the winner in a CT will reveal its bounder as the candidate with the ERC containing Ls but no Ws, and the bounder as the winner will reveal the simply bounded candidate as the comparison containing Ws but no Ls. 

## Collective harmonic bounding

A single candidate can also be bounded by multiple other candidates. This is known as **collective harmonic bounding**. Observe the VT below. Let's assume that GEN only generates candidates of well-formed CV syllables, and CON is as shown.

<div class="ottab vt" title="Collective harmonic bounding">

|     | /at/ | Max | Dep |
| --- | ---- | --- | --- |
|     | ∅    | **  |     |
|     | tata |     | **  |
|     | ta   | *   | *   |

</div>

Candidate a is a well-formed syllable in a trivial sense in that it contains no structure at all; this results in two violations of Max as two segments wer deleted. This is the null parse candidate. Candidate b contains two well-formed syllables, at the cost of inserting both a consonant and a vowel for 2 Dep violations. Candidate c might seem like a reasonable alternative, as it contains a single well-formed syllable, with 1 deletion (input segment /t/) and one insertion (output segment [t]). Additionally, [ta] does better than [tata] on Dep, and does better than the null parse on Max. The violation profile for [ta] is not a superset of any other individual candidate alone, and thus is not simply bounded. However, its fate is sealed in other ways. 

> What does the correspondence diagram for /at/→[ta] look like based on the above description?

In this toy system, there are only two possible linear rankings, and therefore only two possible grammars:

1. Max ≫ Dep
2. Dep ≫ Max

In the first ranking, [tata] is the clear winner as it incurs 0 violations of the first constraint, while [ta] contains 1 and the null parse contains 2. In the opposite ranking, the null parse ∅ is the clear winner as it incurs 0 violations of Dep, while the other candidates have again non-zero violations. Intuitively, the Goldilox nature of [ta] might make it seem worthwhile, but because OT is strict domination, only the best candidates for a given constraint are considered. For each constraint, there is always a better candidate than [ta], even if this chosen constraint is worse on a constraint lower in the hierarchy. 

This is clear to see if we convert the above VT to a comparative tableau, and assume that our ill-fated friend [ta] is the presumed winner.

<div class="ottab ct" title="Collective harmonic bounding">

| /at/    | Max | Dep |
| ------- | --- | --- |
| ta~∅    | W   | L   |
| ta~tata | L   | W   |

</div>

If [ta] is the assumed winner, then the [ERC](erc.md) in the first row says that Max must dominate Dep. However, the ERC in the second row states that Dep must dominate Max. This is a direct contradiction. Because a grammar is an ERC set where every ERC is satisfied (made true by the ranking), it is impossible for [ta] to ever be the winner. Even though its individual violation marks don't make this obvious, its comparisons with other candidates show its status as a perpetual loser. 

For more details, see {{#cite Prince2002}}.