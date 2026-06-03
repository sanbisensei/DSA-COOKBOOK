def longest_common_prefix(strs):
    hum = ""

    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return hum

        hum += strs[0][i]

    return hum


print(longest_common_prefix(["flower", "flow", "flight"]))


# python power version
# import os

# strs=["c","acc","ccc"]
# hum=""
# c=os.path.commonprefix(strs)
# hum+=c

# print(hum)