#
# Day 4
# Input: The start of an MD5 input string
#

from hashlib import md5

def is_hash_start_found ( md5_key, md5_number, starts_needle ):
    
    # Hash the input string appended with a number
    hash = md5( md5_key + str(md5_number) ).hexdigest()
    
    # Look for the needle at the start of the hash
    if hash.startswith(starts_needle):
    
        print "Hash starting with {} found:\n\t md5({} + {}) = {}".format(starts_needle, md5_key, md5_number, hash)
        return md5_number
          
    return 0
    

if __name__ == "__main__":

    input = "yzbqklnj"
    
    #
    # Part 1
    #

    # Find the first positive non-zero integer that returns a hash starting with 5 zeros
    for i in xrange(1, 10**6):
    	if is_hash_start_found ( input, i, "0" * 5 ):
    	    break
    
    #
    # Part 2
    #    

    # Find the first positive non-zero integer that returns a hash starting with 6 zeros
    for i in xrange(1, 10**7):
    	if is_hash_start_found ( input, i, "0" * 6 ):
    	    break
