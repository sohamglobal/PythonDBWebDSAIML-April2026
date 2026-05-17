file=open("top_100_films.csv","r")

data=file.readline()

while data:
    print(data.split(',')[0]+" | "+data.split(',')[1]+" | "+data.split(',')[5])
    data=file.readline()


file.close()
