def wrap(string,w):
	if 0<=len(string)<=1000 and 0<w<len(string):
		wrapper=textwrap.TextWrapper(width=w)
		str=wrapper.fill(text=string)
		return str