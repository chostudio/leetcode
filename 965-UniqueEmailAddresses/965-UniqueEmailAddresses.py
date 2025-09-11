# Last updated: 9/11/2025, 12:31:25 PM
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # this was play station round 1. 
        # first are we guarenteed that there's only one @ symbol? will mkae it wasier to parse? Yes.
        # all domains will end with .com and not guaraenteed to have something before it AND not gauraenteed to only have one or none + or . so watch out for them
        s = set()
        for email in emails:
            first, second = email.split('@')
            # all the invalid ones continue to next email, if get through entire thing, cout += 1
            # everything after the first plus sign will be ignored
            name = first.replace(".", "") # replace dots with nothing. replace RETURNS something you have to assign it to a var
            name = name.split("+")[0] # even if multiple, then only take first part
            
            
            # in constraints it is weidly worded but it is guarenteed that domain is valid i guess. "Domain names must contain at least one character before ".com" suffix." otherwise we would have a check that checks if there's something before the .com
            s.add(name + "@" + second)
        return len(s) # a set bc there could be duplicates of the valid emails. aka point to same final email