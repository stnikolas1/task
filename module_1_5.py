from idlelib.replace import replace

immutable_var=[1,'hi'],1,2,'world',False
print(immutable_var)
immutable_var[0][0]='by-by'
print(immutable_var)
mutable_list=[1,47,'Down',False,6.0]
mutable_list[3]=True
print(mutable_list)