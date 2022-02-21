# Non-Monotonic-AND-Sequence

`i & 0` -> `00`

`i & 1` -> `0101`

`i & 2` -> `00220022`

`i & 3` -> `01230123`

`i & 4` -> `0000444400004444`

`i & 5` -> `0101454501014545`

`i & 6` -> `0022446600224466`

`i & 7` -> `0123456701234567`

`i & 8` -> `00000000888888880...`

`i & 5` creates the most random looking sequence here with its `0, 1, 0, 1, 4, 5, 4, 5`

Although a sequence could still look random while only increasing (`0, 5, 100, 103`) or decreasing, `i & 5` its sequence looks more random due to being the only non-monotonic one:

> […] is called monotonic if and only if it is either entirely non-increasing, or entirely non-decreasing. That is, […] a function that increases monotonically does not exclusively have to increase, it simply must not decrease.

In other words, a non-monotonic function goes up and down/down and up (before the sequence repeats itself). `011` is monotonic, `010` is non-monotonic.
