# Recursive Constraint Demotion

Recursive Constraint Demotion (RCD) is an algorithm that determines whether a given [ERC](erc.md) set is consistent. A consistent ERC set means that at least one possible [ranking](rankings.md) of the given constraints exists. If there are any incompatible ERCs that would result in a ranking contradiction, RCD will find them. 

This section will show a brief demonstration of RCD; however, the best reference is *RCD: The Movie*, available as {{#cite Prince2009}}.