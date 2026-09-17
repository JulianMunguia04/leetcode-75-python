# 649 Dota2 Senate, Queue, Medium

from collections import deque

class Solution:
    def predictPartyVictory(self, senate):
        n = len(senate)
        
        # Queues to store the indices of the senators
        radiant = deque()
        dire = deque()
        
        # Populate initial indices
        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)
                
        # Simulate the round-based voting
        while radiant and dire:
            r_idx = radiant.popleft()
            d_idx = dire.popleft()
            
            # The senator with the smaller index votes first
            if r_idx < d_idx:
                # Radiant bans Dire. Radiant moves to the next round.
                radiant.append(r_idx + n)
            else:
                # Dire bans Radiant. Dire moves to the next round.
                dire.append(d_idx + n)
                
        # Whichever queue still has senators left wins the game
        return "Radiant" if radiant else "Dire"

# Time Complexity O(n)