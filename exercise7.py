def moonweight(weight, weightincrease):
    try:
        for p in range(0,10):
            moonweight = weight/6
            print(moonweight)
            weight = weight + weightincrease
    except:
        print("Error")
moonweight(42,1)
