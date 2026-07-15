### Algorithm

1. Initialize an empty dictionary `seen` mapping value → index
2. Iterate `i`, `num` over `nums`.
  Compute `complement` = `target` - `num`
  If `complement` in `seen`, return [seen[complement], i]
  Otherwise store `seen[num] = i`

  Complexity
Time: 
𝑂
(
𝑛
)
 — one pass through the list.

Space: 
𝑂
(
𝑛
)
 — worst case we store every element in the dictionary.
