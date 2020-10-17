# coding: utf-8
"""
@software: PyCharm
@file: ChineseSort.py
@time: 2020年10月16日22:21:34
@Desc：按照中文排序
"""
# 建立拼音辞典
dic_py = dict()

with open('./file/py.txt', 'r', encoding='utf8') as f:
    content_py = f.readlines()

    for i in content_py:
        i = i.strip()
        word_py, mean_py = i.split('\t')
        dic_py[word_py] = mean_py

# 建立笔画辞典
dic_bh = dict()
with open('./file/bh.txt', 'r', encoding='utf8') as f:
    content_bh = f.readlines()

    for i in content_bh:
        i = i.strip()
        word_bh, mean_bh = i.split('\t')
        dic_bh[word_bh] = mean_bh


###############################
# 辞典查找函数
def searchdict(dic, uchar):
    # 一    齚
    if u'\u4e00' <= uchar <= u'\u9fa5':
        value = dic.get(uchar)
        if value == None:
            value = '*'
    else:
        value = uchar
    return value


# 比较单个字符
def comp_char_PY(A, B):
    if A == B:
        return -1
    pyA = searchdict(dic_py, A)
    pyB = searchdict(dic_py, B)

    # 比较拼音
    if pyA > pyB:
        return 1
    elif pyA < pyB:
        return 0

    # 比较笔画
    else:
        bhA = eval(searchdict(dic_bh, A))
        bhB = eval(searchdict(dic_bh, B))
        if bhA > bhB:
            return 1
        elif bhA < bhB:
            return 0
        else:
            return "拼音相同，笔画也相同？"


# 比较字符串
def comp_char(A, B):
    n = min(len(A), len(B))
    i = 0
    while i < n:
        dd = comp_char_PY(A[i], B[i])
        # 如果第一个单词相等，就继续比较下一个单词
        if dd == -1:
            i = i + 1
            # 如果比较到头了
            if i == n:
                dd = len(A) > len(B)
        else:
            break
    return dd


# 排序函数
def cnsort(nline):
    n = len(nline)
    lines = "\n".join(nline)

    for i in range(1, n):  # 插入法
        tmp = nline[i]
        j = i
        while j > 0 and comp_char(nline[j - 1], tmp):
            nline[j] = nline[j - 1]
            j -= 1
        nline[j] = tmp
    return nline

