first=1
for i in range(0,5):
    if i%2==0:
        first=0
    else:
        first=1
    for j in range(0,i):
        print(first,end='')
        first=1-first
    print('')

# git config --global user.email "you@example.com"
# git config --global user.name "Your Name"