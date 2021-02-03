from song import Song

class Playlist:
  def __init__(self):
    # head
    self.__first_song = None


  # a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):

    # Creates a new song (node)
    new_song = Song(title)
    new_song.set_title(title)

    # Set next pointer to first song (node)
    new_song.set_next_song(self.__first_song)
    self.__first_song = new_song
    print("song successfully added.")


  # a method called find_song that searches for whether a song exits in the playlist and returns its index. The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.

  def find_song(self, title):
    # Assigns first song (node) as head
    current_song = self.__first_song
    # intizalizes an index counter
    index = 0

    # loops until it finds the song (node) or reaches the end of the playlist (linked list)
    while current_song.get_title() != None:
      # returns the index if it finds the song
      if current_song.get_title() == title:
        return index
      # Traverses to the next song (node) in the playlist (linked list)
      current_song = current_song.get_next_song()
      # increments index counter
      index += 1
    return -1


  # a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):

    # removes node if at the head
    if self.__first_song.get_title() == title:
      self.__first_song = self.__first_song.get_next_song()
      print("song successfully removed.")
      return

    # setting up two pointers (current and previous song)
    previous_song = None
    current_song = self.__first_song

    # continously moves pointers until reaches specified song or end of the playlist
    while current_song.get_title() != title:
      previous_song = current_song
      current_song = current_song.get_next_song()
      # function fails if song doesn't exist in the list
      if current_song == None:
        print("song does not exist, no song has been removed.")
        return

    # song removed
    previous_song.set_next_song(current_song.get_next_song())
    print("song successfully removed.")


  # a method called length, which returns the number of songs in the playlist.

  def length(self):
    current_song = self.__first_song
    counter = 0

    # loop traverses through the playlist (linked list) and increments counter every song (node)
    while current_song != None:
      counter += 1
      current_song = current_song.get_next_song()
    return counter


  # a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    current_song = self.__first_song
    song_num = 1

    # loop traverses through the playlist (linked list) and prints out every song (node)
    while current_song != None:
      print(f'{song_num}. {current_song}')
      current_song = current_song.get_next_song()
      song_num += 1
    