/*  DOM mod functions */
//  For Event
function showPlaylistList(playlistName) {
    let musicLists = document.getElementsByClassName("music-list");

    for (let musicList of musicLists) {
        musicList.style.display = "none";
    }

    let musicPlaylistList = document.getElementById(playlistName + "-music-list");
    if (musicPlaylistList !== null) {
        musicPlaylistList.style.display = "block";
    }
}

function showAddPlaylistDialog() {
    let dialog = document.getElementById("add-playlist-dialog");
    dialog.show();
}

function showRemovePlaylistDialog(playlistName) {
    let dialog = document.getElementById("remove-playlist-dialog");
    dialog.playlistName = playlistName;
    dialog.show();
}

function showAddMusicDialog() {
    let dialog = document.getElementById("add-music-dialog");
    dialog.show();
}

// playlists
function createPlaylist(playlistName) {
    let newPlaylist = document.createElement("article");
    newPlaylist.id = playlistName;

    let newPlaylistButton = document.createElement("input");
    newPlaylistButton.id = playlistName + "-button";
    newPlaylistButton.type = "button";
    newPlaylistButton.className = "playlist-button";
    newPlaylistButton.value = playlistName;
    newPlaylistButton.onclick = function () { showPlaylistList(playlistName); };

    let newPlaylistRemoveButton = document.createElement("input");
    newPlaylistRemoveButton.id = playlistName + "-remove-button";
    newPlaylistRemoveButton.type = "button";
    newPlaylistRemoveButton.className = "playlist-remove-button";
    newPlaylistRemoveButton.value = "Remove";
    // LAKS!: onclick event 
    newPlaylistRemoveButton.onclick = function () { showRemovePlaylistDialog(playlistName); };

    newPlaylist.append(newPlaylistButton);
    newPlaylist.append(newPlaylistRemoveButton);
    return newPlaylist;
}

function addPlaylist(playlistName) {
    let playlists = document.getElementById("playlists");
    let newPlaylist = createPlaylist(playlistName);
    playlists.append(newPlaylist);
}

// music-lists
function createMusicList(playlistName) {
    let newMusicList = document.createElement("article");
    newMusicList.id = playlistName + "-music-list";
    newMusicList.className = "music-list";

    let addMusic = document.createElement("article");
    addMusic.id = playlistName + "-add-music";
    addMusic.className = "add-music";

    let addMusicButton = document.createElement("input");
    addMusicButton.id = playlistName + "-add-music-button";
    addMusicButton.type = "button";
    addMusicButton.value = "+";
    addMusicButton.className = "add-music-button";

    addMusic.append(addMusicButton);

    newMusicList.append(addMusic);
    return newMusicList;
}

function addMusicList(playlistName) {
    let musicLists = document.getElementById("music-lists");
    let musicList = createMusicList(playlistName);
    musicLists.append(musicList);
}

//  music-item
function createMusicItem(playlistName, musicName) {
    let newMusic = document.createElement("article");
    newMusic.id = playlistName + "-" + musicName;
    newMusic.className = "music-item";

    let musicLabel = document.createElement("input");
    musicLabel.id = playlistName + '-' + musicName + "-music-label";
    musicLabel.type = "text";
    musicLabel.setAttribute("readonly", true);
    musicLabel.className = "music-item-label";
    musicLabel.value = musicName;

    let musicRemoveButton = document.createElement("input");
    musicRemoveButton.id = playlistName + '-' + musicName + "-remove-music-button";
    musicRemoveButton.type = "button";
    musicRemoveButton.className = "remove-music-button";
    musicRemoveButton.value = "Remove";

    let musicPlayButton = document.createElement("input");
    musicPlayButton.id = playlistName + '-' + musicName + "-play-music-button";
    musicPlayButton.type = "button";
    musicPlayButton.className = "play-music-button";
    musicPlayButton.value = "Play";

    newMusic.append(musicLabel);
    newMusic.append(musicRemoveButton);
    newMusic.append(musicPlayButton);
    return newMusic;
}

function addMusicItem(playlistName, musicName) {
    let musicList = document.getElementById(playlistName + "-music-list");
    let newMusicItem = createMusicItem(playlistName, musicName);
    musicList.append(newMusicItem);
}

//  redering functions
function render_page(playlistsDict) {
    let body = document.getElementById("body");

    let content = document.createElement("div");
    content.id = "content"

    let playlistList = document.createElement("article");
    playlistList.id = "playlists";

    let addPlaylistList = document.createElement("article");
    addPlaylistList.id = "add-playlist";

    let addPlaylistButton = document.createElement("input");
    addPlaylistButton.id = "add-playlist-button";
    addPlaylistButton.type = "button";
    addPlaylistButton.value = "+";
    addPlaylistButton.onclick = function () { showAddPlaylistDialog(); };

    addPlaylistList.append(addPlaylistButton);
    playlistList.append(addPlaylistList);
    content.append(playlistList);

    let musicLists = document.createElement("div");
    musicLists.id = "music-lists";

    content.append(musicLists);

    let musicPlayer = document.createElement("article");
    musicPlayer.id = "music-player";

    let closeMusicPlayerButton = document.createElement("input");
    closeMusicPlayerButton.id = "close-musicPlayer-button";
    closeMusicPlayerButton.type = "button";
    closeMusicPlayerButton.value = "+";

    let musicPlayerLabel = document.createElement("input");
    musicPlayerLabel.id = "music-player-label";
    musicPlayerLabel.type = "text";
    musicPlayerLabel.setAttribute("readonly", true);
    musicPlayerLabel.value = "silence";

    musicPlayer.append(closeMusicPlayerButton);
    musicPlayer.append(musicPlayerLabel);

    content.append(musicPlayer);

    body.append(content);

    let listOfPlaylists = Object.keys(playlistsDict);
    for (let key of listOfPlaylists) {
        addPlaylist(key);
        addMusicList(key);

        let musicList = playlistsDict[key];
        for (let music of musicList) {
            addMusicItem(key, music["title"]);
        }
    }

    showPlaylistList(listOfPlaylists[0]);
}

function update(instruction, input) {
    fetch(dataURL, {
        "method":"POST",
        "header":{"Content-Type":"application/json"},
        "body":JSON.stringify([instruction, input]),
    })
    .then((reponse) => reponse.json() )
    .then((result) => {
        document.getElementById("content").remove();
        playlist = result;
        render_page(playlist);
    });
}


async function setup() {
    const request = await fetch(dataURL);

    return request.json();

}

playlists = "";

const dataURL = "http://127.0.0.1:5000/data"

/*  Setup */
setup().then((result) => {
    playlist = result;
    render_page(playlist);
});

// Dialogs Setup
// add-playlist-dialog
document.getElementById("add-playlist-dialog-save").onclick = function () {
    let dialog = document.getElementById("add-playlist-dialog");
    let input = document.getElementById("add-playlist-dialog-input").value;

    update("add-playlist", input);

    dialog.close();
}

document.getElementById("add-playlist-dialog-cancel").onclick = function () {
    let dialog = document.getElementById("add-playlist-dialog");
    dialog.close();
}

// remove-playlist-dialog
document.getElementById("remove-playlist-dialog-save").onclick = function () {
    let dialog = document.getElementById("remove-playlist-dialog");
    let input = dialog.playlistName;

    update("remove-playlist", input);

    dialog.close();
}

document.getElementById("remove-playlist-dialog-cancel").onclick = function () {
    let dialog = document.getElementById("remove-playlist-dialog");
    dialog.close();
}
