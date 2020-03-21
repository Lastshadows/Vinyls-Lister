import pickle
import os.path
from artist import Artist

def displayMenu():

    print("\npress :\n")
    print("1 : to add something")
    print("2 : to delete something")
    print("3 : to exit\n")

    choice = input("type you choice here : ")
    return choice


# constants
filename = 'artist_dictionnary.pickle'
dict = {}
over =  False

# creating or loading the dictionnary
if not os.path.isfile(filename):

    # create a first element to add to our collection. Symbolic included
    initial_vinyl = Artist('Pink Floyd', 'Alternatif Rock')
    initial_vinyl.addVinyl('The Wall')
    initial_vinyl.addVinyl('Animals')

    dict = {initial_vinyl.artist_name : initial_vinyl}

else:

    with open(filename, 'rb') as handle:
        dict = pickle.load(handle)

print(" Hello Pierre !")
print(" Do you want to add a vinyl, to delete one or to get out ? ")

while not over:

    choice = displayMenu()

    # add a vinyl
    if choice == str(1):
        print("\nType the name of the artist and the name of the album , separated with commas")
        print("example : Pink Floyd, The Wall\n")

        # getting the stdin
        stdin = input("")

        # getting the terms separated by commas
        vinyl = stdin.split(',')

        # removing left and right whitespaces
        for i in range(len(vinyl)):
            vinyl[i] = vinyl[i].lstrip()
            vinyl[i] = vinyl[i].rstrip()

        artist_name, album_name= vinyl

        # if artist already exist, just append the album
        if artist_name in dict:
            dict[artist_name].addVinyl(album_name)

        # else create a new artist and add the vinyl
        else:

            print("New artist ! What is the kind of music ?")
            music_style =  input("")
            music_style = music_style.lstrip()
            music_style = music_style.rstrip()

            artist = Artist(artist_name, music_style)
            artist.addVinyl(album_name)
            dict[artist_name] =  artist

    # delete an album
    elif choice == str(2):

        print("Type the name of the artist and the name of the album that you want to delete, separated with commas ")
        to_delete =  input("example : Pink Floyd, The Wall \n")

        # getting the terms separated by commas
        to_delete = to_delete.split(',')

        # removing left and right whitespaces
        for i in range(len(to_delete)):
            to_delete[i] = to_delete[i].lstrip()
            to_delete[i] = to_delete[i].rstrip()

        artist_name, album_name = to_delete

        if artist_name in dict:

            if album_name in dict[artist_name].vinyls:
                dict[artist_name].vinyls.remove(album_name)

                # if there are no more vinyls of this artist, delete him altogether
                if len(dict[artist_name].vinyls) == 0:
                    dict.pop(artist_name, None)
                    print("suppressed !\n")

            # couldnt  find the album
            else:
                print("album didn't exist !\n")


        else:
            print("artist didnt exist !")

    # not choice 1 or choice 2 : get out of here
    else:
        over = True

sorted_keys =  sorted (dict.keys())
count = 0

with open(filename, 'wb') as handle:
    pickle.dump(dict, handle, protocol=pickle.HIGHEST_PROTOCOL)


for artist_name in sorted_keys:
    print(dict[artist_name].artist_name + ", " + dict[artist_name].style)
    print(dict[artist_name].nbOfAlbums() + " albums")
    print(dict[artist_name].vinyls)
    print("\n")

    count += dict[artist_name].nbOfAlbumsInt()


print("total of " + str(count) + " albums")

# save the dict
with open(filename, 'wb') as handle:
    pickle.dump(dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
