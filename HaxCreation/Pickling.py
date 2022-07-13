import pickle

my = {1: 'a',2:'b',3:'c'}
pickle_file= open("picklefile.txt","ab")
pickle.dump(my,pickle_file)
pickle_file=open("picklefile.txt","rb")
new = pickle.load(pickle_file)
print(new)
