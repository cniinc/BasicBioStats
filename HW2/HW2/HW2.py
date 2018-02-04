
import statistics
import math
import numpy
import matplotlib
import matplotlib.pyplot

#for saving PNGs of figures
matplotlib.use('agg')


msg = "Completing Homework for lessons 1,2"
print(msg)

print("using cholesterolData below:")
cholesterolData = [185, 225, 240, 196, 175, 180, 194, 147, 223]
print(cholesterolData)


class jasonMakesStatistics:
    def mean(data):
        
        meanVal = sum(data)/max(len(data), 1)
        return meanVal
    
    def stdDeviation(data):

        meanVal = jasonMakesStatistics.mean(data)
        

        dataMinusMean = []
        for val in data:
            dataMinusMean.append(val - meanVal)

        sumDMMSquared = 0

        for val in dataMinusMean:
            sumDMMSquared += (val*val)
            
        variance = sumDMMSquared/(len(data)-1)
        return math.sqrt(variance)
    
    def median(data):  #sort, then find middle. If len() divisible by 2, find find mean of len/2 and len/2 + 1
        sortedData = sorted(data)
        medianVal = 0
        

        if len(sortedData) % 2 == 0:  #"if (remainder when divided by) 2 is equal to 0"
            medianVal = jasonMakesStatistics.mean([sortedData[len(sortedData)//2], sortedData[len(sortedData)//2 - 1]])
        else:
            medianVal = sortedData[len(sortedData)//2] #why is this wrong?

        return medianVal

    def getQuartile(quartile, data):
        if quartile < 1 or quartile > 3:
            return "Error: You must give a quartile number between 1 (1st quartile) and 3 (3rd Quartile)." 

        sortedData = sorted(data)

        evenLength = False
        if len(sortedData) %2 == 0:
            evenLength = True
        
        #I wish Python had Case Switch functions.
        if(quartile == 2):
            return jasonMakesStatistics.median(sortedData)

        #if not, make array and split into two different arrays (if odd, remove middle value)
        #print(sortedData)
        if evenLength:
            sortedArray = numpy.array(sortedData)
            sortedArraySplit = numpy.split(sortedArray, 2)
        if not evenLength:
            sortedData.remove(sortedData[len(sortedData)//2])
            sortedArray = numpy.array(sortedData)
            sortedArraySplit = numpy.split(sortedArray, 2)
        
        if(quartile == 1):
            #print(sortedArraySplit[0])
            lowerHalfList = sortedArraySplit[0].tolist()
            yourMedian = jasonMakesStatistics.median(lowerHalfList)
            return yourMedian
                   
        if(quartile == 3):
            #print(sortedArraySplit[1])
            upperHalfList = sortedArraySplit[1].tolist()
            yourMedian = jasonMakesStatistics.median(upperHalfList)
            return yourMedian
    
    def makeBoxPlot(data):
        fig = matplotlib.pyplot.figure(1, figsize = (9,6))

        #coded way of saying a 1x1 plot for list 1: https://stackoverflow.com/questions/3584805/in-matplotlib-what-does-the-argument-mean-in-fig-add-subplot111
        ax = fig.add_subplot(111)

        bp = ax.boxplot(data, showfliers =True)

        fig.savefig('fig1.png', bbox_inches='tight')

    def anyOutliers(data):
        q1 = jasonMakesStatistics.getQuartile(1, data)
        q3 = jasonMakesStatistics.getQuartile(3, data)

        iqr = q3-q1

        upperLimit = q3 + (1.5)*iqr
        lowerLimit = q1 - (1.5)*iqr

        
        #this is probably computationally intensive in large data sets
        outliers = []
        for val in data:
            if val > upperLimit or val < lowerLimit:
                outliers.append(val)

        if len(outliers) == 0:
            return ("no outliers!")

        #if no outliers, function stops at above return. Thus, this only prints if there are outliers
        return outliers


                

        
    

        
           
#jasonMakesStatistics.makeBoxPlot(cholesterolData)
print(jasonMakesStatistics.anyOutliers(cholesterolData))