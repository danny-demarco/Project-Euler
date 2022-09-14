def averages(time1, time2):
    min1, sec1, hun1 = [int(x) for x in time1.split(":")]
    min2, sec2, hun2 = [int(x) for x in time2.split(":")]
    time1 = hun1 + sec1 * 100 + min1 * 60 * 100
    time2 = hun2 + sec2 * 100 + min2 * 60 * 100
    time3 = (time1 + time2) / 2
    min3 = int(time3 // 6000)
    sec3 = int((time3 % 6000) // 100)
    hun3 = int(time3 % 100)
    result = '{:0>2}'.format(min3) + ":" + '{:0>2}'.format(sec3) + ":" + '{:0>2}'.format(hun3)
    print(result)


averages("00:01:50", "00:01:20")