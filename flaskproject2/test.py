import requests
base="http://127.0.0.1:5000/"

data1=[{"user_name":"Vijay","user_password":"pass","user_age":21,"user_mobile_no":123454345},
{"user_name":"Sam","user_password":"sss","user_age":25,"user_mobile_no":37389798},
{"user_name":"Ram","user_password":"abc","user_age":30,"user_mobile_no":91387918}]

for i in range(len(data1)):
	response=requests.put(base+"user/"+str(i),data1[i])
	print(response.json())

input()
d1={"user_name":"Ram","user_password":"abc","user_mobile_no":91387918}
response=requests.put(base+"user/8",d1)
print(response.json())

input()
response=requests.get(base+"user/0")
print(response.json())

input()
response=requests.patch(base+"user/0",data1[0])
print(response.json())

input()
data2=[{"bus_name":"redbus","bus_from":"chennai","bus_to":"salem","bus_cost":450,"bus_seats":30},
{"bus_name":"bluebus","bus_from":"chennai","bus_to":"coimbatore","bus_cost":700,"bus_seats":35},
{"bus_name":"greenbus","bus_from":"chennai","bus_to":"madurai","bus_cost":750,"bus_seats":25}]

for i in range(len(data1)):
	response=requests.put(base+"bus/"+str(i),data2[i])
	print(response.json())

input()
d2={"bus_name":"redbus","bus_from":"chennai","bus_to":"salem","bus_cost":450}
response=requests.put(base+"bus/8",d2)
print(response.json())

input()
response=requests.put(base+"user/1",d2)

input()
d22={"bus-name":"bluebus","bus_from":"chennai","bus_to":"coimbatore","bus_cost":700,"bus_seats":40}
response=requests.patch(base+"bus/1",d22)
print(response.json())

input()
response=requests.get(base+"bus/0")
print(response.json())

input()
response=requests.get(base+"bus/1")
print(response.json())

input()
response=requests.get(base+"user/1")
print(response.json())

input()
d3={"bus_id":1,"user_id":1,"book_tickets":3}
response=requests.put(base+"book/4",d3)
print(response.json())

input()
response=requests.get(base+"bus/1")
print(response.json())