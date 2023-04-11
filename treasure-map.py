#hidden map declaration
row1 = ["🧱","️🧱","️🧱"]
row2 = ["🧱","🧱","️🧱"]
row3 = ["🧱","🧱","🧱"]
map=[row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position=input("Enter your position to mark")


#extraction of user input into usable data
position_list=list(position)
map_row=int(position_list[1])-1
map_column=int(position_list[0])-1

map[map_row][map_column]='🎁'

print(f"{row1}\n{row2}\n{row3}")



