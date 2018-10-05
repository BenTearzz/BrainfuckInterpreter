>>>+++!
(0' 0' 0' 3)
          ^

[-<+>] Moves cell one to the left
(0' 0' 3' 0)
          ^
< Set our current cell to the place we moved it
(0' 0' 3' 0)
       ^

[-<<+>>] Move our cell two to the left
(3' 0' 0' 0)
       ^

<< Set our current cell to the place we moved it
(3' 0' 0' 0)
 ^

>[  All of it can be written in a one liner like this:
    >>>+++[-<<<+>>>]<<<
]
