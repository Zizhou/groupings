import itertools 
def make_groups(total_size, group_size): 
    class_total = [None]*total_size
    for x in range(1, total_size + 1): 
        class_total[x-1] = x 
    possible_groups = [] 
         
    for subset in itertools.combinations(class_total, group_size): 
        id_group = [] 
        for person in subset: 
            id_group.append(person) 
             
        possible_groups.append(id_group) 
 
    return possible_groups 
     
def pick_groups(group_list): 
    groupings = [] 
    while group_list != []: 
        pairings = [] 
        pairings.append(group_list[0]) 
        for group1 in group_list: 
            if list(set(group1) & set(itertools.chain(*pairings))) == []: 
                    pairings.append(group1) 
        groupings.append(pairings) 
        for pair in pairings: 
            if pair in group_list: 
                group_list.remove(pair) 
    return groupings  
