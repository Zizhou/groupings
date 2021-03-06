import itertools, random

#totally uneedeed? 
class Person(object):
    def __init__(self, id_num):
        self.worked_with = []
        self.worked_with.append(id_num)
        self.id_num = id_num

    def __unicode__(self):
        return "ID:" + str(self.id_num)

    def get_work(self):
        return map(unicode, self.worked_with)

    #pass list of id numbers, check if in worked with
    def check_prior(self, partners):
        no_prior = True
        for person in partners:
            if person in self.worked_with:
                if person != self.id_num:
                    no_prior = False
                else:
                    print "self"
            else:
                self.worked_with.append(person)
#            print unicode(self) + " has no history with " + unicode(person) + ":" + str(no_prior)
        return no_prior

    def prior(self, person):
        if person in self.worked_with:
            #print unicode(person)
            #print self.get_work()
            return False
        else:
            self.worked_with.append(person)
            return True

#pair joining method            
def make_groups(total_size, group_size):
    class_total = [0]*total_size
    for x in range(0, total_size):
        #class_total[x] = Person(x)
        class_total[x] = x
        
    possible_pairs = []
    possible_groups = []

    #all possible combinations of nC2, from which we will construct groups
    for subset in itertools.combinations(class_total, 2):
        possible_pairs.append(subset)
    while possible_pairs != []:
        print possible_pairs
        print possible_groups
        current_group = []
        for pair in possible_pairs:
            if pair[0] not in set(itertools.chain(*possible_groups)):
                current_group = [pair[0]]
                break
        if current_group == []:
            current_group = [possible_pairs[0][0]]
        for x in range(0, group_size - 1):
            next_pair = []
            for entry in possible_pairs:
                #print entry
                #print current_group[-1]
                if entry[0] == current_group[-1]:
                    next_pair.append(entry)
            #[next_pair for entry in possible_pairs if entry[1] == current_group[-1]]

            if next_pair != []:
                current_group.append(next_pair[0][1])
                print next_pair[0][1]
        for pair in itertools.combinations(current_group, 2):
            if pair in possible_pairs:
                possible_pairs.remove(pair)
        possible_groups.append(current_group)
    return possible_groups

#pruning method
def imake_groups(total_size, group_size):
    class_total = [0]*total_size
    for x in range(0, total_size):
        #class_total[x] = Person(x)
        class_total[x] = x
        
    possible_groups = []
    possible_pairs = []
    #all possible combinations of n choose [group_size]    
    for subset in itertools.combinations(class_total, group_size):
        possible_groups.append(subset)
    #all possible pairs
    for subset in itertools.combinations(class_total, 2):
        possible_pairs.append(subset)
    #eliminate groups with repeat pairs
    no_repeats = eliminate_repeats(possible_groups, possible_pairs)

    return no_repeats 

##list of groups in, list of groups out
#needs work
def ieliminate_repeats(groups):
    pairings = []
    delete = []
    #shuffle for random groupings(will need for roulette method)
    random.shuffle(groups)
    for circle in groups:
        valid = True
        these_pair = []
        for pair in itertools.combinations(circle, 2):
            if pair not in pairings:
                these_pair.append(pair)
                #print "yes"+unicode(pair[0]) + unicode(pair[1])
            else:
               #print unicode(pair[0]) + unicode(pair[1])
                valid = False
        if not valid:
            delete.append(circle)
           #print "deleting:" + unicode(circle[0])+ unicode(circle[1])+ unicode(circle[2])
        else:
            for pair in these_pair:
                pairings.append(pair)
            #print "accept:" + unicode(circle[0])+ unicode(circle[1])+ unicode(circle[2])
    #print "delete"
    #print "deleting"
    #print groups
    #print delete
    eliminated = list(set(groups).difference(delete))
 #   for circle in groups:
 #       print "judging:" + str(circle)
 #       if circle in delete:
 #           print map(unicode, circle)
 #           groups.remove(circle)
    #print eliminated
    return eliminated

#pass through
def ipick_groups(groups):
    return groups


def pick_groups(group_list):
    group_list.sort()
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
    
def pretty_print_groupings(groupings):
    groupings.sort(key = len, reverse = True)
    for rounds in groupings:
        if True: #len(rounds) >= len(groupings[0]):
            for x in rounds:
                print "["
                for y in x:
                    print y
                   
                print "]"
            print "~~~~~~~~~~~~~~~~~~~"
def main():
    class_size = input("Class size:")
    group_size = input("Group size:")
    pretty_print_groupings(pick_groups(make_groups(class_size, group_size)))
    
