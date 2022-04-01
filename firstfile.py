#facebook likes
name = []
while (True):
	like=input("Enter a name:")
	if like == "":
		break
	else :
		name.append(like)
if len(name) == 1 :
    print (name[0],"likes your post")
elif len(name) == 2 :
	print (name[0],name[1], "Likes your post")
elif len(name) > 2:
	print (name[0],name[1],"and",len(name)-2,"others liked your post")

	