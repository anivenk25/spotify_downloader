import main

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

results = []

# to search
for i in range (0,len(main.a1)) :
    query = str(main.a1[i])+ 'youtube'
    for j in search(query, tld="co.in", num=2, stop=2, pause=0):
        print(j)
        if 'youtube' in j :
            results.append(j)
print(results)