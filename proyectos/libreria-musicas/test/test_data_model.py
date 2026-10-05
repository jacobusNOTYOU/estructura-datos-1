from models.logistic_engine import *
import json

def data_model_test():
    # add_playlist
    print("Test: Testing method `add_playlist()`.")
    data_model: DataModel = DataModel()

    failed_proof = False
    failed_tests: int = 0
    number_of_tests: int = 12
    test_number: int = 0

    # Casos Comunes
    test_names: list[str] = [
        "relax", "work", "study"
    ]
    try:
        for n in test_names:
            data_model.add_playlist(n)
    except NameError:
        print(f"Failed: {n} shouldn't raise a NamerError Exception!")
        failed_proof = True
    except Exception:
        print(f"Failed: {n} raised an exception!")
        failed_proof = True

    # Casos que debe levantar excepciones
    exception_raiser_names: list[str] = [
        "Library", "relax"
    ]
    try:
        data_model.add_playlist("Library")
    except NameError:
        pass
    except Exception:
        print(f"Failed: 'Library' raised a different exception than `NameError`!")
        failed_proof = True

    try:
        data_model.add_playlist(test_names[1])
    except NameError:
        pass
    except Exception:
        print(f"Failed: '{test_names[1]}' raised a different exception than `NameError`!")
        failed_proof = True
    
    if failed_proof:
        failed_proof = False
        failed_tests += 1
    test_number += 1
    print(f"Passed: {test_number - failed_tests}/{number_of_tests}.")

    # add_music
    print("Test: Testing method `add_music()`.")
    data_model._library.append("Library")

    test_titles: list[str] = [ "Stal", "Wet Hands", "Burges in the back"]
    test_authors: list[str] = ["C418", "C418", "WirdAI"]
    test_dirs: list[str] = ["m.mp3", "/df/", ""]
    test_names.append("Library")

    try:
        for n in test_names:
            for i in range(len(test_titles)):
                data_model.add_music(n, test_titles[i], test_authors[i], test_dirs[i])
    except Exception:
        print(f"Failed: No Exception should be raised!")
        failed_proof = True

    try:
        data_model.add_music("1234", test_titles[0], test_authors[0], test_dirs[i])
    except NameError:
        pass
    except Exception:
        print(f"Failed:  A different exception than `NameError` was raised!")
        failed_proof = True
    else:
        print("Failed: A `NameError` excepcion should be raised!")
        failed_proof = True

    try:
        data_model.add_music("Library", test_titles[0], test_authors[0], test_dirs[i])
    except NameError:
        pass
    except Exception:
        print(f"Failed:  A different exception than `NameError` was raised!")
        failed_proof = True
    else:
        print("Failed: A `NameError` excepcion should be raised!")
        failed_proof = True

    try:
        data_model.add_music(test_names[0], test_titles[0], test_authors[0], test_dirs[0])
    except Exception:
        print("Failed: An Exception was raised!")
        failed_proof = True

    if failed_proof:
        failed_proof = False
        failed_tests += 1
    test_number += 1
    print(f"Passed: {test_number - failed_tests}/{number_of_tests}.")

    # get_playlist_names
    print("Test: Testing method `get_playlist_names()`.")

    try:
        names: list[str] = data_model.get_playlist_names()
    except Exception:
        print(f"Failed: No exception should be raised!")
        failed_proof = True

    for n in test_names:
        if n not in names:
            print(f"Failed: '{n}' wasn't added to the library.")
            failed_proof = True
    
    if len(names) != len(test_names):
        print(
            f"Failed: There should be the same amount of names introduced in "
            f"`add_playlist()` as names returned by `get_playlist_names()`!"
        )
        failed_proof = True

    if failed_proof:
        failed_proof = False
        failed_tests += 1
    test_number += 1
    print(f"Passed: {test_number - failed_tests}/{number_of_tests}.")

    # get_music_titles
    print("Test: Testing method `get_music_titles()`.")
    try:
        music_titles: list[list[str]] = []
        for i in range(len(test_names)):
            for j in range(len(test_titles)):
                music_titles.append(data_model.get_music_titles(test_names[j]))

    except Exception:
        print(f"Failed: No exception should be raised!")
        failed_proof = True

    for i in range(len(music_titles)):
        for j in range(len(music_titles[i])):
            if music_titles[i][j] not in test_titles:
                print(
                    f"Failed: `get_music_titles()` returned a list of titles that "
                    f"doesn't match the ones provided in `add_music()`!"
                )
                failed_proof = True

    try:
        data_model.get_music_titles("1234")
    except NameError:
        pass
    except Exception:
        print(f"Failed: Wrong exception was raised!(Expected 'NameError')")
        failed_proof = True
    else:
        print(f"Failed: No exception was raised!(Expected 'NameError')")
        failed_proof = True

    if failed_proof:
        failed_proof = False
        failed_tests += 1
    test_number += 1
    print(f"Passed: {test_number - failed_tests}/{number_of_tests}.")

    # get_music
    print("Test: Testing method `get_music()`.")
    musics: list[str] = []
    try:
        for i in range(len(test_names)):
            for j in range(len(music_titles[i])):
                musics.append(data_model.get_music(names[i], music_titles[i][j]))
    except Exception:
        print(f"Failed: No exception should be raised!")
        failed_proof = True
    
    try:
        data_model.get_music("1234", test_titles[0])
    except NameError:
        pass
    except Exception:
        print(f"Failed: Wrong exception was raised!(Expected 'NameError')")
        failed_proof = True
    else:
        print(f"Failed: No exception was raised!(Expected 'NameError')")
        failed_proof = True

    try:
        data_model.get_music(test_names[0], "")
    except NameError:
        pass
    except Exception:
        print(f"Failed: Wrong exception was raised!(Expected 'NameError')")
        failed_proof = True
    else:
        print(f"Failed: No exception was raised!(Expected 'NameError')")
        failed_proof = True

    try:
        musics_dics: list[dict] = []
        for m in musics:
            musics_dics.append(json.loads(m))
    except Exception:
        print("Failed: Failed to deserialize a song!")
        failed_proof = True

    if failed_proof:
        failed_proof = False
        failed_tests += 1
    test_number += 1
    print(f"Passed: {test_number - failed_tests}/{number_of_tests}.")

    # get_music_dir
    print("Test: Testing method `get_music_dir()`.")
    try:
        directions: list[str] = []
        for i in range(len(names)):
            dirs: list[str] =[]
            for j in range(len(test_titles)):
                dirs.append(data_model.get_music_dir(names[i], test_titles[j]))
            directions.append(dirs)
    except NameError:
        print(
            f"Failed: Playlist or title not found!"
        )
        failed_proof = True
    except Exception:
        print(
            f"Failed: An exception was raised!"
        )
        failed_proof = True

    if failed_proof:
        failed_proof = False
        failed_tests += 1
    test_number += 1
    print(f"Passed: {test_number - failed_tests}/{number_of_tests}.")

    # get_playlist
    print("Test: Testing method `get_playlist()`.")

    try:
        playlists: list[str] = []
        for n in names:
            playlists.append(data_model.get_playlist(n))
    except Exception:
        print(
            f"Failed: No exception should be raised!"
        )
        failed_proof = True

    try:
        data_model.get_playlist("1243")
    except NameError:
        pass
    except Exception:
        print(
            f"Failed: Wrong exception was raised!"
        )
        failed_proof = True

    try:
        deserialized_playlists: list[str] = []
        for s in playlists:
            deserialized_playlists.append(json.loads(s))
    except json.JSONDecodeError:
        print(
            f"Failed: `get_playlists()` returns can't be deserializad!"
        )
        failed_proof = True
    except Exception:
        print(
            f"Failed: An exception was raised!"
        )
        failed_proof = True

    if failed_proof:
        failed_proof = False
        failed_tests += 1
    test_number += 1
    print(f"Passed: {test_number - failed_tests}/{number_of_tests}.")

    # to_json
    print("Test: Testing method `to_json()`.")
    try:
        library: str = data_model.to_json()
    except Exception:
        print(
            f"Failed: An exception was raised!"
        )
        failed_proof = True
    
    try:
        library_dict: dict = json.loads(library)
    except json.JSONDecodeError:
        print(
            f"Failed: The result of `to_json()` wasn't deserialized!"
        )
        failed_proof = True
    except Exception:
        print(
            f"Failed: An exception was raised!"
        )
        failed_proof = True

    if failed_proof:
        failed_proof = False
        failed_tests += 1
    test_number += 1
    print(f"Passed: {test_number - failed_tests}/{number_of_tests}.")

    # save
    print("Test: Testing method `save()`.")

    try:
        data_model.save("test/data_model_test.json")
    except Exception:
        print(
            f"Failed: An exception was raised!"
        )
        failed_proof = True

    if failed_proof:
        failed_proof = False
        failed_tests += 1
    test_number += 1
    print(f"Passed: {test_number - failed_tests}/{number_of_tests}.")

    # load
    print("Test: Testing method `load()`.")

    try:
        data_model_1: DataModel = DataModel()
        data_model_1.load("test/data_model_test.json")
    except Exception:
        print(
            f"Failed: An exception was raised!"
        )
        failed_proof = True
    
    if data_model_1.to_json() != data_model.to_json():
        print(
            f"Failed: The json file wasn't loaded correctly!"
        )
        failed_proof = True

    if failed_proof:
        failed_proof = False
        failed_tests += 1
    test_number += 1
    print(f"Passed: {test_number - failed_tests}/{number_of_tests}.")

    # remove_music
    print("Test: Testing method `remove_music()`.")

    try:
        data_model.remove_music("1234", test_titles[0])
    except NameError:
        pass
    except Exception:
        print(
            f"Failed: Wrong Exception raised!(Expected 'NameError')"
        )
        failed_proof = True
    else:
        print(
            f"Failed: Exception 'NameError' wasn't raised!"
        )
        failed_proof = True

    try:
        data_model.remove_music(test_names[0], "")
    except NameError:
        pass
    except Exception:
        print(
            f"Failed: Wrong Exception raised!(Expected 'NameError')"
        )
        failed_proof = True
    else:
        print(
            f"Failed: Exception 'NameError' wasn't raised!"
        )
        failed_proof = True

    try:
        for i in range(len(names)):
            for j in range(len(test_titles)):
                data_model.remove_music(names[i], test_titles[j])
    except Exception:
        print(
            f"Failed: An exception was raised!"
        )
        failed_proof = True

    if failed_proof:
        failed_proof = False
        failed_tests += 1
    test_number += 1
    print(f"Passed: {test_number - failed_tests}/{number_of_tests}.")

    # remove_playlist
    print("Test: Testing method `remove_playlist()`.")
    try:
        data_model.remove_playlist("1234")
    except NameError:
        pass
    except Exception:
        print(
            f"Failed: Wrong exception was raised!(Expected 'NameError')"
        )
        failed_proof = True
    else:
        print(
            f"Failed: Exception 'NameError' wasn't raised!"
        )
        failed_proof = True
    
    try:
        for n in names:
            data_model.remove_playlist(n)
    except Exception:
        print(
            f"Failed: An exception was raised!"
        )
        failed_proof = True

    if failed_proof:
        failed_proof = False
        failed_tests += 1
    print(f"Passed: {number_of_tests - failed_tests}/{number_of_tests}.")

    print()