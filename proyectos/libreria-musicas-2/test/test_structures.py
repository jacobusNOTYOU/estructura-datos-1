from libreria_musicas.models.structures import *

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

    # next
    print("Test: testing the `next()` method.")
    try:
        musics = []
        for i in range(len(playlists)):
            mus = []
            for j in range(len(titles)):
                mus.append(playlists[i].next(True))
            musics.append(mus)
    except Exception:
        print(
            f"Failed: an exception was raised!"
        )
        little_failed = True
    
    if little_failed:
        little_failed = False
        failed_test_number += 1

    test_number += 1

    # prev
    print("Test: testing the `prev()` method.")
    try:
        musics = []
        for i in range(len(playlists)):
            mus = []
            for j in range(len(titles)):
                mus.append(playlists[i].prev(True))
            musics.append(mus)
    except Exception:
        print(
            f"Failed: an exception was raised!"
        )
        little_failed = True
        raise
    
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


def static_playlist_test() -> int:
    failed_test_number = 0
    test_number = 0
    print("Test: StaticPlaylist test.")

    print("Test: testing constructor.")
    test_number += 1
    try:
        playlist = IndexedPlaylist('test', 3)
    except:
        print(f"Failed: constructor raised an exception.")
        failed_test_number += 1
    
    # is_empty
    passed = True
    print(f"Test: testing `is_empty`.")
    test_number += 1
    try:
        if playlist.is_empty() == False:
            print(f"Failed: playlist is empty, yet is_empty says it isn't!")
            passed = False
    except Exception as e:
        print(f"Failed: an exception was raised by `is_empty`!\n{e}")
        passed = False
    
    if not passed:
        failed_test_number += 1


    # append
    test_titles = ["", "test", "test test"]
    test_authors = ["", "test", "test test"]
    test_dirs = ["", "test", "test test"]
    print(f"Test: testing `append`.")
    test_number += 1
    try:
        for i in range(len(test_titles)):
            playlist.append(test_titles[i], test_authors[i], test_dirs[i])
    except Exception as e:
        print(f"Failed: `append` raised an exception!", e)
        failed_test_number += 1

    # is_in
    print("Test: testing `is_in`.")
    test_number += 1
    try:
        pos = playlist.is_in(test_titles[1])
        if pos == -1:
            print(f"Failed: `is_in` didn't find {test_titles[1]}!")
            failed_test_number += 1
    except:
        print(f"Failed: an exception was raised by `is_in`!")
        failed_test_number += 1
        raise

    # remove
    print("Test: testing `remove`.")
    test_number += 1
    try:
        playlist.remove(test_titles[0])
        if playlist.is_in(test_titles[0]) != -1:
            print(playlist.is_in(test_titles[0]))
            print(f"Failed: `remove` didn't remove {test_titles[0]}")
            failed_test_number += 1
    except Exception as e:
        print(f"Failed: an exception was raised by `remove`!", e)
        failed_test_number += 1
    
    playlist.append(test_titles[0], test_authors[0], test_dirs[0])

    # get
    print(f"Test: testing `get`.")
    test_number += 1
    try:
        test_music = playlist.get(test_titles[1])
        if test_music.title != test_titles[1]:
            print(f"Failed: {test_music.title} doesn't match {test_titles[1]}!")
    except:
        print(f"Failed: an exception was raised by `get`!")
        failed_test_number += 1

    # get_title
    passed = True
    print(f"Test: testing `get_titles`.")
    test_number += 1
    try:
        titles = playlist.get_titles()
        if len(titles) != len(playlist):
            print(
                f"Failed: `get_titles` doesn't return the same amount of titles"
                f" as musics that are in the playlist!"
            )
            passed = False
        for t in titles:
            if playlist.get(t) is None:
                print(f"Failed: `get_titles` returns titles that are not in playlist!")
                passed = False
    except:
        print(f"Failed: an exception was raised by `get_titles`!")
        passed = False
    
    if not passed:
        failed_test_number += 1

    # get_authors
    passed = True
    print(f"Test: testing `get_authors`.")
    test_number += 1
    try:
        authors = playlist.get_authors()

        if len(authors) != len(playlist):
            print(
                f"Failed: `get_authors` doesn't return the same amount of "
                f"authors as there are elements on playlist!"
            )
            passed = False
        
        for i in range(len(authors)):
            if authors[i] != playlist.musics[i].author:
                print(
                    f"Failed: the return of `get_authors` doesn't match the "
                    f"authors in the playlist!"
                )
                passed = False
    except:
        print(f"Failed: an exception was raised by `get_authors`!")
        passed = False
    
    if not passed:
        failed_test_number += 1

    # get_dir
    passed = True
    print(f"Test: testing `get_dir`.")
    test_number += 1
    try:
        direction = playlist.get_dir(test_titles[1])
        if direction != playlist.get(test_titles[1]).direction:
            print(f"Failed: {direction} is not the direction of {test_titles[1]}")
            passed = False
    except Exception as e:
        print(f"Failed: an exception was raised by `get_dir`!", e)
        passed = False
    
    if not passed:
        failed_test_number += 1

    # play
    passed = True
    print(f"Test: testing `play`.")
    test_number += 1
    try:
        music = playlist.play(test_titles[1])
        if music.title != test_titles[1]:
            print(
                f"Failed: `play`'s return's title {music.title} doesn't match "
                f"{test_titles[1]}!"
            )
            passed = False
    except:
        print(f"Failed: an exception was raised by `play`!")
        passed = False
    
    if not passed:
        failed_test_number += 1

    # next
    passed = True
    print(f"Test: testing `next`.")
    test_number += 1
    try:
        test_next = playlist.next()
        if test_next.title != test_titles[2]:
            print(
                f"Failed: the `next` '{test_next.title}' should be "
                f"'{test_titles[2]}'!"
            )
            passed = False
        playlist.next()
        try:
            test_next_2 = playlist.next()
        except StopIteration:
            print("Succes: raised the right Exception.")
        else:
            print(
                f"Failed: `next` shouldn't loop!"
            )
            passed = False

        test_next_3 = playlist.next(True)
        if test_next_3.title == test_next.title:
            print(
                f"Failed: `next` should loop!"
            )
            passed = False
    except Exception as e:
        print(f"Failed: an exception was raised by `next`!{e}")
        passed = False
    
    if not passed:
        failed_test_number += 1

    # prev
    passed = True
    print(f"Test: testing `prev`.")
    test_number += 1
    try:

        test_prev = playlist.prev()
        if test_prev.title != test_titles[1]:
            print(
                f"Failed: the `prev` '{test_prev.title}' should be "
                f"'{test_titles[1]}'!"
            )
            passed = False
        
        try:
            test_prev = playlist.prev()
        except StopIteration:
            print(f"Succes: The right exception was raised!")
        else:
            print(
                f"Failed: `prev` shouldn't loop!"
            )
            passed = False

        test_prev_3 = playlist.prev(True)
        print(test_prev_3)
        if test_prev_3.title == test_prev.title:
            print(
                f"Failed: `prev` should loop!"
            )
            passed = False
    except StopIteration:
        pass
    except Exception as e:
        print(f"Failed: an exception was raised by `prev`!\n{e}")
        passed = False
    
    if not passed:
        failed_test_number += 1

    # restart
    passed = True
    print(f"Test: testing `restart`.")
    test_number += 1
    try:
        playlist.restart()
        if playlist._current != 0:
            print("Failed: The playlist pointer should point at cero!")
            passed = False

    except Exception as e:
        print(f"Failed: an exception was raised by `restart`!\n{e}")
        passed = False
    
    if not passed:
        failed_test_number += 1

    # get
    passed = True
    print(f"Test: testing `get`.")
    test_number += 1
    try:
        pass
    except Exception as e:
        print(f"Failed: an exception was raised by `get`!\n{e}")
        passed = False
    
    if not passed:
        failed_test_number += 1

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
    # Library test
    static_playlist_test_number = static_playlist_test()
    print()
    completed_tests_number = (
        (music_test_number[1] - music_test_number[0])
        + (playlist_test_number[1] - playlist_test_number[0])
        + (librery_test_number[1] - librery_test_number[0])
        + (static_playlist_test_number[1] - static_playlist_test_number[0])
    )
    tests_number = (
        music_test_number[1] 
        + playlist_test_number[1] 
        + librery_test_number[1]
        + static_playlist_test_number[1]
    )
    print(f"Completed: {completed_tests_number}/{tests_number}")