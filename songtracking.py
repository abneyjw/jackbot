import random

class songTracking:
    nice = [1,2,3,4,5,14,21,30,32,33,34]
    cozy = [6,7,8,11,12,13,18,35,36,37,38,39,40]
    storm = [15,16,17,24,25,26,41,42]
    winter = [19,20,21,22,23,29,31,43,44]

    def track(self, currentVibe, mySpot):
        if(currentVibe in self.nice):
                fi = "/home/pi/jackbot/nice.txt"
        elif(currentVibe in self.cozy):
                fi = "/home/pi/jackbot/cozy.txt"
        elif(currentVibe in self.storm):
                fi = "/home/pi/jackbot/storm.txt"
        else:
                fi = "/home/pi/jackbot/winter.txt"

        found = False
        print(fi)
        f = open(fi)
        countent = f.readlines()
        for i in range(0,len(countent)):
            curr = countent[i].split(',')
            if(curr[0] == mySpot.id()):
                found = True
                countent[i] = curr[0] + ',' + str(int(curr[1])+1) + '\n'
                break
        if (found == False):
            countent = countent+ [str(mySpot.id() + ',1\n')]
        
        f.close()
        f = open(fi, "w")
        f.writelines(countent)
        f.close()
    
    def rec(self,currentVibe,mySpot):
        if(currentVibe in self.nice):
                fi = "/home/pi/jackbot/nice.txt"
        elif(currentVibe in self.cozy):
                fi = "/home/pi/jackbot/cozy.txt"
        elif(currentVibe in self.storm):
                fi = "/home/pi/jackbot/storm.txt"
        else:
                fi = "/home/pi/jackbot/winter.txt"
        f = open(fi)
        choices = []
        countent = f.readlines()
        for i in range(0,len(countent)):
            curr = countent[i].split(',')
            if(int(curr[1]) >= 5):
                for j in range(0,int(curr[1])):
                    choices.append(curr[0])
        if(len(choices) > 0):            
            choice = random.randint(0,(len(choices)-1)) 
            print(choices[choice]) 
            mySpot.play_track([choices[choice]])
            f.close()





