import requests
import json
def reques():
    a=requests.get("http://saral.navgurukul.org/api/courses")   
    with open("file.json","w") as f:
        json.dump((a.json()),f,indent=4)
    b=a.json()
    c=0
    d=[]
    print("No. Corscs ----id")
    for i in b["availableCourses"]:
        # print(c,i["name"],"---->",i["id"])
        d.append(i["id"])
    # print(d)
        c+=1
    s=int(input("enter your seeriyal number"))
    r=requests.get("http://saral.navgurukul.org/api/courses/"+(d[s])+"/exercises")
    a=r.json()
    d1=[]
    c=0
    for i in a['data']:
        # for j in i:
        print(c,i['slug'])
        d1.append(i["slug"])
        c+=1
    # print(c,d1)
    user=int(input("ener your slug number"))
    req=requests.get("http://saral.navgurukul.org/api/courses/"+str(s)+"/exercise/getBySlug?slug="+d1[user])
    r1=req.json()
    print("content",r1["content"])

    print("if you want go previous content  than type up")
    print("if you want go next content than type next ")
    print("if you want go previous content than type previous")
    print("if you want go previous content than type exit")
    i=0
    for i in range(len(d1)):
        user1=input("enter your next step")
        if user1=="up":
            req=requests.get("http://saral.navgurukul.org/api/courses/"+str(s)+"/exercise/getBySlug?slug="+d1[user-1])
            r1=req.json()
            print(user-1,"content",r1["content"])
        if user1=="next":
            req=requests.get("http://saral.navgurukul.org/api/courses/"+str(s)+"/exercise/getBySlug?slug="+d1[user+1])
            r1=req.json()
            print(user+1,"content",r1["content"])
        if user1=="previous":
            req=requests.get("http://saral.navgurukul.org/api/courses/"+str(s)+"/exercise/getBySlug?slug="+d1[user])
            r1=req.json()
            print(user,"content",r1["content"])
        if user1=="exit":
            reques()
reques()




