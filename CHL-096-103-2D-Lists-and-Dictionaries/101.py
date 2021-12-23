'''
Using program 100, ask the user for a name and a region. Display the relevant data. Ask
the user for the name and region of data they want to change and allow them to make
the alteration to the sales figure. Display the sales for all regions for the name they
choose.
'''
data_set = {"John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
            "Tom":  {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
            "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
            "Fiona":{"N": 3904, "S": 3645, "E": 8821, "W": 2451}}

name = input("Enter a name: ")
region = input("Enter a region: ")
print(data_set[name][region])

nm_ch = input("Enter a name: ")
rg_ch = input("Enter a region: ")
vl_ch = int(input("Enter the new value: "))
data_set[nm_ch][rg_ch] = vl_ch

for k, v in data_set[nm_ch].items():
    print(k, ':', v)
    
    
