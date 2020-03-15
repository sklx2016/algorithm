def LongestSubstring(s):
    res = 0
    if len(s) == 0:
        return 0
    str_dict = {}
    start = 0
    for i in range(len(s)):
        if s[i] in str_dict and str_dict[s[i]] >= start:
            start = str_dict[s[i]] + 1
        res_cur = i - start + 1
        str_dict[s[i]] = i
        res = max(res, res_cur)
    return res

















