# Last updated: 9/12/2026, 8:37:10 PM
1class Solution:
2    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
3        
4        # what do we need to do in order to pre set up the dfs?
5        # adj lsit makes it easier for us
6        adj = collections.defaultdict(list)
7        state = defaultdict(str)
8
9
10        supplies = set(supplies) # O(1) check now
11
12        for i in range(len(recipes)):
13            state[recipes[i]] = "unvisited"
14            supplies.add(recipes[i]) # for now, assume we at leasat have the reciept in supplies
15            for food in ingredients[i]:
16                state[food] = "unvisited"
17                adj[recipes[i]].append(food)
18
19
20        def dfs(food):
21            if food not in supplies:
22                return False
23            if state[food] == "visiting":
24                state[food] = "impossible"
25                return False # impossible depdendecy A <-> B
26            if state[food] == "impossible":
27                return False
28            if state[food] == "doable":
29                return True # alr checked on prev run
30            
31
32            # else, unvisited
33            state[food] = "visiting"
34
35            result = True
36            for ingredient in adj[food]:
37                result = result and dfs(ingredient)
38                
39            # if we bubble up false, then we need to mark up the chain that it's impossible to make the higher dependent food also impossible
40            if result == False:
41                state[food] = "impossible"
42                return False
43            state[food] = "doable"
44            return True # if we go through all the depdendcies and all there (still True)
45        
46        ans = []
47        for recipe in recipes:
48            result = dfs(recipe)
49            if result == True:
50                ans.append(recipe)
51        
52        return ans