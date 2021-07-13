#since root path is '/', ''(empty) will point to root
#creating Path class with curr_path
#cd will pop the last directory upon '..'
#expecting correct inputs for simplicity, error handling not perfectly managed
#input the path directly
# some test case scenarios have been hardcoded for reference, before accepting user input
class Path:
    def __init__(self, path):
        self.curr_path = path

    def cd(self, new_path):
        new_pathList=new_path.split('/')
        pathLength=len(new_pathList)
        pathList=self.curr_path.split('/')
        pathList = [a for a in pathList if a !=""]
        i=0;
        if new_pathList[0]=='':#absolute path - revert to root
            #direct pathname
            del pathList[:]
            if new_pathList[1]!='..':
                pathList.append('/'+new_pathList[1])
            i+=2
        while(i<pathLength):
            j=len(pathList)-1
            if new_pathList[i]=='..' and pathList:
                #parent dir
                pathList.pop(j)
            elif pathList:
                pathList.append(new_pathList[i])
            elif new_pathList[i]!='..':
                pathList = [new_pathList[i]]
            i=i+1
        self.curr_path="/".join(pathList)
        #print("asdfasdf   ",self.curr_path )
        if not self.curr_path or self.curr_path[0] != "/":
            self.curr_path = "/"+self.curr_path
        

path = Path('/a')
path.cd('x/../y/z')
print(path.curr_path)#/a/y/z

path = Path('/a')
path.cd('x/y/z')
print(path.curr_path)#/a/x/y/z

path = Path('/a')
path.cd('/x/../y/z')
print(path.curr_path)#/y/z

path = Path('/a')
path.cd('/../a/b')
print(path.curr_path)#/a/b

path = Path('/a')
path.cd('..')
print(path.curr_path)#/

path = Path('/a')
path.cd('/..')
print(path.curr_path)#/

path = Path('/')
print("Current Path: ",path.curr_path)
while True:
    in_path = input("Hit enter without input to exit.\ncd ")
    if not in_path: break
    path.cd(in_path)
    print("Current Path: ",path.curr_path)

"""
Output:
/a/y/z
/a/x/y/z
/y/z
/a/b
/
/
Hit enter without input to exit.
cd x
/x
Hit enter without input to exit.
cd ..
/
Hit enter without input to exit.
cd /y/z/ss/../asdf
/y/z/asdf
Hit enter without input to exit.
cd zx/../..
/y/z
Hit enter without input to exit.
cd 
"""

