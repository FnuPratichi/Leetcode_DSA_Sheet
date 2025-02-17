def cal_hammingDistance(s1,s2):
    distance = 0
    if len(s1)!=len(s2):
        print("Size mismatch")
    else:
        for i in range(0,len(s1)):
            if s1[i]!=s2[i]:
                distance = distance+1
        print(distance)


cal_hammingDistance('abab','abab')
cal_hammingDistance('abcb','abab')
cal_hammingDistance('abcc','abab')