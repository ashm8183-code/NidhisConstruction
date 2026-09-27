# NidhisConstruction

Python solution for the Nidhi's Construction problem.

## Problem

Nidhi builds a structure using numbered cubes. Each new cube is placed next to an existing cube in one of four directions:

- Top
- Down
- Left
- Right

The task is to determine the four neighboring cubes of a given cube.

## Approach

The solution represents each cube using its `(row, column)` position on a 2D grid.

The commands are first sorted by existing cube number and then by new cube number.

Two dictionaries are used:

- `position` stores the position of each cube.
- `board` stores the cube present at each position.

If a cube is placed where another cube already exists, the old cube is replaced.

## Language

Python 3
