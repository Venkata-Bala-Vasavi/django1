from collections import Counter,namedtuple,OrderedDict,defaultdict,deque
Books=namedtuple('Book', ['book_id','title','author'])
copie=Counter()
history=defaultdict(deque)
arrivals=OrderedDict()
vip=deque()
def add_Book(book_id,title,author,copies=1):
    if copie[book_id]==0:
        copie[book_id]+=copies
        arrivals[book_id]=Books(book_id,title,author)
    else:
        copie[book_id]+=copies
def issue_Book(book_id,user_id):
    if copie[book_id]>0:
        copie[book_id]-=1
        history[user_id].appendleft(book_id)
        if len(history[user_id])>3:
            history[user_id].pop()
    else:
        print("Book is unavailable.")
def return_Book(book_id,user_id):
    copie[book_id]+=1
def prior_requests(user_id,book_id):
    vip.append((user_id,book_id))
    while vip:
        book_id,user_id=vip.popleft()
        if copie[book_id]>0:
            copie[book_id]-=1
            history[user_id].appendleft(book_id)
            if len(history[user_id])>3:
                history[user_id].pop()
        else:
            print("Book is unavailable.")
def display():
    common={}
    for user_id in history:
        borrowed_Books=Counter(history[user_id])
        for book_id in borrowed_Books:
            if book_id in common:
                common[book_id]+=1
            else:
                common[book_id]=1
    sorted_common=OrderedDict(sorted(common.items(), key=lambda x:x[1],reverse=True))
    print("Topmost borrowed books are:")
    print(list(sorted_common)[:2])
    user=input("Enter user id for browser history:")
    print(f"Borrow history of {user}:")
    print(history[user])
    print("New Arrivals in library:")
    for book_id, book in arrivals.items():
            print(f"{book_id}: {book.title} by {book.author}")
while True:
    op=int(input("Enter an option:\n1.Add a Book\n2.Issue a Book\n3.VIP request\n4.Display\n5.Exit\n"))
    if op==1:
        id=input("Enter book id:")
        title=input("Enter title of book:")
        author=input("Enter author of book:")
        add_Book(id,title,author)
    elif op==2:
        id=input("Enter book id:")
        user=input("Enter user id:")
        issue_Book(id,user)
    elif op==3:
        id=input("Enter book id:")
        user=input("Enter VIP user_id:")
        prior_requests(id,user)
    elif op==4:
        display()
    elif op==5:
        print("Thank you!")
        break
    else:
        print("Please enter a valid option.")
