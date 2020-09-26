#Project 5
#Hunter Boone and Riley McNay
#December 3, 2019

def read_playlist(filename):
    """
    Input: filename of CSV file listing (song,artist,genre) triples
    Output: List of (song,artist,genre)
    """
    playlist = []
    for line in open(filename):
        bits = [b.strip() for b in line.split(',')]
        playlist.append(bits)
    return playlist

def playlist_transform(s,t,compareType="Song"):
    """
    Computes the edit distance for two playlists s and t, and prints the minimal edits 
      required to transform playlist s into playlist t.
      
    Inputs:
    s: 1st playlist (format: list of (track name, artist, genre) triples)
    t: 2nd playlist (format: list of (track name, artist, genre) triples)
    compareType: String indicating the type of comparison to make.
       "Song" (default): songs in a playlist are considered equivalent if the 
         (song name, artist, genre) triples match.
       "Genre": songs in a playlist are considered equivalent if the same genre is used.
       "Artist": songs in a playlist are considered equivalent if the same artist is used.
    Output: The minimum edit distance and the minimal edits required to transform playlist
      s into playlist t.
    """
    if compareType == "Song":
      type = 0
    elif compareType == "Artist":
      type = 1
    else:
      type = 2

    A, B = [], []
    s, t = [" "] + s, [" "] + t

    A.append(range(len(s) + 1))
    B.append(range(len(t) + 1))
    
    for i in range(len(s)):       #appends index from s to A
      A.append([i])
      B.append([4])
    for j in range(len(t)):       # appends index from t to A
      A.append([j])
      B.append([3])

    for i in range(1, len(s)):
        for j in range(1, len(t)):
            if type == 0:                   # if equal to a SONG
              if s[i] == t[j]:              # if songs are equal
                c_match = A[i-1][j-1]
                match = True
              else:
                c_match = A[i-1][j-1] + 1
                match = False
            else:                           # ARTIST or GENRE  
              if s[i][type] == t[j][type]:
                c_match = A[i-1][j-1]
                match = True
              else:
                c_match = A[i-1][j-1]+1
                match = False

            insert = A[i][j-1] + 1
            delete = A[i-1][j] + 1
            minimum = min(c_match, insert, delete)

            if minimum == c_match:
              if match:
                B[i].append(1)          #do not change
              else:
                B[i].append(2)          #change s[i] to t[j]
            elif minimum == insert:
              B[i].append(3)            #insert t[j]
            else:
              B[i].append(4)            #remove s[i]
            A[i].append(minimum)

    x = len(s)-1
    y = len(t)-1
    listt = []

    while x >= 0 or y >= 0:             # Printing out of operations
        if x == 0 and y == 0:
            break
        if B[x][y] == 1:
            a = "Leave " + str(s[x]) + " unaltered"
            listt.insert(0, a)
            x -= 1
            y -= 1
        elif B[x][y] == 2:
            b = "Change " + str(s[x]) + " to " + str(t[y])
            listt.insert(0, b)
            x -= 1
            y -= 1
        elif B[x][y] == 3:
            c = "Insert " + str(t[y])
            listt.insert(0, c)
            y -= 1
        elif B[x][y] == 4:
            d = "Remove " + str(s[x])
            listt.insert(0, d)
            x -= 1

    for k in range(0, len(listt)):
        print(listt[k])

    return A[len(s)-1][len(t)-1]


if __name__=="__main__":
    b1 = read_playlist("blues1.csv")
    b2 = read_playlist("blues2.csv")
    b3 = read_playlist("playlist1.csv")
    b4 = read_playlist("playlist2.csv")
    
    print("\nPlaylist 1:")
    for song in b1:
      print(song)

    print("\nPlaylist 2:")
    for song in b2:
      print(song)

    print("\nComparing playlist similarity by song:")
    playlist_transform(b1,b2)
    print("\nComparing playlist similarity by genre:")
    playlist_transform(b1,b2,"Genre")
    print("\nComparing playlist similarity by artist:")
    playlist_transform(b1,b2,"Artist")

    print("\nPlaylist 3:")
    for song in b3:
      print(song)

    print("\nPlaylist 4:")
    for song in b4:
      print(song)

    print("\nComparing playlist similarity by song:")
    playlist_transform(b3,b4)
    print("\nComparing playlist similarity by genre:")
    playlist_transform(b3,b4,"Genre")
    print("\nComparing playlist similarity by artist:")
    playlist_transform(b3,b4,"Artist")