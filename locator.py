def SearchingChallenge(strParam):

  # code goes here
    import collections
    txt = strParam
    txtlist = txt.split()                       # split the whole string into words inside a list
    repeated = []                               # the main list with the repeated characters for each word in separate dictionary
    large_num = []                              # to contain the largest repeated character numbers
    for y in txtlist:
        frequencies = collections.Counter(y)
        insiderepeated = {}
        for key, value in frequencies.items():
            if value > 1:
                insiderepeated[key] = value
    # updating the main diction list         
        repeated.append(insiderepeated)
    
    for a_dictionary in repeated :
        if not a_dictionary:      # check if the word did not contain any repeated characters
            large_num.append(0)
        else :
            all_values = a_dictionary.values()
            max_value = max(all_values)
            large_num.append(max_value)
    
    max_num = max(large_num)
    max_index = large_num.index(max_num)
    if max_num == 0:
          return -1
    else:
          result = txtlist[max_index]
          return result

# keep this function call here 
# print(SearchingChallenge(input()))