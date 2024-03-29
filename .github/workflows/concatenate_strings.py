import sys

def concatenate_strings(str1, str2):
    """将两个字符串拼接起来"""
    return str1 + str2

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python concatenate_strings.py <string1> <string2>")
    else:
        string1 = sys.argv[1]
        string2 = sys.argv[2]
        result = concatenate_strings(string1, string2)
        print(result)
