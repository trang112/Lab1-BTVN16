"""Đây là một hàm đếm số lần xuât hiện của một substring trong một chuỗi string"""

def count_substring(string, sub_string):
    count = 0 
    for i in range(0,len(string)):
        temp = string[i:i+len(sub_string)]
        if temp == sub_string:
            count += 1
    return count

if __name__ == "__main__":
    count = count_substring("ABCDCDC","CDC")
    print(count)