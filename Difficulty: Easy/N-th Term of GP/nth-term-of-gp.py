class Solution:
	def nthTerm(self, a, r, n):
	    MOD= 10**9 + 7
	    return (a * pow(r,n-1,MOD)) % MOD