"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[42, 42, 42, 42, 42, 42, 42], 3],
            "answer": [42, 42, 42],
        },
        {
            "input": [[42, 42, 42, 99, 99, 17], 0],
            "answer": [],
        },
        {
            "input": [[1, 1, 1, 2, 2, 2], 5],
            "answer": [1, 1, 1, 2, 2, 2],
        },
    ],
    "Extra": [
        {
            "input": [['tom', 42, 'bob', 'bob', 99,
'bob', 'tom', 'tom', 99], 2],
            "answer": ['tom', 42, 'bob', 'bob', 99,
'tom', 99],
        },
        {
            "input": [[1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3,
4, 5, 4, 3, 2, 1], 1],
            "answer": [1, 2, 3, 4, 5],
        },
        {
            "input": [[1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3,
4, 5, 4, 3, 2, 1, 2, 3, 4, 5], 3],
            "answer": [1, 2, 3, 4, 5, 4, 3, 2, 1, 2,
3, 4, 5, 1, 5],
        },
        {
            "input": [[1], 5],
            "answer": [1],
        },
    ]
}
