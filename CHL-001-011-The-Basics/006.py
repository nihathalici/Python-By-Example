'''
Ask how many slices of pizza the user started with and ask how many slices
they have eaten. Work out how many slices they have left and display
the answer in a user- friendly format.
'''

startingSlices = int(input('How many slices of pizza have you started?'))
eatenSlices = int(input('How many slices have you eaten?'))

print("From {} slices of pizza, {} slices have you already been eaten.".format(startingSlices, eatenSlices))

'''
Author's solution:

startNum = int(input('Enter the number of slices of pizza you started with: '))
endNum = int(input('How many slices have you eaten? '))
slicesLeft = startNum - endNum
print("You have", slicesLeft, "slices remaining")
'''




