#
# Day 11
# Input: Previous password
#

def next_password ( cycles, password ):
    
    for cycles in xrange(0, cycles):
    
        # Check password validity
        conseq_triple = False
        doubles = 0

        while not conseq_triple or doubles <= 1:

            password = list(password)
            conseq_triple = False
            doubles = 0

            # Increment by 1
            for i in xrange( -1, -len(password), -1 ):
                if password[i] == "z":
                    password[i] = "a"
                else:
                    password[i] = chr(ord(password[i]) + 1)
                    break
        
            password = "".join(password)
            print password
    
            if any(char in password for char in ['i', 'o', 'l']):
                continue
    
            # Check for triple
            for i in xrange( 0, len(password) - 2 ):
                if ord(password[i]) + 1 == ord(password[i+1]) and ord(password[i+1]) + 1 == ord(password[i+2]):
                    conseq_triple = True
                    break
            
            # Check for double
            i = 0
            while i < len(password)-1:
                if password[i] == password[i+1]:
                    doubles += 1
                    i += 1
                i += 1
        
    return password
    
    
if __name__ == "__main__":

    input = "hepxcrrq"
    
    #
    # Part 1
    #
    
    # Get next month's password
    print next_password ( 1, input )
    
    #
    # Part 2
    #
    
    # Get the month-after-next's password
    print next_password ( 2, input )