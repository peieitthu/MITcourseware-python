def main():
    import sys
    input = sys.stdin.read
    
    # Read the input
    data = input().split()
    
    # Initialize the index for traversing the input data
    index = 0
    
    # Read number of test cases
    N = int(data[index])
    index += 1
    
    # Initialize a list to store results
    results = []
    
    # Process each test case
    for _ in range(N):
        # Read the number of integers in the current test case
        X = int(data[index])
        index += 1
        
        # Read the integers and process the sum of squares of non-negative numbers
        sum_of_squares = sum(int(data[index + i]) ** 2 for i in range(X) if int(data[index + i]) >= 0)
        index += X
        
        # Append the result for the current test case
        results.append(sum_of_squares)
    
    # Print all results, each on a new line with no blank lines in between
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()
