//  Data Fetchers
async function get() {
    let response = await fetch('/data');
    return response.json();
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
        showErrorDialog(`La playlist ${newPlaylist} ya existe!`);
    }
}

async function getPlaylist(playlistName) {
    let response = await reportOp(
        'get_playlist',
        playlistName
    );

    if (Object.hasOwn(response, 'message')) {
        console.log(`Error: Playlist ${playlistName} not found!`);
        showErrorDialog(
            `Error: No se encontro la playlist ${playlistName}!`
        );
    }
    else {
        return response;
    }
}

async function removePlaylist(oldPlaylist) {
    let response = await reportOp(
        'remove_playlist',
        oldPlaylist
    )

    if (response['message'] === 'Success!') {
        document.getElementById(oldPlaylist).remove();
        if (oldPlaylist === activePlaylist) {
            let playlist = await getPlaylist('Library');
            activePlaylist = 'Library';
            renderPlaylist(playlist, false, false);
        }
    }
    else {
        showErrorDialog(`No se encontro ${oldPlaylist} la playlist!`);
    }
}

async function displayPlaylist(playlistName, withAdd, withRemove) {
    let response = await reportOp(
        'get_playlist',
        playlistName
    );

    if (Object.hasOwn(response, 'message')) {
        showErrorDialog(
            `Error: El servidor no encontro la playlist ${playlistName}!`
        );
    }
    else {
        activePlaylist = playlistName;
        renderPlaylist(response, withAdd, withRemove);
    }
}

async function getMusic(title) {
    let response = await reportOp(
        'get_music',
        ['Library', title]
    );

    if (Object.hasOwn(response, 'message')) {
        showErrorDialog(
            `No se encontro la cancion ${title} en la playlist Library`

        );
    }
    else {
        return response;
    }
}

async function addMusic(playlist, title, author, direction) {
    let response = await reportOp(
        'add_music',
        [
            playlist,
            {
                title : title,
                author : author,
                direction : direction
            }
        ]
    );

    if (response['message'] !== 'Success!') {
        showErrorDialog(
            `Error: No se encontro la playlist ${playlist} o la cancion `
            + `${title} ya esta en la Libreria!`
        );
    }
}

async function addSelectedMusic() {
    let selectedMusic = document.getElementsByClassName('add-selected');

    for (let musicElement of selectedMusic) {
        let title = musicElement.attributes[1].nodeValue;
        let music = await getMusic(title);

        addMusic(activePlaylist, music['title'], music['author'], music['direction']);
    }

    let playlist = await getPlaylist(activePlaylist);
    renderPlaylist(playlist);
}

async function removeMusic(playlist, title) {
    let response = await reportOp(
        'remove_music',
        [playlist, title]
    );

    if (response['message'] !== 'Success!') {
        console.log(
            `Error: Song ${title} not found in playlist ${playlist}!`
        );
        showErrorDialog(
            `Error: La cancion ${title} no se encontro en la playlist ${playlist}`
        );
    }
}

async function setPlayMusic(playlist, title) {
    let response = await reportOp('play',[
        playlist,
        title
    ]);

    if (Object.hasOwn(response, 'message')) {
        showErrorDialog(
            `Error: Playlist ${playlist} or song ${title} not found!`
        );
    }
    else {
        playingPlaylist = playlist;
        playingTitle = response['title'];
        playingAuthor = response['author'];
        playingDir = response['direction'];
        finishPlaylist = false;
    }
}

async function setNextMusic(playlist) {
    let response = await reportOp('next',[
        playlist,
        loop
    ]);

    if (!Object.hasOwn(response, 'message')) {
        playingTitle = response['title'];
        playingAuthor = response['author'];
        playingDir = response['direction'];
        finishPlaylist = false;
    }
    else {
        finishPlaylist = true;
    }
}

async function setPrevMusic(playlist) {
    let response = await reportOp('prev',[
        playlist,
        loop
    ]);

    if (!Object.hasOwn(response, 'message')) {
        playingTitle = response['title'];
        playingAuthor = response['author'];
        playingDir = response['direction'];
        finishPlaylist = false;
    }
    else {
        finishPlaylist = true;
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

function showRemovePlaylistDialog(playlist) {
    let dialog = document.getElementById('remove-playlist-dialog');
    dialog.playlistName = playlist;

    let label = document.getElementById('remove-playlist-dialog-label');
    label.value = `Serguro que quiere borrar ${playlist}?`;

    dialog.show();
}

function showAddMusicDialog() {
    createAddMusicDialog();
    let dialog = document.getElementById('add-music-dialog');
    dialog.show();
    renderLibraryList();
}

function switchAddMusicState(musicName) {
    let article = document.getElementById('add-' + musicName);
    if (article.className === 'add-selected') {
        article.className = 'add-unselected';
    }
    else {
        article.className = 'add-selected';
    }

    let Label = document.getElementById(musicName + 'add-selected-label');
    if (Label !== null) {
        Label.setAttribute('id', musicName + 'add-unselected-label');
        Label.setAttribute('class', 'add-unselected-label');
    }
    else {

        Label = document.getElementById(musicName + 'add-unselected-label');
        if (Label !== null) {
            Label.setAttribute('id', musicName + 'add-selected-label');
            Label.setAttribute('class', 'add-selected-label');
        }
    }

    let Button = document.getElementById(musicName + 'add-selected-button');
    if (Button !== null) {
        Button.setAttribute('id', musicName + 'add-unselected-button');
        Button.className = 'add-unselected-button';
        Button.value = 'agregar';
    }
    else {

        Button = document.getElementById(musicName + 'add-unselected-button');
        if (Button !== null) {
            Button.id = musicName + 'add-selected-button';
            Button.className = 'add-selected-button';
            Button.value = 'quitar';
        }
    }

}

function showRemoveMusicDialog() {
    let dialog = document.getElementById('remove-music-dialog');

    //  set label
    let label = document.getElementById(dialog.id + '-label');
    label.value = `Seguro que quires eliminar ${activePlaylist + '-' + activeAuthor}?`

    dialog.show();
}

async function setAudio() {
    let temp = document.getElementById('track');
    if (temp !== null) {
        temp.remove();
    }
    let track = document.createElement('audio');
    track.id = 'track';
    track.src = '/mp3/' + playingDir;
    track.load();
    updateTimer = setInterval(seekUpdate, 1000);
    track.ondurationchange = function() { 
        let durationLabel = document.querySelector('.music-player-length-time');
        let durationMinutes = Math.floor(track.duration / 60);
        let durationSeconds = Math.floor(track.duration - durationMinutes * 60);

        if (durationMinutes < 10) { durationMinutes = '0' + durationMinutes; }
        if (durationSeconds < 10) { durationSeconds = '0' + durationSeconds; }

        durationLabel.value = durationMinutes + ':' + durationSeconds;
    }
    track.onended = function() {
        nextMusic(playingPlaylist);
    }
    document.getElementById('body').append(track);
}

async function playMusic(playlist, title) {
    clearInterval(updateTimer);
    await setPlayMusic(playlist, title);

    await setAudio();

    renderMusicPlayer();

    document.getElementById('track').play();
}

async function nextMusic(playlist) {
    clearInterval(updateTimer);
    await setNextMusic(playlist);

    await setAudio();

    renderMusicPlayer();

    if (!finishPlaylist) {
        document.getElementById('track').play();
    }
}

async function prevMusic(playlist) {
    clearInterval(updateTimer);
    await setPrevMusic(playlist);

    await setAudio();

    renderMusicPlayer();

    if (!finishPlaylist) {
        document.getElementById('track').play();
    }
}

function playPause() {
    let button = document.querySelector('.play-button');
    let track = document.getElementById('track');
    if (button.value === playSymbol) {
        button.value = pauseSymbol;
        track.play();
    }
    else {
        button.value = playSymbol;
        track.pause();
    }
}

function seekUpdate() {
    let track = document.getElementById('track');
    let seekPosition = 0;
    let progressBar = document.getElementById('music-player-progress-bar');
    let currentTimeLabel = document.querySelector('.music-player-current-time');
    let durationLabel = document.querySelector('.music-player-length-time')
    if (!isNaN(track.duration)) {
        seekPosition = track.currentTime * (100 / track.duration);
        progressBar.value = seekPosition;

        let currentMinutes = Math.floor(track.currentTime / 60);
        let currentSeconds = Math.floor(track.currentTime - currentMinutes * 60);

        if (currentMinutes < 10) { currentMinutes = '0' + currentMinutes; }
        if (currentSeconds < 10) { currentSeconds = '0' + currentSeconds; }

        currentTimeLabel.value = currentMinutes + ':' + currentSeconds;

    }
}

function seekTo() {
    let track = document.getElementById('track');

    let progress = document.getElementById('music-player-progress-bar').value;
    let position = track.duration * (progress / 100);

    track.currentTime = position;
}

//  Rendering
function createButton(parent, className, value, event) {
    let button = document.createElement('input');

    button.id = parent + className;
    button.type = 'button';
    button.className = className;
    button.value = value;
    if (event !== null) {
        button.onclick = event;
    }

    return button;
}

function createRemoveButton(event) {
    let button = document.createElement('div');
    button.className = 'remove-button';
    button.onclick = event;

    let image = document.createElement('img');
    image.src = trashPath;
    image.className = 'remove-img';

    button.append(image);
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

function createPlaylistElement(playlist, withRemove = true, withAdd = true) {
    let playlistElement = document.createElement('article');
    playlistElement.id = playlist;
    playlistElement.className = 'playlist-element'

    let playlistButton = createButton(
        playlist, 
        'playlist-button',
        playlist,
        function (){ displayPlaylist(playlist, withAdd, withRemove); }
    );

    let removeButton = null;
    if (withRemove) {
        removeButton = createRemoveButton(
            function() { showRemovePlaylistDialog(playlist); }
        );
    }

    playlistElement.append(playlistButton);
    if (withRemove) {
        playlistElement.append(removeButton);
    }

    return playlistElement;
}

function createMusicElement(title, author, withRemove = true) {
    let musicElement = document.createElement('article');
    musicElement.id = title + '-' + author;
    musicElement.className = 'music-element';

    let label = createLabel(
        title + '-' + author,
        '-label',
        title + ' Por ' + author
    )

    let removeButton = null;
    if (withRemove) {
        removeButton = createRemoveButton(
            function() {
                activeTitle = title;
                activeAuthor = author;
                showRemoveMusicDialog();
            }
        );
    }
    
    let playButton = createButton(
        title + '-' + author,
        '-play-button',
        playSymbol,
        async function (){
            activeTitle = title;
            playMusic(activePlaylist, title);
        }  
    )

    musicElement.append(label);
    if (withRemove) {
        musicElement.append(removeButton);
    }
    musicElement.append(playButton);
    
    return musicElement;
}

/*
 *  the class 'add-selected-button' and 'add-selected-label' 
 *  represents a selected song.
 *  the class 'add-unselected-button' and 'add-unselected-label' 
 *  represents a selected song.
 */
function createAddMusicElement(title, author) {
    let musicElement = document.createElement('article');
    musicElement.id = 'add-' + title + '-' + author;
    musicElement.setAttribute('data-title', title);
    musicElement.setAttribute('data-author', author);

    let label = createLabel(
        title + '-' + author,
        'add-unselected-label',
        title + ' Por ' + author
    )

    let addButton = createButton(
        title + '-' + author,
        'add-unselected-button',
        'agregar',
        function (){ 
            switchAddMusicState(title + '-' + author); 
        }
    )

    musicElement.append(label);
    musicElement.append(addButton);
    
    return musicElement;
}

function createAddMusicDialog() {
    let temp = document.getElementById('add-music-dialog');
    if (temp !== null) {
        temp.remove();
    }
    let dialog = document.createElement('dialog');
    dialog.id = 'add-music-dialog';

    //  exit button
    let exitButton = createButton(
        dialog.id,
        '-exit-button',
        'X',
        function () {
            dialog.close();
        }
    );

    //  label
    let label = createLabel(
        dialog.id,
        '-label',
        'Elige las canciones para tu nueva playlist!'
    );

    //  save button
    let saveButton = createButton(
        dialog.id,
        '-save-button',
        'Guardar',
        function () {
            dialog.close();
            addSelectedMusic();
        }
    );

    //  add elements
    dialog.append(exitButton);
    dialog.append(label);
    dialog.append(saveButton);

    //  add to the DOM
    let body = document.getElementById('body');
    body.append(dialog);
}

function renderPlaylist(playlist, addButton = true, withRemove = true) {
    //  create the playlist 
    let musicListTemp = document.getElementById('music-list');
    if (musicListTemp !== null) {
        musicListTemp.remove();
    }
    let musicList = document.createElement('div');
    musicList.id = 'music-list';
    //  addButton
    if (addButton) {
        let buttonAdd = createButton(
            playlist, 'add-button', '+', function () {
                showAddMusicDialog();
            }
        );
        musicList.append(buttonAdd);
    }
    //  Render each music
    for (let music of playlist) {
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

        let withAdd = true;
        if (playlist === 'Library') {
            withRemove = false;
            withAdd = false;
        }
        let playlistElement = createPlaylistElement(playlist, withRemove, withAdd);
        if (playlist === 'Library') {
            playlsitList.prepend(playlistElement);
        }
        else {
            playlsitList.append(playlistElement);
        }
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
    renderPlaylist(library['Library'], false, false);
}

async function renderLibraryList() {
    let response = await reportOp('get_playlist', 'Library');

    if (Object.hasOwn(response, 'message')) {
        showErrorDialog(
            `Error: El servidor no encontro la Libreria!`
        );
    }
    else {
        let dialog = document.getElementById('add-music-dialog');
        for (let music of response) {
            dialog.append(createAddMusicElement(
                music['title'],
                music['author']
            ));
        }
    }
}

/**
 * Music Player Plan:
 *  Phase 1: First Load
 *      - Render the music player.
 *      - Load the audio.
 *      - Set initial indicators values. X
 *      - Play the selected track.
 * 
 *  Phase 2: Controls
 *      - Exit Button:
 *          - Close the music player.
 *          - Stop the current track.
 * 
 *      - Bar:
 *          - Show the current progress.
 *          - Seek to in the current track.
 *          - Update the indicators values.
 * 
 *      - Prev Button:
 *          - Load the previous track.
 *          - Play the previous track.
 *          - Update indicators and labels.
 * 
 *      - Play Button:
 *          - Pause/Play the current track.
 * 
 *      - Next Button:
 *          - Load the next track.
 *          - Play the next track.
 *          - Update indicators and labels.
 * 
 * 
 *  Phase 3: Automatics
 *      - Update indicators when track is playing.
 *      - Play next track when the current track ends.
 * 
 * OPS:
 * 
 * 
 */

function createMusicPlayer() {
    let temp = document.getElementById('music-player');
    if (temp !== null) {
        temp.remove();
    }

    let musicPlayer = document.createElement('article');
    musicPlayer.id = 'music-player';

    let head = document.createElement('div');
    head.id = 'music-player-head';

    let headLabel = createLabel(
        head.id,
        'label',
        playingTitle + ' Por ' + playingAuthor
    )

    let headExitButton = createButton(
        head.id,
        'exit-button',
        'X',
        function () {
            clearInterval(updateTimer);
            musicPlayer.remove();
            document.getElementById('track').pause()
            document.documentElement.style.setProperty('--content-height', '100vh');
        }
    )

    head.append(headLabel);
    head.append(headExitButton);

    let indicadors = document.createElement('div');
    indicadors.id = 'music-player-indicators';

    let currenTimeLabel = createLabel(
        indicadors.id,
        'music-player-current-time',
        '00:00'
    );

    let progressBar = document.createElement('input');
    progressBar.id = 'music-player-progress-bar';
    progressBar.type = 'range';
    progressBar.min = 0;
    progressBar.max = 100;
    progressBar.value = 0;
    progressBar.onchange = function() { seekTo(); };

    let lengthTimeLabel = createLabel(
        indicadors.id,
        'music-player-length-time',
        '00:00'
    );

    indicadors.append(currenTimeLabel);
    indicadors.append(progressBar);
    indicadors.append(lengthTimeLabel);

    let controls = document.createElement('div');
    controls.id = 'music-player-controls';

    let prevButton = createButton(
        controls.id,
        'prev-button',
        prevSymbol,
        function() { prevMusic(playingPlaylist); }
    );

    let playButtonSymbol = finishPlaylist? playSymbol: pauseSymbol;

    let playButton = createButton(
        controls.id,
        'play-button',
        playButtonSymbol,
        playPause
    );

    let nextButton = createButton(
        controls.id,
        'next-button',
        nextSymbol,
        function() { 
            nextMusic(playingPlaylist); 
        }
    );

    let loopToggleSymbol = loop? loopSymbol: playThroughSymbol;
    let loopToggle = document.createElement('div');
    loopToggle.className = 'loop-toggle';

    let loopImage = document.createElement('img');
    loopImage.className = 'loop-img';
    loopImage.src = loop? loopPath: playThroughPath;

    loopToggle.onclick = function() {
        if (loop) {
            loop = false;
            loopImage.src = playThroughPath;
        }
        else {
            loop = true;
            loopImage.src = loopPath;
        }
    }

    loopToggle.append(loopImage);

    controls.append(prevButton);
    controls.append(playButton);
    controls.append(nextButton);
    controls.append(loopToggle);

    musicPlayer.append(head);
    musicPlayer.append(indicadors);
    musicPlayer.append(controls);

    document.getElementById('body').append(musicPlayer);
}

async function renderMusicPlayer() {
    document.documentElement.style.setProperty('--content-height', '80vh');
    createMusicPlayer();
}

//  initial setup
// Rendering Globals
let activePlaylist = 'Library';
let activeTitle;
let activeAuthor;
let activeDir;
let loop = false;
let finishPlaylist = false;
let prevSymbol = '\u25AE\u25C0';
let playSymbol = '\u25B6';
let pauseSymbol = '\u25AE\u25AE';
let nextSymbol = '\u25B6\u25AE';
let loopSymbol = "\uD83D\uDD01";
let playThroughSymbol = "\u21C4";

//  images
let trashPath = '/static/trash-light.png';
let darkTrash = '/static/trash-dark.png';
let lightTrash = '/static/trash-light.png';

let loopPath = '/static/loop-light.png';
let darkLoop = '/static/loop-dark.png';
let lightLoop = '/static/loop-light.png';

let playThroughPath = '/static/play-through-light.png';
let playThroughDark = '/static/play-through-dark.png';
let playThroughLight = '/static/play-through-light.png';

//  Track Globals
let playingPlaylist;
let playingTitle;
let playingAuthor;
let playingDir;
let updateTimer;
get().then((result) => renderLibrary(result));

//  Specific Events
//  add-playlist-dialog
document.getElementById('add-playlist-dialog-exit').onclick = function() {
    let dialog = document.getElementById('add-playlist-dialog');
    dialog.close();
}

document.getElementById('add-playlist-dialog-save').onclick = async function() {
    let dialog = document.getElementById('add-playlist-dialog');
    let input = document.getElementById('add-playlist-dialog-input');
    let newPlaylist = input.value;
    input.value = '';
    dialog.close();
    addPlaylist(newPlaylist);
    activePlaylist = newPlaylist;
    let playlist = await getPlaylist(newPlaylist);
    renderPlaylist(playlist);
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

//  remove-playlist-dialog
document.getElementById('remove-playlist-dialog-remove-button').onclick = function () {
    let dialog = document.getElementById('remove-playlist-dialog');

    removePlaylist(dialog.playlistName);

    dialog.close();
}

document.getElementById('remove-playlist-dialog-cancel-button').onclick = function () {
    let dialog = document.getElementById('remove-playlist-dialog');
    dialog.close();
}

//  remove-music-dialog
document.getElementById('remove-music-dialog-remove-button').onclick = async function () {
    let dialog = document.getElementById('remove-music-dialog');

    let state = removeMusic(activePlaylist, activeTitle);
    if (state) {
        document.getElementById(activeTitle + '-' + activeAuthor).remove();
    }

    dialog.close();
}

document.getElementById('remove-music-dialog-cancel-button').onclick = function () {
    let dialog = document.getElementById('remove-music-dialog');
    dialog.close();
}

//  toggle-theme
document.getElementById('toggle-theme').onclick = function() {
    let toggle = document.getElementById('toggle-theme');
    let body = document.getElementById('body');
    if (toggle.value === '\u{25CF}') {
        toggle.value = '\u{25CB}';
        body.className = 'light';
        trashPath = darkTrash;
        loopPath = darkLoop;
        playThroughPath = playThroughDark;
    }
    else {
        toggle.value = '\u{25CF}';
        body.className = 'dark';
        trashPath = lightTrash;
        loopPath = lightLoop;
        playThroughPath = playThroughLight;
    }
    let removeImages = document.getElementsByClassName('remove-img');
    for (let image of removeImages) {
        image.src = trashPath;
    }

    let loopImages = document.getElementsByClassName('loop-img');
    for (let image of loopImages) {
        image.src = loop? loopPath: playThroughPath;
    }
}