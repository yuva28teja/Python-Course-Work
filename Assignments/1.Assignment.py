# ---------------- Ganna Music App Information System ----------------

# Song Details
song_id = int(input("Enter Song ID: "))                  # int
song_name = input("Enter Song Name: ")                   # str
artist_name = input("Enter Artist Name: ")              # str
album_name = input("Enter Album Name: ")                # str
duration_min = float(input("Enter Duration (in minutes): "))  # float

genres = input("Enter Genres (comma-separated): ").split(",")  # list

plays_count = int(input("Enter Number of Plays: "))    # int
likes_count = int(input("Enter Number of Likes: "))    # int
stats = (plays_count, likes_count)                     # tuple

popularity_percentage = float(input("Enter Popularity Percentage: "))  # float

tags = set(input("Enter Song Tags (comma-separated): ").split(","))    # set

publisher_name = input("Enter Publisher Name: ")       # str
publisher_contact = input("Enter Publisher Contact Number: ")  # str
publisher_location = input("Enter Publisher Location: ")  # str

publisher_details = {  # dict
    "name": publisher_name,
    "contact": publisher_contact,
    "location": publisher_location
}

print("\n=========== GANNA MUSIC APP DETAILS ===========\n")

# 1. Using Comma Separation (sep=',')
print("Song ID, Name, Artist:", song_id, song_name, artist_name, sep=", ")

# 2. Using Percentage Formatting (% operator)
print("Popularity: %.2f%%" % popularity_percentage)

# 3. Using f-strings
print(f"Song Name: {song_name}")
print(f"Artist: {artist_name}")
print(f"Album: {album_name}")
print(f"Duration: {duration_min} minutes")
print(f"Plays: {stats[0]}")
print(f"Likes: {stats[1]}")
print(f"Genres: {genres}")
print(f"Tags: {tags}")

# 4. Using .format() method
print("Publisher Details: Name - {}, Contact - {}, Location - {}"
      .format(publisher_details['name'], publisher_details['contact'], publisher_details['location']))

# ------------------------- SAMPLE OUTPUT -------------------------
# Enter Song ID: 101
# Enter Song Name: Shape of You
# Enter Artist Name: Ed Sheeran
# Enter Album Name: Divide
# Enter Duration (in minutes): 4.5
# Enter Genres (comma-separated): Pop,Dance
# Enter Number of Plays: 100000
# Enter Number of Likes: 80000
# Enter Popularity Percentage: 95
# Enter Song Tags (comma-separated): Top Hit,Trending
# Enter Publisher Name: Sony Music
# Enter Publisher Contact Number: 1234567890
# Enter Publisher Location: USA
#
# =========== GANNA MUSIC APP DETAILS ===========
#
# Song ID, Name, Artist: 101, Shape of You, Ed Sheeran
# Popularity: 95.00%
# Song Name: Shape of You
# Artist: Ed Sheeran
# Album: Divide
# Duration: 4.5 minutes
# Plays: 100000
# Likes: 80000
# Genres: ['Pop', 'Dance']
# Tags: {'Trending', 'Top Hit'}
# Publisher Details: Name - Sony Music, Contact - 1234567890, Location - USA
