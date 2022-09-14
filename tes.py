def averages(time1, time2):
    time1 = time1.split(":")
    time2 = time2.split(":")
    for elem in range(len(time1)):
      time1[elem] = int(elem)
    for elem in range(len(time2)):
      time2[elem] = int(elem)
    
    print(time1)
    print(time2)
    for i in time1:
      print(type(i))
    # for elem in time1:
    #   int(elem)
    # for elem in time2:
    #   int(elem)
    print(f"{time1[0]+time2[0]//2}:{time1[1]+time2[1]//2}:{time1[2]+time2[2]//2}")

averages("02:32:45", "02:34:25")