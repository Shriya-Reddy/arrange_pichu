# arrange_pichu
Here the goal is to arrange k pichu’s in a map, so that no two pichu’s are in the same row, column and diagonal with no X or @ between them. The initial state is the given map. The successor function adds ‘p’ in the map. My approach is to get one map from successor function, then check if it is goal, if no then check if it is acceptable function.
## Acceptable function :
                Takes one map from successor function and check performs row, column and diagonal check. If all are true, it means then it is acceptable and appends it to fringe. 
### Row check: 
      Checks if p’s placed in each row are in acceptable position.
### Column check:
      Checks if p’s placed in each column are in acceptable position.
### Diagonal check: 
      Checks if p’s placed in diagonal are in acceptable position.
The cost function here can be described as binomial that just gives 0(False) if it is not acceptable and 1(True) if it is acceptable.
## Approach:
1. Add house map to fringe
2. Check if it is goal, then return it
3. Else, get successor function of house map. For each successor function, check if it is acceptable
4. If it is acceptable, then append it fringe
5. Then repeat the steps again until goal is reached
