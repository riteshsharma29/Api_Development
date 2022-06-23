import requests

def test_get(*args):
    try :
        arg = [param for param in args]
        if len(arg) == 1:
            response = requests.get(arg[0])
        elif len(arg) == 3:
            url = arg[0] + arg[1] + "&" + arg[1]
            response = requests.get(arg[0])
        print("Status Code", response.status_code)
        print("JSON Response ", response.json())
    except Exception as e:
        print(e)

test_get("http://127.0.0.1:5000/All")
test_get("http://127.0.0.1:5000/4")
test_get("http://127.0.0.1:5000/4&Raj")

def test_delete(*args):
    try :
        arg = [param for param in args]
        if len(arg) == 1:
            response = requests.delete(arg[0])
        print("Status Code", response.status_code)
        print("JSON Response", response.json())
    except Exception as e:
        print(e)

test_delete("http://127.0.0.1:5000/delete/8")


def test_post(*args):
    try :
        arg = [param for param in args]
        if len(arg) == 2:
            response = requests.post(arg[0], json=arg[1])
        elif len(arg) > 2:
            params = arg[0] + arg[1] + "&" + arg[2] + "&" + arg[3] + "&" + arg[4]
            response = requests.post(params)
        print("Status Code", response.status_code)
        print("JSON Response ", response.json())
    except Exception as e:
        print(e)


# test_post("http://127.0.0.1:5000/add",{"FirstName":"Jason","LastName":"James","Gender":"Male","Salary":"10000"})
# test_post("http://127.0.0.1:5000/addParam/","Bhupendra","Saha", "Male","8222.69")


def test_put(*args):
    try :
        arg = [param for param in args]
        if len(arg) == 3:
            response = requests.put(arg[0]  + str(arg[1]), json=arg[2])
        print("Status Code", response.status_code)
        print("JSON Response ", response.json())
    except Exception as e:
        print(e)

test_put("http://127.0.0.1:5000/update/",4,{"FirstName":"Raju","LastName":"Raja","Gender":"Male","Salary":"10000"})


# url = "http://127.0.0.1:5000/All"
# response = requests.get(url)
# print("Status Code", response.status_code)
# print("JSON Response ", response.json())
#
# url = "http://127.0.0.1:5000/4"
# response = requests.get(url)
# print("Status Code", response.status_code)
# print("JSON Response ", response.json())
#
# url = "http://127.0.0.1:5000/4&Raj"
# response = requests.get(url)
# print("Status Code", response.status_code)
# print("JSON Response ", response.json())

# url = "http://127.0.0.1:5000/add"
# data = {"FirstName":"Ranveer","LastName":"Lamba","Gender":"Male","Salary":"10000"}
# response = requests.post(url, json=data)
# print("Status Code", response.status_code)
# print("JSON Response ", response.json())


# url = "http://127.0.0.1:5000/addParam/"
# params = "Rajendra&" + "Saha&" + "Male&" + "8222.69"
# print(url + params)
# response = requests.post(url + params)
# print("Status Code", response.status_code)
# print("JSON Response ", response.json())



# url = "http://127.0.0.1:5000/update/4"
# data = {"FirstName":"Raj","LastName":"Jana","Gender":"Male","Salary":"10000"}
# response = requests.put(url, json=data)
# print("Status Code", response.status_code)
# print("JSON Response ", response.json())

# url = "http://127.0.0.1:5000/delete/7"
# response = requests.delete(url)
# print("Status Code", response.status_code)
# print("JSON Response ", response.json())

