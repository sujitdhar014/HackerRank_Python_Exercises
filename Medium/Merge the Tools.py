def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        substring=string[i:i+k]

        seen=set()
        result=''
        for char in substring:
            if char not in seen:
                seen.add(char)
                result+=char
        print(result)



s = "AABCAAADA"
k = 3
merge_the_tools(s,k)