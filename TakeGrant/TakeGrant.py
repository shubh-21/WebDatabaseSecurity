def take(AdjMat,subIndx,objIndx,p,rights):
    if (AdjMat[subIndx][objIndx]=='t' and rights in AdjMat[objIndx][p]):
        print("\nYou have taken the Access")
        AdjMat[subIndx][p]=rights
        return AdjMat

def grant(AdjMat,subIndx,objIndx,p,rights):
    if (AdjMat[subIndx][objIndx]=='g' and rights in AdjMat[subIndx][p]):
        print("\nYou have granted the Access")
        AdjMat[objIndx][p]=rights
        return AdjMat



subjects=["S1","S2"]
objects=["O1","O2"]
AdjMat=[['0','0','g','rw'],['0','0','t','0'],['0','0','0','0'],['0','0','0','0']]
print("\nwhat Operations you want to perform\n")
while(1):
    task=int(input("1.Take\n2.Grant\n3.Create Subject/Object\n4.Delete Right\n5.Exit\n"))
    if(task==1):
        print("\nThese are the subjects you are having : ",subjects)
        sub=input("\nFor whom you want to perform Take Operation\n")
        print("\nThese are the objects you are having : ",objects)
        obj=input("\nFrom whom you want to take rights\n")
        print("\nThese are the objects you are having : ",objects)
        p=input("\nOn which object you want to grant rights\n")
        rights=input("\nWhat right you want to grant\n1.r\n2.w\nYou may combine two or more rights as...rw\n")
        subIndx=subjects.index(sub)
        objIndx=objects.index(obj)+len(subjects)
        pIndx=objects.index(p)+len(subjects)
        AdjMat=take(AdjMat,subIndx,objIndx,pIndx,rights)
        print(AdjMat)
    if(task==2):
        print("\nThese are the subjects you are having : ",subjects)
        sub=input("\nFor whom you want to perform Grant Operation\n")
        print("\nThese are the objects you are having : ",objects)
        obj=input("\nFor whom you want to grant rights\n")
        print("\nThese are the objects you are having : ",objects)
        p=input("\nOn which object you want to have rights\n")
        rights=input("\nWhat right you want to have\n1.r\n2.w\nYou may combine two or more rights as...rw\n")
        subIndx=subjects.index(sub)
        objIndx=objects.index(obj)+len(subjects)
        pIndx=objects.index(p)+len(subjects)
        AdjMat=grant(AdjMat,subIndx,objIndx,pIndx,rights)
        print(AdjMat)
    if(task==3):
        subToAdd=input("\nSubject you want to Add:\n")
        newRow=[]
        for i in range(len(objects)+len(subjects)):
            newRow.append('0')
        AdjMat.append(newRow)
        subjects.append(subToAdd)
        for i in AdjMat:
            i.append('0')
        print(AdjMat)
    if(task==4):
        rightTodel=input("\nWhich Right You want to delete:\nr for read\nw for write\n")
        print("\nThese are the subjects you are having : ",subjects)
        sub=input("\nFor whom you want to remove right\n")
        print("\nThese are the objects you are having : ",objects)
        obj=input("\nOn whom you want to remove right\n")
        subIndx=subjects.index(sub)
        objIndx=objects.index(obj)+len(subjects)
        right=AdjMat[subIndx][objIndx]
        AdjMat[subIndx][objIndx]=right.replace(rightTodel,"0")
        print(AdjMat)
    if(task==5):
        break
