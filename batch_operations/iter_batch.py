from itertools import islice
import time

def batched(iterable, batch_lenght):
    "Batch data into tuples of length n. The last batch may be shorter."
    # batched('ABCDEFG', 3) --> ABC DEF G
    if batch_lenght < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while (batch := tuple(islice(it, batch_lenght))):
        yield batch

def test_1():
    # print("working on it")
    # start_time = time.time()
    def myIter():
        for x in range(1, 10000, 2):
            yield x
    for x in batched(myIter(), 10):
        # print(x)
        pass
    # print("--- %s seconds ---" % (time.time() - start_time))
    # print("*"*20)
