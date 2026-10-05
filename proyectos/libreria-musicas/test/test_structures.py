from models.structures import *

# Music test
def music_test() -> int:
    failed_test_number = 0
    test_number = 0

    print("Test: Music test")
    music_titles = ["", "test", "test test"]
    music_authors = ["", "tester", "tester re-tester"]
    musics = []
    for i in range(len(music_titles)):
        musics.append(Music(music_titles[i], music_authors[i]))
    test_number += 1

    for i in range(len(music_titles)):
        if musics[i].title != music_titles[i]:
            print(
                f"Failed: `Music`s title: {musics[i].title} "
                f"doen't match it's respective title: {music_titles[i]}"
            )
            failed_test_number += 1
    test_number += 1

    for i in range(len(music_authors)):
        if musics[i].author != music_authors[i]:
            print(
                f"Failed: `Music`s author: {musics[i].author} "
                f"doen't match it's respective author: {music_authors[i]}"
            )
            failed_test_number += 1
    test_number += 1
    
    print("Passed: Music test!")
    print(f"Passed: {test_number - failed_test_number}/{test_number}.")
    return failed_test_number, test_number


# Playlist test
def playlist_test() -> int:
    print("Test: Playlist test.")
    failed_test_number = 0
    test_number = 0
    little_failed = False

    # constructor
    print("Test: testing the constructor.")
    try:
        test_name = ["", "test", "test test"]
        playlists = []
        for n in test_name:
            playlists.append(Playlist(n))
        test_number += 1
    except _:
        print(
            f"Failed: Constructor raised an Exception."
        )
        failed_test_number += 1

    # append
    print("Test: testing the `append()` method.")
    try:
        test_titles = ["ana", "banana", "caravana"]
        test_authors = ["Pedro", "Marcos", "Maria"]
        test_dirs = ["google.com", "~/videos/el_video.mp5", ""]
        for i in range(len(playlists)):
            for j in range(len(test_titles)):
                playlists[i].append(test_titles[j], test_authors[j], test_dirs[j])
        test_number += 1
    except _:
        print(
            f"Failed: `append()` method raised an Exception."
        )
        failed_test_number += 1

    # get_titles
    print("Test: testing the `get_titles()` method.")
    try:
        titles = []
        for i in range(len(playlists)):
            titles.append(playlists[i].get_titles())

        for i in range(len(playlists)):
            for j in range(len(test_titles)):
                if titles[i][j] != test_titles[j]:
                    print(
                        f"Failed: title: {titles[i][j]} is diferent than"
                        f" expected {test_titles[j]}!"
                    )
                    little_failed = True

    except _:
        print(
            f"Failed: `get_titles()` method raised an Exception."
        )
        failed_test_number += 1

    if little_failed:
        little_failed = False
        failed_test_number += 1
    
    test_number += 1

    # get_authors
    print("Test: testing the `get_authors()` method.")
    try:
        authors = []
        for i in range(len(playlists)):
            authors.append(playlists[i].get_authors())

        for i in range(len(playlists)):
            for j in range(len(test_authors)):
                if authors[i][j] != test_authors[j]:
                    print(
                        f"Failed: author: {authors[i][j]} is diferent than"
                        f" expected {test_authors[j]}!"
                    )
                    little_failed = True

    except _:
        print(
            f"Failed: `get_authors()` method raised an Exception."
        )
        failed_test_number += 1

    if little_failed:
        little_failed = False
        failed_test_number += 1
    
    test_number += 1

    # get_dir
    print("Test: testing the `get_dir()` method.")
    try:
        directions = []
        for i in range(len(playlists)):
            directions.append(playlists[i].get_dir(test_titles[i]))
    except Exception:
        little_failed = True

    if little_failed:
        little_failed = False
        failed_test_number += 1
    
    test_number += 1

    # get
    print("Test: testing the `get()` method.")
    try:
        songs = []
        for i in range(len(playlists)):
            songs_row = []
            for j in range(len(titles)):
                songs_row.append(playlists[i].get(titles[i][j]))
            songs.append(songs_row)
        
        for i in range(len(playlists)):
            for j in range(len(titles)):
                if songs[i][j] is None:
                    print(f"Failed: a song shoudn't be None!")
                    little_failed != True
                elif songs[i][j].title != titles[i][j]:
                    print(
                        f"Failed: song title: {songs[i][j].title} doen't macht "
                        f"expected title: {titles[i][j]}!"
                    )
                    little_failed = True

    except _:
        print(
            f"Failed: `get()` method raised an Exception."
        )
        failed_test_number += 1
    
    if little_failed:
        little_failed = False
        failed_test_number += 1

    test_number += 1
    
    # remove
    print("Test: testing the `remove()` method.")
    try:
        pass
    except _:
        print(
            f"Failed: `remove()` method raised an Exception."
        )
        failed_test_number += 1

    print(f"Passed: {test_number - failed_test_number}/{test_number}.")
    return failed_test_number, test_number


def library_test() -> int:
    failed_test_number = 0
    test_number = 0
    little_failed = False
    print("Test: Library test.")

    test_names = ["", "test", "test test"]

    # constructor
    print("Test: testing the constructor.")
    try:
        libraries = []
        for i in range(len(test_names)):
            libraries.append(Library())
    except _:
        print(
            f"Failed: the `constructor` raised an exception!"
        )
        failed_test_number += 1

    if little_failed:
        little_failed = False
        failed_test_number += 1
    
    test_number += 1

    # append
    print("Test: testing the `append()` method.")
    try:
        for i in range(len(libraries)):
            for j in test_names:
                libraries[i].append(j)
    except _:
        print(
            f"Failed: the `constructor` raised an exception!"
        )
        failed_test_number += 1

    if little_failed:
        little_failed = False
        failed_test_number += 1
    
    test_number += 1

    # get_names
    print("Test: testing the `get_names()` method.")
    try:
        names = []
        for i in range(len(libraries)):
            names.append(libraries[i].get_names())

        for i in range(len(libraries)):
            for j in range(len(test_names)):
                if names[i][j] != test_names[j]:
                    print(
                        f"Failed: name: {names[i][j]} didn't match expected"
                        f" name: {test_names[i]}!"
                    )
                    little_failed = True
    except _:
        print(
            f"Failed: the `constructor` raised an exception!"
        )
        failed_test_number += 1

    if little_failed:
        little_failed = False
        failed_test_number += 1
    
    test_number += 1

    # add_music
    print("Test: testing the `add_music()` method.")
    titles = ["stal", "Wo ich auch stehe", ""]
    authors = ["C418", "Abraham"]
    directions = ["google.con", "~/musics/music.mp5", ""]
    try:
        lengths_1 = []
        for i in range(len(libraries)):
            lengths_1.append(len(libraries[i]))

        for i in range(len(libraries)):
            for j in range(len(names)):
                if j < len(authors):
                    if libraries[i].add_music(
                                    names[i][j], 
                                    titles[j], 
                                    authors[j],
                                    directions[j]
                                    ):
                        print(f"Test: succesfully added "
                            f"{titles[j]} to playlist: {names[i][j]}"
                        )
                    else:
                        print(f"Failed: `Playlist` {names[i][j]} not found!")
                        little_failed = True
                else:
                    libraries[i].add_music(names[i][j], titles[j], direction=directions[j])
                    print(f"Test: succesfully added "
                        f"{titles[j]} to playlist: {names[i][j]}"
                    )

        lengths_2 = []
        for i in range(len(libraries)):
            lengths_2.append(len(libraries[i]))

        for i in range(len(lengths_1)):
            if lengths_1[i] > lengths_2[i]:
                print(f"Failed: The length should have inceremented!")
                failed_test_number += 1

    except _:
        print(
            f"Failed: the `constructor` raised an exception!"
        )
        failed_test_number += 1

    if little_failed:
        little_failed = False
        failed_test_number += 1
    
    test_number += 1

    # get
    print("Test: testing the `get()` method.")
    try:
        playlists = []
        for i in range(len(libraries)):
            playlist = []
            for j in range(len(names[i])):
                playlist.append(libraries[i].get(names[i][j]))
            playlists.append(playlist)
        
        for i in range(len(playlists)):
            if len(playlists) != len(libraries[i]):
                print(
                    f"Failed: couldn't get the exact amount of playlist "
                    f"contained in a `Library` using the `get_names()` "
                    f"and the `get()` funcitons!"
                )
                little_failed = True
    except _:
        print(
            f"Failed: the `constructor` raised an exception!"
        )
        failed_test_number += 1

    if little_failed:
        little_failed = False
        failed_test_number += 1
    
    test_number += 1

    # get_music_dir
    print("Test: testing the get_music_dir()` method.")
    try:
        dirs = []
        for i in range(len(names)):
            dirss = []
            for j in range(len(titles)):
                dirss.append(libraries[i].get_music_dir(names[i][j], titles[j]))
            dirs.append(dirss)
    except NameError:
        print(
            f"Failed: `NameError` was rarised!"
        )
        little_failed = True
    except Exception:
        print(
            f"Failed: An exception was raised!"
        )
        little_failed = True

    if little_failed:
        little_failed = False
        failed_test_number += 1
    
    test_number += 1

    # remove
    print("Test: testing the `remove()` method.")
    try:
        for i in range(len(names)):
            for j in range(len(names[i])):
                libraries[i].remove(names[i][j])

        for i in range(len(libraries)):
            if len(libraries[i]) != 0:
                print(
                    f"Failed: Couldn't reomove all `Playlists` in `Library` "
                    f"#{i}!"
                )
                little_failed = True
    except _:
        print(
            f"Failed: the `constructor` raised an exception!"
        )
        failed_test_number += 1

    if little_failed:
        little_failed = False
        failed_test_number += 1
    
    test_number += 1

    print(f"Passed: {test_number - failed_test_number}/{test_number}.")
    return failed_test_number, test_number
    

def structures_test():
    # Music test
    music_test_number = music_test()
    print()
    # Playlist test
    playlist_test_number = playlist_test()
    print()
    # Library test
    librery_test_number = library_test()
    print()
    completed_tests_number = (
        (music_test_number[1] - music_test_number[0])
        + (playlist_test_number[1] - playlist_test_number[0])
        + (librery_test_number[1] - librery_test_number[0])
    )
    tests_number = (
        music_test_number[1] 
        + playlist_test_number[1] 
        + librery_test_number[1]
    )
    print(f"Completed: {completed_tests_number}/{tests_number}")