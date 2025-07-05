def runForever(n):
    if n > 0:
        runForever(n)
    else:
        runForever(n - 1)

runForever(1)