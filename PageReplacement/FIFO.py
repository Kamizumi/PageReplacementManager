
def FIFO(referenceString, frameSize):
    frames = [None] * frameSize
    queue = []
    pageFaults = 0

    for page in referenceString:
        if page in frames:
            print(f"Hit: {page} \n")
            print(f"{frames}  \n")
        else:
            print(f"Fault : {page}\n")
            pageFaults += 1

            if None in frames:
                queue.append(page)
                frames[frames.index(None)] = page
            else:
                oldestPage = queue.pop(0)
                target = frames.index(oldestPage)
                frames[target] = page
                queue.append(page)

            print(f"{frames}  \n")
    return pageFaults



fart = FIFO("710325431373111355144705563603", 6)
print(fart)