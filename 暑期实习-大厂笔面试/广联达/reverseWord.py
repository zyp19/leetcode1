# def reverseWord(s):
#     s = list(s)
#     i = 0
#     j = len(s)-1
#     while i < j:
#         if s[i]==s[j]:
#             continue
#         s[i] ,s[j] = s[j],s[i]
#         i += 1
#         j -= 1
#     return str(s)
# result = reverseWord("hello xiao mi")
# print(result)

def reverseWord(s):
    s =  s.split(" ")
    s = s[::-1]
    print(" ".join(s))
while True:
    s = input()
    reverseWord(s)
    print(s)

