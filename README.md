StackOverflow console client.

# Usage

Fetch new questions:

```
> f
fetching data...

1: c (30 / 770)
2: python (40 / 1371)
3: bash (3 / 310)
4: git (1 / 243)
5: go (0 / 660)
```

Show list of questions for tag:

```
> s 1

1: [new] Is there a way to combine two variables in c++?
  ['c++', 'variables', 'combinations', 'receipt'], 4 min ago, score 0, answer_count 0

2: [new] 8-way recursive flood fill problem with a twist
  ['c++', 'c', 'flood-fill'], 6 min ago, score 0, answer_count 0

3: [new] How to read in values from specific columns in a CSV file to perform calculations - C++
  ['c++', 'csv', 'class', 'col'], 6 min ago, score 0, answer_count 0

4: [new] __uuidof (MMDeviceEnumerator) undeclared identifier
  ['c++', 'com', 'vs-2019'], 9 min ago, score 0, answer_count 0

5: [new] Dynamic vs static array
  ['c++', 'pointers', 'memory', 'dynamic'], 14 min ago, score 0, answer_count 0

6: [new] What is the most efficient way to scan all files in all drives in C++?
  ['c++', 'file', 'drive', 'scanning'], 15 min ago, score 0, answer_count 0

7: [new] What is the most efficient way to scan all files in all drives in C++?
  ['c++', 'file', 'drive', 'scanning'], 15 min ago, score -1, answer_count 0
```

Open questions:

```
> o 1, 4, 5
```

Mark questions on the buffer as readed:

```
> del
delete by c (remain=765)
```