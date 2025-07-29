# def find_max_occurred_alphabet(string):
#   alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
#                     "m", "n", "o", "p", "q", "r", "s",
#                     "t", "u", "v", "x", "y", "z"]
#   max_occurrence = 0
#   max_alphabet = alphabet_array[0]
#
#   for alphabet in alphabet_array:
#     occurrence = 0
#
#     for char in string:
#       if char == alphabet:
#         occurrence += 1
#
#     if occurrence > max_occurrence:
#       max_alphabet = alphabet
#       max_occurrence = occurrence
#
#   return max_alphabet


def find_alphabet_occurrence_array(string):
  alphabet_occurrence_array = [0] * 26

  for char in string:
    if not char.isalpha():
      continue
    arr_index = ord(char) - ord('a')
    alphabet_occurrence_array[arr_index] += 1

  max_occurrence = 0
  max_index = 0

  for index in range(len(alphabet_occurrence_array)):
    alphabet_occurrence = alphabet_occurrence_array[index]

    if alphabet_occurrence > max_occurrence:
      max_occurrence = alphabet_occurrence
      max_index = index

  return chr(max_index + ord('a'))


result = find_alphabet_occurrence_array
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))

# alphabet_occurrence_array = [0] * 26
#
# for char in string:
#   if not char.isalpha():
#     continue
#   arr_index = ord(char) - ord('a')
#   alphabet_occurrence_array[arr_index] += 1
#
# return alphabet_occurrence_array
