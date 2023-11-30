book=[]
Your_Library=[]
Your_wishlist=[]
update_library=[]
final_library=[]
own=input("Entre the name of a book you own : ")
own1=input("Entre the name of another book you own (or press ENTRE to skip) : ")
Your_Library.append(own)
if own1:
    
    Your_Library.append(own1)
    print(Your_Library)
else: 
    print(Your_Library)
    wish=input("Entre the name of book you wish to have in future : ")
    wish1=input("Entre the name of another book you wish to have (or press ENTRE to skip) : ")
    Your_wishlist.append(wish)
    if wish1:
        
        Your_wishlist.append(wish1)
        print("Your wishlist:",Your_wishlist)
    else:
        print("Your wishlist:",Your_wishlist)
    wish2=input("Entre the name of a book from your wishlist you've acquired (or press ENTRE to skip) : ")
    if wish2 in Your_wishlist:
            
            update_library.extend(Your_Library)
            update_library.append(wish2)
            Your_wishlist.remove(wish2)
            print("Update library:",update_library)
            print("Update wishlist:",Your_wishlist)
    else:
            print("Update library:",update_library)
            print("Update wishlist:",Your_wishlist)

    donate=input("Entre the name of a book from your library you wish to donate (or press ENTRE to skip) : ")
    if donate:
                update_library.remove(donate)
                final_library.extend(update_library)
                print("Your library after the donations:",final_library)
    else:
                print(update_library)