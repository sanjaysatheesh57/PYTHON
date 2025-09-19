#This is a program to demonstrate the use of lists with an example. MOVIE WATCH LIST.

movies_to_watch= ['matrix','iron heart','rambo','interstellar']
print("The watch-list is :",movies_to_watch)

new= 'anabella'
movies_to_watch.append(new)
print("New watch-list is :",movies_to_watch)

movies_to_watch.remove('interstellar')
print(" watch-list is (removed watched movies) :",movies_to_watch)

movies_to_watch.sort()
print("sorted watch-list is :",movies_to_watch)

movies_to_watch.reverse()
print("reversed watch-list is :",movies_to_watch)

latest_movies=['loka','thudarum','96']
print("Latest movies added to watch list :",movies_to_watch+latest_movies)




