"""
Consider a string consisting of lowercase English alphabetic letters (i.e., [a-z]) only. We use the following rules to encode all of its characters into string s:
· a is encoded as 1, b is encoded as 2, c is encoded as 3, ..., and i is encoded as 9.
· j is encoded as 10#, k is encoded as 11#, i is encoded as 12#, ..., and z is encoded as 26#.
· If there are two or more consecutive occurrences of any character, then the character count is written within parentheses (i.e., (c) , where c is an integer denoting the count of consecutive occurrences being encoded) immediately following the character. For example, consider the following string encodings:
o String "abzx" is encoded as s = "1226#24#".
o String "aabccc" is encoded as s = "1(2)23(3)".
o String "bajj" is encoded as s = "2110#(2)".
o String "wwxyzwww" is encoded as s = "23#(2)24#25#26#23#(3)°.
Complete the frequency function in the editor below. It has one parameter: a string, s, that was encoded using the rules above and consists of digits (i.e., decimal integers from 0 to 9), # symbols, and parentheses. It must return an array of 26 integ
· The element at index 0 denotes the frequency of character a in the original string.
· The element at index 1 denotes the frequency of character b in the original string.
· The element at index 2 denotes the frequency of character c in the original string.
· The element at index 25 denotes the frequency of character z in the original string. Input Format
Locked stub code in the editor reads encoded string s from stdin and passes it to the function.
Constraints
· String s consists of decimal integers from 0 to 9, #s, and O's only.
· 1 length of s 105
· It is guaranteed that string s is a valid encoded string.
· 2 c 104, where c is a parenthetical count of consecutive occurrences of an encoded character.
Output Format
The function must return an array of 26 integers denoting the respective frequencies of each character (i.e., a through z) in the decoded string. This is printed to stdout by locked stub code in the editor.
Sample Input 0
1226#24#
Sample Output 0
1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1
"""
### SOLUTION: Right to left
def stats(encoded: str) -> list:
    i = len(encoded) - 1
    result = [0] * 27
    while i >= 0:
        token, count = '', 0
        if encoded[i] == ')':
            i -= 1
            while encoded[i] != '(':
                count = count * 10 + int(encoded[i])
                i -= 1
            i -= 1
            if encoded[i] == '#':
                token = int(encoded[i-2:i])
                i -= 3
            else:
                token = int(encoded[i])
                count = 1
                i -= 1

        elif encoded[i] == '#':
            token = int(encoded[i - 2:i])
            count = 1
            i -= 3
        else:
            token = int(encoded[i])
            count = 1
            i -= 1
        result[token] += count
    return result[1:]

print(stats('1226#24#'))
print(stats('1226#24#14#(33)'))