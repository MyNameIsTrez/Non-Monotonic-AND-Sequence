# Non-Monotonic-AND-Sequence

`i & 0` -> `0…`

`i & 1` -> `01…`

`i & 2` -> `0022…`

`i & 3` -> `0123…`

`i & 4` -> `00004444…`

`i & 5` -> `01014545…`

`i & 6` -> `00224466…`

`i & 7` -> `01234567…`

`i & 8` -> `00000000888888880…`

`i & 5` creates the most random looking sequence here with its `01014545`

Although a sequence could still look random while only increasing (`0189`) or decreasing, `i & 5` its sequence looks more random due to it being the only non-monotonic one:

> […] is called monotonic if and only if it is either entirely non-increasing, or entirely non-decreasing. That is, […] a function that increases monotonically does not exclusively have to increase, it simply must not decrease.

In other words, a non-monotonic function goes up and down/down and up (before the sequence repeats itself). `011` is monotonic, `010` is non-monotonic.

I wanted to know whether more/less monotonic functions would appear if the value to the right of the `&` would get larger.

The conclusion is that if you run main.py, the first ***non-monotonic*** value to the right of the `&` is `5`, and that every value *larger than* `8` is also ***non-monotonic***. In other words, `0/1/2/3/4/6/7/8` are the only monotonic values!