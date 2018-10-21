def flagger (data):

    #data = "2012,AO,Artisanal opportunities,future,0,Global average,80.74,"
    #data[r][c]
    #counts

    scenerioCounter=0
    goalsCounter=0
    longGoalCounter=0
    dimensionCounter=0
    regionIDCounter=0
    region_nameCounter=0
    valueCounter=0

    error_file = open("ERROR.txt", "w+")


    for i in range(len(data)):


        if (not(data[i][0].isdigit())):
            scenerioCounter=scenerioCounter+1

            error_file.write("ERROR_FLAGGED: Row: " + str(i) + " Colomn: 1  |  DATA IS NOT FORMATTED PROPERLY! MUST BE OF TYPE <INT>\n\n")

            #print("Scenerio: " + str(data[i][0]))

        if (not(data[i][1].isalpha())):
            goalsCounter=goalsCounter+1

            error_file.write("ERROR_FLAGGED: Row: " + str(i) + " Colomn: 2  |  DATA IS NOT FORMATTED PROPERLY! MUST BE OF TYPE <STRING>\n\n")

            #print("goals: " + str(data[i][1]))

        if (not(data[i][2].replace(" ","").replace("&","").replace("(","").replace(")","").isalpha())):
            longGoalCounter=longGoalCounter+1

            error_file.write("ERROR_FLAGGED: Row: " + str(i) + " Colomn: 3  |  DATA IS NOT FORMATTED PROPERLY! MUST BE OF TYPE <STRING>\n\n")

            #print("long goal: " + str(data[i][2]))

        if (not(data[i][3].isalpha())):
            dimensionCounter=dimensionCounter+1

            error_file.write("ERROR_FLAGGED: Row: " + str(i) + " Colomn: 4  |  DATA IS NOT FORMATTED PROPERLY! MUST BE OF TYPE <STRING>\n\n")

            #print("dimension " + str(data[i][3]))

        if (not(data[i][4].isdigit())):
            regionIDCounter=regionIDCounter+1

            error_file.write("ERROR_FLAGGED: Row: " + str(i) + " Colomn: 5  |  DATA IS NOT FORMATTED PROPERLY! MUST BE OF TYPE <INT>\n\n")

            #print("region ID: " + str(data[i][4]))

        if (not(data[i][5].replace(" ","").replace("_","").replace("(","").replace(")","").replace("-","").isalpha())):
            region_nameCounter=region_nameCounter+1

            error_file.write("ERROR_FLAGGED: Row: " + str(i) + " Colomn: 6  |  DATA IS NOT FORMATTED PROPERLY! MUST BE OF TYPE <STRING>\n\n")

            #print("region name: " + str(data[i][5]))

        if (not(data[i][6].replace(".","").replace("-","").isdigit())):
            valueCounter=valueCounter+1

            error_file.write("ERROR_FLAGGED: Row: " + str(i) + " Colomn: 7  |  DATA IS NOT FORMATTED PROPERLY! MUST BE OF TYPE <FLOAT>\n\n")

            #print("value: " + str(data[i][6]))

    return scenerioCounter, goalsCounter, longGoalCounter, dimensionCounter, regionIDCounter, region_nameCounter, valueCounter

dataset = open('dataTest.txt')
lines = dataset.readlines()
row = []
for line in lines:

    row.append(line.strip().split(","))

print(flagger(row))
