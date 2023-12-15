import csv
import os
import json

os.chdir(os.path.dirname(os.path.abspath(__file__)))
f=open("../data/4000-most-common-english-words.csv", "r")
words=f.read().split("\n")
f.close()

####

def word_with_most_vowels(wordlist):
    mostSoFar=0
    vowelCount=0
    vowels="aeiou"
    mostVowelsWord=""
    for word in wordlist:
        vowelCount=0
        for letter in word:
            if letter in vowels:
                vowelCount=vowelCount+1
        if vowelCount>mostSoFar:
            mostSoFar=vowelCount
            mostVowelsWord=word
    return mostVowelsWord
print("word with most vowels: ", word_with_most_vowels(words))
print("")

####

def average_word_length(wordlist):
    wordLengthCount=0
    for word in wordlist:
        wordLengthCount=wordLengthCount+len(word)
    return wordLengthCount/4000
print("average word length: ",round(average_word_length(words),0))
print("")

####

def most_common_starting_letter(wordlist):
    counts=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    mostCommonSoFar=0
    mostCommonLetter="p"
    for word in wordlist:
       firstletter=word[0].lower()
       position=ord(firstletter)-ord("a")
       counts[position]=counts[position]+1
       if counts[position]>mostCommonSoFar:
           mostCommonSoFar=counts[position]
           mostCommonLetter=chr(position + ord("a"))
    return mostCommonLetter

print("most common letter:", most_common_starting_letter(words))
print("")

 ####

f = open("../data/gradebook_data.csv", "r")
reader = csv.reader(f)
failingSeniors=""
freshmanCount=0
sophmoreCount=0
juniorCount=0
seniorCount=0
freshmanGrades=0
sophmoreGrades=0
juniorGrades=0
seniorGrades=0
countA=0
countB=0
countC=0
countD=0
countF=0
for row in reader:
    name, gradelevel, percent=row
    percent=int(percent)
    gradelevel=int(gradelevel)

    # number of abcdf
    if percent>=90:
        countA=countA+1
    elif percent>=80:
        countB=countB+1
    elif percent>=70:
        countC=countC+1
    elif percent>=60:
        countD=countD+1
    elif percent<=59:
        countF=countF+1

    # number of faiing seniors
    if gradelevel==12 and percent<60:
        failingSeniors=name+", "+failingSeniors

    # each grade level average percent
    if gradelevel==9:
        freshmanCount=freshmanCount+1
        freshmanGrades=freshmanGrades+percent
    if gradelevel==10:
        sophmoreCount=sophmoreCount+1
        sophmoreGrades=sophmoreGrades+percent
    if gradelevel==11:
        juniorCount=juniorCount+1
        juniorGrades=juniorGrades+percent
    if gradelevel==12:
        seniorCount=seniorCount+1
        seniorGrades=seniorGrades+percent

print("# of A:",countA)
print("# of B:",countB)
print("# of C:",countC)
print("# of D:",countD)
print("# of F:",countF)
print("")

freshmanAverage=freshmanGrades/freshmanCount
print("average freshman percent:",round(freshmanAverage,2))
sophmoreAverage=sophmoreGrades/sophmoreCount
print("average sophmore percent:",round(sophmoreAverage,2))
juniorAverage=juniorGrades/juniorCount
print("average junior percent:",round(juniorAverage,2))
seniorAverage=seniorGrades/seniorCount
print("average senior percent:",round(seniorAverage,2))

print("")
print("failing seniors:",failingSeniors)
f.close()

print("")

####

f = open("../data/1000-largest-us-cities.json", "r")
cities = json.load(f)
f.close()

print("Cities in Kansas: ")
for city in cities:
    if city["state"]=="Kansas":
        print(city["city"])

####
print("")

longestNameCity=""
for city in cities:
    if len(city["city"])>len(longestNameCity):
        
        longestNameCity=city["city"]
print("city w/ longest name:",longestNameCity)

####
print("")

farthestNorth=""
biggestLatitude=cities[0]["latitude"]

farthestEast=""
biggestLongitude=cities[0]["longitude"]

farthestSouth=""
smallestLatitude=cities[0]["latitude"]

farthestWest=""
smallestLongitude=cities[0]["longitude"]

for city in cities:
    if city["latitude"]>biggestLatitude:
        biggestLatitude=city["latitude"]
        farthestNorth=city["city"]
    elif city["latitude"]<smallestLatitude:
        smallestLatitude=city["latitude"]
        farthestSouth=city["city"]
    if city["longitude"]>biggestLongitude:
        biggestLongitude=city["longitude"]
        farthestEast=city["city"]
    elif city["longitude"]<smallestLongitude:
        smallestLongitude=city["longitude"]
        farthestWest=city["city"]
print("farthest north city:",farthestNorth)
print("farthest east city:",farthestEast)
print("farthest south city:",farthestSouth)
print("farthest west city:",farthestWest)
print("")

####

fastestGrowthCity=""
fastestGrowthPercent=0
fastestShrinkingCity=""
fastestShrinkingPercent=0
for city in cities:
    if city["growth_from_2000_to_2013"] == "":
        city["growth_from_2000_to_2013"] = 0
    else:
        city["growth_from_2000_to_2013"]=float(city["growth_from_2000_to_2013"].replace("%",""))
    
    if city["growth_from_2000_to_2013"]>fastestGrowthPercent:
        fastestGrowthPercent=city["growth_from_2000_to_2013"]
        fastestGrowthCity=city["city"]
    elif city["growth_from_2000_to_2013"]<fastestShrinkingPercent:
        fastestShrinkingPercent=city["growth_from_2000_to_2013"]
        fastestShrinkingCity=city["city"]
print("city w/ fastest growth:", fastestGrowthCity)
print("city w/ fastest shrinking:", fastestShrinkingCity)
print("")

####

highestPopulation=0
mostPopulatedCity=""
for city in cities:
    if int(city["population"])>highestPopulation:
        highestPopulation=int(city["population"])
        mostPopulatedCity=city["city"]
print("most populated city:", mostPopulatedCity)
print("")

####

