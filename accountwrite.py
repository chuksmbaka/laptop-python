import sys

file = open("clients.dat", "a")

print("Enter the account, name and balance")
print("Enter end-of-file to end input")

count = 0
while (count < 2):
    accountline = input("- ")
    print("\n")
    count = count + 1

    #send the contents of accounLine to the file object above
file.writelines(accountline)