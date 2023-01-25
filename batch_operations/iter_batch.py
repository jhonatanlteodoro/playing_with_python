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

def test_2():
    # start_time = time.time()
    to_batch = (x for x in range(1, 10000, 2))
    for x in batched(to_batch, 10):
        # print(x)
        pass
    # print("--- %s seconds ---" % (time.time() - start_time))


def test_3():
    to_batch = [x for x in range(1, 10000, 2)]
    batch = []
    lenght = len(to_batch)
    times = lenght / 10
    counter = 0
    idx = 0
    while counter < times:
        batch.append(to_batch[idx: idx+10])
        counter += 1
        idx += 10
    for b in batch:
        # print(b)
        pass


if __name__ == '__main__':
    import timeit
    # print(timeit.timeit("test()", setup="from __main__ import test"))

    # For Python>=3.5 one can also write:
    print(timeit.timeit("test_1()", number=1000, globals=locals()))

    print(timeit.timeit("test_2()", number=1000, globals=locals()))
    
    print(timeit.timeit("test_3()", number=1000, globals=locals()))

