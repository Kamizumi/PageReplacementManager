import LRU
import FIFO
import OPTIMAL
import util



'''
We'll run all tests here to keep it neat
'''

'''
For Part 2 testing
We'll use one reference string to make sure the testing stays consistent
Compares expected values with values obtained from the algorithm
'''
def test():
    expected =[
        {"FIFO" : 15, "LRU" : 18, "OPT" : 13},
        {"FIFO" : 15, "LRU" : 16, "OPT" : 11},
        {"FIFO" : 13, "LRU" : 12, "OPT" : 9},
        {"FIFO" : 12, "LRU" : 11, "OPT" : 8}
        ]

    testRefNum = "710325431373111355144705563603"
    tests = [3,4,5,6]

    for i in range(len(tests)):

        results = {
            "FIFO" : FIFO.FIFO(testRefNum, tests[i]),
            "LRU" : LRU.LRU(testRefNum, tests[i]),
            "OPT" : OPTIMAL.OPTIMAL(testRefNum, tests[i])
        }
        print(f"Results for {tests[i]} frame sizes")

        for algorithm, val in results.items():
            matching = "√" if val == expected[i][algorithm] else f"Failed, expected {expected[i][algorithm]}"
            print(f"{algorithm :4} : {val} | Expected : {expected[i][algorithm]} | {matching}")
        print("-----------------------------------------")

'''
Part 3
Randomized testing for all 50 reference strings with 3-6 page frames
'''


def main():
    all_ref_strings = util.read_test_data("testData.txt")
    frameSizes = [3,4,5,6]
    trials = 50

    for size in frameSizes:
        sum = {"FIFO" : 0, "LRU" : 0, "OPT" : 0}

        print(f"\n--- Running 50 Trials for Size: {size} ---")

        

