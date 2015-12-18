#
# Day 10
# Input: A sequence of digits to spell out
#

def look_and_say ( cycles, input ):

    # For each cycle, use the previous cycle's output as input
    for i in xrange(0, cycles):
    
        # Start with one of the first digit and compare thereafter
        prev_digit = input[0]
        count = 1
        output = ""
    
        for digit in input[1:]:
    
            # Add to current repeated digit's count
            if digit == prev_digit:
                count += 1
                
            # Add the previous digit's count to the output and move on to the next digit
            else:
                output += (str(count) + prev_digit)
            
                prev_digit = digit
                count = 1
            
        # Add the final digit's count to the output  
        output += (str(count) + prev_digit)  
            
        input = output
        
    return len(output)
          
if __name__ == "__main__":

    input = "1321131112"
    
    #
    # Part 1
    #
    print look_and_say ( 40, input )
    
    #
    # Part 2
    #
    print look_and_say ( 50, input )
    