# initiate program
print("\n\t\t\tProgram initiated!")
#ask user to enter a valid ascii code
print("\n Please enter a valid ASCII code")
#define user code as an input
code=int(input())
if code in range(32,126):
  print("The correspondent letter for \"",code,"\"""ASCII code is" "\"", chr(code) ,"\"")
else:
  print("This is not a printable character!")
print("\n\t\t\tProgram finished!")
