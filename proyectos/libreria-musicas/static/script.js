//  Data Fetchers
async function get() {
    response = await fetch('/data')
    return response.json()
}

async function reportOp(instruction, data) {
    let response = await fetch('/data',{
        "method":"POST",
        "headers":{"Content-Type":"application/json"},
        "body":JSON.stringify({
            "instruction":instruction,
            "data":data
        })
    });

    return response.json();
}

//  Operations
async function addPlaylist(newPlaylist) {
    let response = await reportOp(
        'add_playlist',
        newPlaylist
    )

    if (response['message'] === 'Success!') {
        let newPlaylistElemtent = createPlaylistElement(newPlaylist);
    
        let playlistList = document.getElementById('playlist-list');
        playlistList.append(newPlaylistElemtent);
    }
    else {
        showErrorDialog(`The playlist ${newPlaylist} already exist!`);
    }
}

//  Events
function showAddPlaylistDialog() {
    let dialog = document.getElementById('add-playlist-dialog');
    dialog.show();
    let dialogText = document.getElementById('add-playlist-dialog-input');
    dialogText.focus();
}

function showErrorDialog(Error) {
    let dialog = document.getElementById('error-dialog');
    document.getElementById('error-dialog-label').value = Error;
    dialog.show();
}

//  Rendering
function createButton(parent, className, value, event) {
    let button = document.createElement('input');

    button.id = parent + className;
    button.type = 'button';
    button.className = className;
    button.value = value;
    button.onclick = event;

    return button;
}

function createLabel(parent, className, value) {
    let label = document.createElement('input');

    label.id = parent + className;
    label.type = 'text';
    label.setAttribute('readonly', true);
    label.className = className;
    label.value = value

    return label;
}

function createPlaylistElement(playlist, withRemove = true) {
    let playlistElement = document.createElement('article');

    let playlistButton = createButton(
        playlist, 
        'playlist-button',
        playlist,
        function (){}   //  Needs an event!
    )

    let removeButton = null;
    if (withRemove) {
        removeButton = createButton(
            playlist,
            'remove-button',
            'X',
            function (){}   //  Needs an event!
        )
    }

    playlistElement.append(playlistButton);
    if (withRemove) {
        playlistElement.append(removeButton);
    }

    return playlistElement;
}

function createMusicElement(title, author, withRemove = true) {
    let musicElement = document.createElement('article');

    let label = createLabel(
        title + '-' + author,
        'label',
        title + ' By ' + author
    )

    let removeButton = null;
    if (withRemove) {
        removeButton = createButton(
            title + '-' + author,
            'remove-button',
            'X',
            function (){}   //  Needs an event!
        );
    }
    
    let playButton = createButton(
        title + '-' + author,
        'play-button',
        '>',
        function (){}   //  Needs an event!
    )

    musicElement.append(label);
    if (withRemove) {
        musicElement.append(removeButton);
    }
    musicElement.append(playButton);
    
    return musicElement;
}

function renderPlaylist(playlist, addButton = true) {
    //  create the playlist 
    let musicListTemp = document.getElementById('music-list');
    if (musicListTemp !== null) {
        musicListTemp.remove();
    }
    let musicList = document.createElement('div');
    //  addButton
    if (addButton) {
        let buttonAdd = createButton(
            playlist, 'add-button', '+', function () {}
        );
        musicList.append(buttonAdd);
    }
    //  Render each music
    for (let music of playlist) {
        let withRemove = music == "Library";
        let musicElement = createMusicElement(
            music['title'],
            music['author'],
            withRemove
        );
        musicList.append(musicElement);
    }
    //  add to the DOM
    let content = document.getElementById('content');
    content.append(musicList);
}

function renderPlaylistList(playlists, addButton = true) {
    //  Make sure 'playlist-list' exist
    let Temp = document.getElementById('playlist-list');
    if (Temp !== null) {
        Temp.remove();
    }
    let playlsitList = document.createElement('article');
    playlsitList.id = 'playlist-list';

    //  Render each playlist elements
    for (let playlist of playlists) {
        let withRemove = true;
        if (playlist === 'Library') {
            withRemove = false;
        }
        let playlistElement = createPlaylistElement(playlist, withRemove);
        playlsitList.append(playlistElement);
    }

    //  addButton
    if (addButton) {
        let buttonAdd = createButton(
            'playlist-list', 'add-button', '+', showAddPlaylistDialog
        );
        playlsitList.prepend(buttonAdd);
    }

    //  add playlist list to the DOM
    let content = document.getElementById('content');
    content.prepend(playlsitList);
}

function renderLibrary(library) {
    //  RenderPlaylistList
    let playlistNames = Object.keys(library);
    renderPlaylistList(playlistNames);

    // Render de active playlist
    renderPlaylist(library['Library'], false);
}

get().then((result) => renderLibrary(result));

//  Specific Events
//  add-playlist-dialog
document.getElementById('add-playlist-dialog-exit').onclick = function() {
    let dialog = document.getElementById('add-playlist-dialog');
    dialog.close();
}

document.getElementById('add-playlist-dialog-save').onclick = function() {
    let dialog = document.getElementById('add-playlist-dialog');
    let newPlaylist = document.getElementById('add-playlist-dialog-input').value;
    dialog.close();
    addPlaylist(newPlaylist);
}

document.getElementById('add-playlist-dialog-cancel').onclick = function() {
    let dialog = document.getElementById('add-playlist-dialog');
    dialog.close();
}

//  error-dialog
document.getElementById('error-dialog-exit-button').onclick = function() {
    let dialog = document.getElementById('error-dialog');
    dialog.close();
}

document.getElementById('error-dialog-ok-button').onclick = function() {
    let dialog = document.getElementById('error-dialog');
    dialog.close();
}
