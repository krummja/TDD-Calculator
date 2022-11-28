# Test Driven Development (TDD) Example Application

1. What is TDD?
2. What is SOLID?
3. Example Application
   1. Boilerplate Code
   2. Writing Tests
   3. Satisfying Tests
4. Github Actions
5. Coverage Testing

## What are we making?

We'll implement a very simple program that can take in a string that represents
a list of numbers and returns their sum.

```console
>>> Calculator.add("1,2,3")
6

>>> Calculator.add("10,2")
12
```

In developing this app, we'll start with the simplest case and gradually expand
its scope using TDD.

1. Add 0, 1, or 2 arguments. Empty strings return 0.
2. Allow adding *n* arguments.
3. Handle newlines in the input string.
4. Support different delimiters.
5. The first line is optional. All existing scenarios should still be valid.
6. Calling the function to add with a negative number should throw an exception
7. Numbers greater than 1000 should be ignored.
8. Delimiters can be any length with the format: `//[delimiter]\n`
   e.g. `//[---]\n1---2---3` should return 6.
9. Allow multiple delimiters.
10. Make sure multiple delimiters can be of any length.
