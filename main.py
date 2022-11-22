
class Todo:
    def __init__(self,id,description,priority,status="pending"):
        self.id=id
        self.description=description
        self.priority=priority
        self.status=status
def addTodo(obj):
        string=""
        myf=open('Todo.txt','a')
        string+=str(obj.id)+"-"+obj.description+"-"+obj.priority+"-"+obj.status+"\n"
        myf.write(string)
        myf.close()
def searchByKeyWord(var):
        res=[]
        myf=open('Todo.txt','r')
        data=myf.readlines()
        for i in data:
                if i.split('-')[1].find(var)!=-1:
                    res.append(i)
        myf.close()
        return res
def updateToDo(prio,stat,id):
        myf=open('Todo.txt','r+')
        data=myf.readlines()
        for i in range(len(data)) :
            if data[i].split('-')[0]==str(id):
                data[i]=data[i].replace(data[i].split('-')[2],prio)
                data[i]=data[i].replace(data[i].split('-')[3],stat+"\n")
        myf.truncate(0)
        myf.seek(0)
        myf.writelines(data)
        myf.close()
def deleteToDo(id):
    myf=open('Todo.txt','r+')
    data=myf.readlines()
    for i in range(len(data)) :
           if data[i].split('-')[0]==str(id):
                data.remove(data[i])
                break
    myf.truncate(0)
    myf.seek(0)
    myf.writelines(data)
    myf.close()

def ShowAll():
        res=[]
        myf=open('Todo.txt','r')
        data=myf.readlines()
        for i in data:
            res.append(i)
        myf.close()
        return res

t1=Todo (2,'shop primo','low','done')
t2=Todo(1,'sell primo','high','pending')
addTodo(t1)
addTodo(t2)
print(searchByKeyWord('buy'))
updateToDo('medium','pending',2)
deleteToDo(3)
print(ShowAll())
