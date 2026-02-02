class Solution:
    def canWinNim(self, n: int) -> bool:
        # if the number is a multiple of 4 I will not get a chance to finish the game
        # if the number is not a multiple of 4 I will take the remaining amount of stones from the nearest number to the multiple of 4 and then I will win 
        # or the one who started when the number of remaining stones are a multiple of 4 will lose
        if n % 4 == 0:
            return False
        else:
            return True
        