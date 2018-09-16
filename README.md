# three-characters
The availability of all three-character usernames on Reddit.

This shows how the number of three-character usernames left on Reddit decreased over time.

The method for obtaining the creation date of each account was slow and inefficient, and though I have found a better way of doing this, I included the original method for the sake of consistency. 

The total number of possible three-character usernames is 54,872. This is because Reddit accepts usernames with all alphanumeric characters as well as the hyphen and underscore. Reddit is case-insensitive so uppercase or lowercase does not matter. That totals to 26 letters, 10 digits, and 2 extra characters. With 38 possible characters for each position, the total number of possible usernames is 38^3, which equals 54,872.

You may notice however, that the graph starts below 50,000. The purpose of that is because there were 6,170 accounts that I could not obtain the creation date for. They were either deleted, suspended, or shadowbanned which resulted in their creation dates being removed from the public view. To deal with this I removed them from total number of accounts. This way you could still see the availability approaching zero.





