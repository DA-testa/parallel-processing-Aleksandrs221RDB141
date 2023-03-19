# python3

def parallel_processing(n, m, data):
    output = []
    time = [0]*n #to save time
    # TODO: write the function for simulating parallel tasks, 
    for job in range(m):
        minthread = 0 #minimal required thread
        mintime=time[0] #minimal required time
        for thread in range(1,n):
            if mintime>time[thread]: 
                minthread = thread 
                mintime = time[thread]        
        time[minthread]=(time[minthread]+data[job])
        # create the output pairs
        output.append((minthread,mintime))
    return output
def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n, m = map(int,input().split())
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int,input().split()))
    # TODO: create the function
    result = parallel_processing(n,m,data)
    for thread,process in result:
        print(thread,process)
    # TODO: print out the results, each pair in it's own line
if __name__ == "__main__":
    main()