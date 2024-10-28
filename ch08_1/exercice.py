#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import os
import json

# Exercice 1
def compareFiles(FPfile1, FPfile2) :
    file1 = open(FPfile1, encoding = "utf-8")
    file2 = open(FPfile2, encoding = "utf-8")
    
    index = 0
    lineFile1 = file1.readline()
    lineFile2 = file2.readline()
    mistaken = False

    while (lineFile1 != "" and lineFile2 != "") and not mistaken :
        #print((lineFile1 != "" and lineFile2 != "") and not mistaken)
        if lineFile1 != lineFile2 :
            print(f"The files are not identical. Line {index + 1} is different.")
            
            print("\"" + lineFile1 + "\"" + "is not the same as : " + "'" + lineFile2 + "'")
            
            mistaken = True
        else :
            lineFile1 = file1.readline()
            lineFile2 = file2.readline()
        index += 1

    if not mistaken :
        print("The files are not different. You gave me the same file !")

    file1.close()
    file2.close()
    return mistaken


# Exercice 2
def copyFile(filePath1, filePath2, copy = " "*3) :
    file1 = open(filePath1, "r", encoding = "utf-8")
    file2 = open(filePath2, "w", encoding = "utf-8")

    lineFile1 = file1.readline()
    sb = ""

    while lineFile1 != "" :
        splittedLine = lineFile1.split(" ")
        newLine = ""
        for word in splittedLine :
            newLine += word + copy
        newLine += "\n"
        sb += newLine

        file2.write(newLine)
        lineFile1 = file1.readline()
        print(sb)

    print(sb)
    file1.close()
    file2.close()


# Exercice 3
def determineGrade(FPgradesPercent : str, FPfactors : str, FPoutput = "output/gradesAlpha.txt") -> list[tuple] :
    factors = {}
    alphaGrades = []

    with open(FPgradesPercent, "r", encoding = "utf8") as fileGrades :
        gradesPercent = fileGrades.readlines()

    with open(FPfactors, 'r', encoding = "utf8") as fileFactors :
        factors = json.load(fileFactors)
        print(factors)

    with open(FPoutput, "w", encoding = "utf-8") as newFile :
        for percentage in gradesPercent :
            grade = int(percentage)
            for letter, limits in factors.items() :
                if (limits[0] <= grade < limits[1]) :
                    alphaGrades.append((grade, letter))
                    newFile.write(str(grade) + "\t->\t" + letter.strip() + "\n")
    
    return alphaGrades




if __name__ == '__main__':
    if not os.path.exists("output") :
        os.mkdir("output")

    different = compareFiles("data/exemple.txt", "data/exemple2.txt")
    if not different :
        print("The files are not different.")
    
    copyFile("data/exemple.txt", "output/exemple_copy.txt")

    print(determineGrade("data/notes.txt", "data/seuils.json"))
