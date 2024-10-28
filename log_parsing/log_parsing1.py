logs = [
    "2021-04-15 0:21:19 ERROR DeleteProduct:84 - This is error : llukaku",
    "2021-01-06 8:56:10 WARN SaveAction:52 - There are too many requests on record number 5 : antomas",
    "2021-03-16 12:35:59 DEBUG SaveAction:16 - Kritische Fehler beim Speichern : iipeter",
    "2021-02-16 5:38:56 FATAL EditAction:19 - Product is already deleted : llukaku",
    "2021-02-16 8:13:35 FATAL EditAction:69 - Product not found for deleting : mkyong",
    "2021-04-18 3:45:43 DEBUG EditAction:16 - Ungültige Fehler : iipeter",
    "2021-04-07 17:25:48 WARN EditAction:23 - This is warn : llukaku",
    "2021-03-31 18:47:23 INFO EditAction:31 - Updated successfully record number 4 : iipeter",
    "2021-03-27 21:25:45 DEBUG SaveAction:61 - Ungültige Fehler : mkyong",
    "2021-01-12 23:36:8 DEBUG SaveAction:52 - Kritische Fehler beim Speichern : iipeter",
    "2021-02-18 5:51:42 INFO DeleteProduct:83 - Updated successfully record number 5 : iipeter",
    "2021-03-06 17:26:50 ERROR HelloExample:44 - Delete error : iipeter",
    "2021-03-07 2:50:25 DEBUG SaveAction:14 - Ungültige Fehler : iipeter",
    "2021-02-26 12:4:41 FATAL HelloExample:46 - Product is already deleted : mkyong",
    "2021-03-31 9:20:21 INFO DeleteProduct:57 - Updated successfully record number 5 : iipeter"
]

# Accessing each item in the lis using a for loop
for line in logs:
    line_split = line.split() # Split the string and convert to a list
    date = line_split[0] # The first element in the list is the data
    time = line_split[1] # The second element in the list is the time
    message = line_split[2] # The third element in the list is the error message
    user = line_split[-1] # The last element in the list is the user name

    # Print a message for only FATAL Errors
    if message == "FATAL":
        print(f"{user} => Error {message} on {date} at {time}")