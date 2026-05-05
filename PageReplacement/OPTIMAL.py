
def OPTIMAL(referenceString, frameSize):
    frames = [None] * frameSize
    pageFaults = 0


    for currStep, page in enumerate(referenceString):
        if page in frames:
            #print(f"Hit: {page}\n")
            #print(f"{frames}\n")
            pass

        else:
            #print(f"Fault: {page}\n")
            #print(f"{frames}\n")
            pageFaults += 1
            

            if None in frames:
                index = frames.index(None)
                frames[index] = page
            else:
                pageToReplace = None
                distance = -1

                for candidatePage in frames:
                    futureString = referenceString[currStep + 1:]

                    if candidatePage not in futureString:
                        pageToReplace = candidatePage
                        break

                    else:
                        nextUse = futureString.index(candidatePage)
                        if nextUse > distance:
                            distance = nextUse
                            pageToReplace = candidatePage
                target = frames.index(pageToReplace)
                frames[target] = page

    return pageFaults


#fart = OPTIMAL("710325431373111355144705563603", 6)
#print(fart)