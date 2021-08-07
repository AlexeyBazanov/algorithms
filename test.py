import line_profiler
profile = line_profiler.LineProfiler()


@profile
def test():
    a = [0,1,2]
    a[1] = 10
    return 10 * 10


test()