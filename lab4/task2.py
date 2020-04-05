class Task:
	def perform(self, subWord, word):
		l = 0
		i=0

		while i < len(word):
			while word[i]==subWord[l]:
				i+=1
				l+=1
				if l >= len(subWord):
					return True
#endWhile
			l=0
			i+=1
		return False



task = Task()
print(task.perform("byla", "kobylamamalybok"))