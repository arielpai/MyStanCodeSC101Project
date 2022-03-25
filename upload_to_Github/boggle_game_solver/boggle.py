"""
File: boggle.py
Name: Ariel Pai
----------------------------------------
TODO: Boggle! Let users insert four random letters for four times,
      and assemble those letters to become meaningful words according
      to the rules of Boggles. Note: the length of the words must be
      four or more than four letter long.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO: Boggle!
	"""
	start = time.time()
	####################
	s_l = []
	i = 0
	while i < 4:
		s = input(str(i+1)+' row of letters: ')
		if s[1] == ' ' and s[3] == ' ' and s[5] == ' ':
			s = s[0]+s[2]+s[4]+s[6]
			s_l.append(s)
			i += 1
		else:
			print('Illegal input')
	read_dictionary()
	ans_l = []
	boggle(s_l, ans_l)
	print('There are', str(len(ans_l)), 'words in total.')
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def boggle(s_l, ans_l):
	"""
	:param s_l: list, the words inserted by user
	:param ans_l: list, the list of answers found
	:return: list, answer list
	"""
	permutations(s_l, [], ['ABCD', 'EFGH', 'IJKL', 'MNOP'], [], 0, 0, ans_l)


def permutations(s_l, p, index_l, index_p, row, column, ans_l):
	"""
	:param s_l: list, the words inserted by user
	:param p: list, the permutations of the words inserted
	:param index_l: list, index of the words inserted
	:param index_p: list, the permutation of the indexes of the words
	:param row: int, the row of the letter
	:param column: int, the column of the letter
	:param ans_l: list, the list of answers found
	:return: list, answer list
	"""
	dictionary = read_dictionary()
	if len(p) >= 4:
		p_str = ''.join(p)
		if p_str in dictionary:
			if p_str not in ans_l:
				# To eliminate duplicate words
				print('Found "'+p_str+'"')
				ans_l.append(p_str)

	# Early stop (if the prefix does not exist in the dictionary, do not proceed with the loop)
	if has_prefix(''.join(p)):
		for i in range(len(s_l)):
			for j in range(len(s_l[i])):
				if index_l[i][j] in index_p:
					pass
				else:
					""""
					If there is no letter in the list, append the letter s_l[i][j] to p, 
					and  index_l[i][j] to index_p
					"""
					if len(index_p) == 0:
						index_p.append(index_l[i][j])
						p.append(s_l[i][j])
						row = i
						column = j
						# Explore
						permutations(s_l, p, index_l, index_p, row, column, ans_l)
						# Un-choose
						index_p.pop()
						p.pop()
						# To figure out the row and column of the last letter in p and index_p
						if len(index_p) != 0:
							for a in range(len(index_l)):
								for b in range(len(index_l)):
									if index_l[a][b] == index_p[len(index_p) - 1]:
										row = a
										column = b

					elif row - 1 <= i <= row + 1 and column - 1 <= j <= column + 1:
						# Choose
						index_p.append(index_l[i][j])
						p.append(s_l[i][j])
						row = i
						column = j
						# Explore
						permutations(s_l, p, index_l, index_p, row, column, ans_l)
						# Un-choose
						index_p.pop()
						p.pop()
						# To figure out the row and column of the last letter in p and index_p
						if len(index_p) != 0:
							for a in range(len(index_l)):
								for b in range(len(index_l)):
									if index_l[a][b] == index_p[len(index_p)-1]:
										row = a
										column = b


def read_dictionary():
	dictionary = []
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE) as f:
		for line in f:
			dictionary.append(line.strip())
	return dictionary


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	dictionary = read_dictionary()
	for i in dictionary:
		if i.startswith(sub_s) is True:
			return True


if __name__ == '__main__':
	main()
