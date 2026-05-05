import matplotlib.pyplot as plt

frameSizes = [3,4,5,6]

FIFO_avg = [19.14, 16.66, 13.56, 11.10]
LRU_avg = [19.36, 16.36, 13.44, 11.10]
OPTIMAL_avg = [14.34, 11.52, 9.76, 8.66]

#FIFO graph
plt.figure()
plt.plot(frameSizes, FIFO_avg, marker = 'o')
plt.title("FIFO: Average # Of Page Faults vs Frame Sizes")
plt.xlabel("Frame Size")
plt.ylabel("Average Page Faults")
plt.grid(True)
plt.show()

#LRU graph
plt.figure()
plt.plot(frameSizes, LRU_avg, marker = 'o')
plt.title("LRU: Average # Of Page Faults vs Frame Sizes")
plt.xlabel("Frame Size")
plt.ylabel("Average Page Faults")
plt.grid(True)
plt.show()

#OPTIMAL graph
plt.figure()
plt.plot(frameSizes, OPTIMAL_avg, marker = 'o')
plt.title("OPT: Average # Of Page Faults vs Frame Sizes")
plt.xlabel("Frame Size")
plt.ylabel("Average Page Faults")
plt.grid(True)
plt.show()

#ALL GRAPHS
plt.figure()
plt.plot(frameSizes, OPTIMAL_avg, marker = 'o', label = "OPTIMAL")
plt.plot(frameSizes, LRU_avg, marker = 'o', label = "LRU")
plt.plot(frameSizes, FIFO_avg, marker = 'o', label = "FIFO")
plt.title("Average # Of Page Faults vs Frame Sizes")
plt.xlabel("Frame Size")
plt.ylabel("Average Page Faults")
plt.legend()
plt.grid(True)
plt.show()

