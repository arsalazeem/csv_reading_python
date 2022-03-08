import openpyxl
import json
import csv
from csv import reader as rd


master_list = []

with open('activeServicesWithPackagesDetail.csv', 'r', encoding='cp1252') as file:
    reader = csv.reader(file)
    try:

        for row in reader:

            try:
                current_id = int(row[0])
                print(row)
                sellerId = row[0]
                email = row[1]
                serviceId = row[2]
                serviceName= row[3]
                description = row[4]
                isFeatured = row[5]
                categoryId = row[6]
                categoryName = row[7]
                packageId = row[8]
                packageType = row[9]
                pDescription = row[10]
                deliveryTimeInDays = row[11]
                isSourceFileIncluded = row[12]
                price = row[13]
                revisions=row[14]
                master_list.append({
                    "sellerId": row[0],
                    "email": row[1],
                    "serviceId": row[2],
                    "serviceName": row[3],
                    "description": row[4],
                    "isFeatured": row[5],
                    "categoryId": row[6],
                    "categoryName": row[7],
                    "packageId": row[8],
                    "packageType": row[9],
                    "pDescription": row[10],
                    "deliveryTimeInDays": row[11],
                    "isSourceFileIncluded": row[12],
                    "price": row[13],
                    "revisions": row[14]})

            except Exception as e:
                print(e)
                pass
    except:
        pass

#dump data as json into a json file
jsonString = json.dumps(master_list)
jsonFile = open("activeServicesWithPackagesDetail.json", "w")
jsonFile.write(jsonString)
jsonFile.close()
# import csv
# rdr = csv.reader(open("second_file.csv"))
# line1 = rd().__next__()
# line2 = rdr.__next__()
# second_file
# firstName
# lastName
# email
# dialCode
# phoneNumber
# aboutMe
# sellerType
# agencyName
# title
# streetAddress
# apartment
# city
# state
# zipCode
# endofsecondfile
# sellerId
# email
# serviceId
# serviceName
# description
# isFeatured
# categoryId
# categoryName
# packageId
# packageType
# pDescription
# deliveryTimeInDays
# isSourceFileIncluded
# price
# revisions
# second_file
# firstName
# lastName
# email
# dialCode
# phoneNumber
# aboutMe
# sellerType
# agencyName
# title
# streetAddress
# apartment
# city
# state
# zipCode
# print(count)
# jsonString = json.dumps(master_list)
# jsonFile = open("activeSellers.json", "w")
# jsonFile.write(jsonString)
# jsonFile.close()
# f = open("file1.txt", "r")
# i=0
# while True:
#     try:
#         print(f.read(i))
#         i = i + 1
#     except:
#         break
