import database

print("1 - Get Data")
print("2 - Write Data")
print("3 - Delete Data")
print("4 - Update Data")
op = input("Select an option: ")

if op == "1":
    oData = database.databaseClass()
    oData.getData()

elif op == "2":
    oData = database.databaseClass()
    name = input("Name: ")
    country = input("Country: ")
    oData.insertData(name,country)

elif op == "3":
    oData = database.databaseClass()
    oData.getData()
    id = input("Which element you want to delete?: ")
    oData.deleteData(id)

elif op == "4":
    oData = database.databaseClass()
    oData.getData()
    id = input("Which element you want to update?: ")
    name = input("Name: ")
    country = input("Country: ")
    oData.updateData(id,name,country)

else:
    print("Invalid option")

