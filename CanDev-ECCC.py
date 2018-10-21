def flagger(data):
    '''
    (list[][]) -> (int, int, int, int, int, int, int)
    Receives data list and returns the amount of problems in each column
    Pre Condition: Data set is expected to follow given convention
    '''

    #Counters used to keep track of problems in each column
    scenarioCounter=0
    goalsCounter=0
    longGoalCounter=0
    dimensionCounter=0
    regionIDCounter=0
    region_nameCounter=0
    valueCounter=0

    #Loops through each row of data set
    for i in range(len(data)):

        #Checks if scenerio data set is integers
        if (not(data[i][0].isdigit()) or len(data[i][0])>70):
            scenarioCounter=scenarioCounter+1

            #print("Scanerio: " + str(data[i][0]))

        # Checks if goals data set is letters
        if (not(data[i][1].isalpha()) or len(data[i][0])>70):
            goalsCounter=goalsCounter+1

            #print("goals: " + str(data[i][1]))

        # Checks if longGoal data set is letters
        if (not(data[i][2].replace(" ","").replace("&","").replace("(","").replace(")","").isalpha()) or len(data[i][0])>70):
            longGoalCounter=longGoalCounter+1

            #print("long goal: " + str(data[i][2]))

        # Checks if dimension data set is letters
        if (not(data[i][3].isalpha()) or len(data[i][0])>70):
            dimensionCounter=dimensionCounter+1

            #print("dimension " + str(data[i][3]))

        # Checks if regionID data set is integers
        if (not(data[i][4].isdigit()) or len(data[i][0])>70):
            regionIDCounter=regionIDCounter+1

            #print("region ID: " + str(data[i][4]))

        # Checks if region_name data set is letters
        if (not(data[i][5].replace(" ","").replace("_","").replace("(","").replace(")","").replace("-","").isalpha()) or len(data[i][0])>70):
            region_nameCounter=region_nameCounter+1

            #print("region name: " + str(data[i][5]))

        # Checks if value data set is integers
        if (not(data[i][6].replace(".","").replace("-","").isdigit()) or len(data[i][0])>70):
            valueCounter=valueCounter+1

            #print("value: " + str(data[i][6]))

    return scenarioCounter, goalsCounter, longGoalCounter, dimensionCounter, regionIDCounter, region_nameCounter, valueCounter

dataset = open('dataTest.txt')
lines = dataset.readlines()
row = []
for line in lines:

    row.append(line.strip().split(","))

typeerror_count = flagger(row)