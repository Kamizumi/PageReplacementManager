from collections import deque

def LRU(referenceString, frameSize):
    frames = [None] * frameSize
    order = deque()
    pageFaults = 0

    for page in referenceString:
        if page in frames:
            print(f"Hit: {page}\n")
            print(f"{frames}\n")
            
            #Removes current position and then appends to end of deque
            #Essentially moves page from oldest to most recently used
            order.remove(page)
            order.append(page)
        else:
            print(f"Fault: {page}\n")
            pageFaults += 1

            if None in frames:
                index = frames.index(None)
                frames[index] = page
            else:
                lruPage = order.popleft()
                newIndex = frames.index(lruPage)
                frames[newIndex] = page
            
            order.append(page)
            print(f"{frames} \n")
    return pageFaults

fart = LRU("710325431373111355144705563603", 6)
print(fart)