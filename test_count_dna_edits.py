def capital_case(x):
    return x.capitalize()

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'
	
def Sequence_deletion(data):
    count = 0
    for nt in range(len(data[1])):
        if (data[1][nt] == data[2][count]):
            count +=1
        else:
            continue
    if(count == len(data[2])):
        return 1
    else:
        return 0

def Sequence_insertion(data):
    count = 0
    for nt in range(len(data[2])):
        if (data[2][nt] == data[1][count]):
            count +=1
        else:
            continue
    if(count == len(data[1])):
        return 1
    else:
        return 0

def Sequence_mutation(data):
    if(data[1] == data[2]):
        return 0
    else:
        return 1

def count_dna_edits():
    with open("orig_seq.csv") as infile:
        next(infile) # to skip the header line
        count_insertion = count_deletion = count_mutation = count_unexpected_or_no_change = 0
        for line in infile:
            data = line.split()
    
            if((len(data[1]) > len(data[2])) and (Sequence_deletion(data))):
                count_deletion +=1
    
            elif((len(data[1]) < len(data[2])) and (Sequence_insertion(data))):
                count_insertion +=1
    
            elif((len(data[1]) == len(data[2])) and (Sequence_mutation(data))):
                count_mutation +=1
            else:
                count_unexpected_or_no_change +=1
        print("count_insertion " + str(count_insertion) + " count_deletion " + str(count_deletion) + " count_mutation " + str(count_mutation) + " count_unexpected_or_no_change " + str(count_unexpected_or_no_change) )
        return (count_insertion,count_deletion,count_mutation)
    
    
def test_capital_case():
    assert count_dna_edits() == (1, 2, 2)
