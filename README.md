# ff-python
A Python implementation of the Flippy Flop data structure. 

## Background

A Flippy Flop is an unpredictable data structure.
Flip (insertion) and flop (removal) operations succeed at random.

## Usage

As you'll see in the example below, the Flippy Flop is sufficiently unpredictable.

### Python

```python
from flippyflop import FlippyFlop

ff = FlippyFlop()

# Attempt to insert a value
ff.flip(5)

# Could be 5, or None if the flip call failed
flop1 = ff.flop()

# Could be 5 if the flop call didn't remove the value, or None if the flip call failed
flop2 = ff.flop()

# However, it's easy to verify the number of elements in a FlippyFlop
count = ff.count
```

# Libraries 

A Flippy Flop is an unpredictable data structure.
Flip (insertion) and flop (removal) operations succeed at random.

Find libraries [libraries.io](https://libraries.io/github).


# Contact

You can most easily reach me on twitter [@_Shakeel](http://twitter.com/_Shakeel).

# License

This project is licensed under the terms of [the MIT license](LICENSE).
