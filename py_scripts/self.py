#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
class Me:
    def __init__(self,name,age,id,gender,status,education):
        self.name = name
        self.age = age
        self.id = id
        self.gender = gender
        self.status = status
        self.education = education

    def speakname(self,lastname):
        return self.name+lastname

    def av_age(self):
        return str(float(self.age/100))

    def __add__(self, newguy):
        return Me(self.name + " " + newguy.name , 28, "234234", "Male", "Single", "M.Sc")

def main():
    aung = Me("Aung", 28, "324265", "Male", "Single", "M.Sc")
    thu = Me("Thu", 28, "324265324", "Male", "Single", "M.Sc(CS)")
    print aung.speakname(" Rha Hein")
    print aung.av_age()
    guys = aung+thu
    print guys.speakname(" Rha Hein")

if __name__ == "__main__":
    main()

