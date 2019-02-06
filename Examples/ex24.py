def add(*args):
	if len(args)<=1: raise KeyError('Two or more arguments expected')

	nsum = sum([a for a in args if type(a) in (int, float)])
	ssum = ''.join([a for a in args if type(a)==str])

	if ssum != '': return ssum
	else: return nsum
