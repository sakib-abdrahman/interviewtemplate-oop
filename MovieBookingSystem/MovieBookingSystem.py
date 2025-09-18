class MovieBookingSystem:
    def __init__(self):
        pass

    def addMovie(self, title: str, total_seats: int) -> str:
        """
        Adds a new movie to the system with the specified title and total seats.
        Returns the movie ID as a string.
        """

        pass

    def bookSeats(self, movie_id: str, num_seats: int) -> str:
        """
        Books the specified number of seats for a movie.
        Returns the booking ID as a string.
        """

        pass

    def cancelBooking(self, booking_id: str) -> int:
        """
        Cancels a booking and releases the seats back to the movie.
        Returns the number of available seats for the movie after cancellation.
        """

        pass

    def getMovieList(self) -> list:
        """
        Returns a list of all movies currently in the system.
        Each movie is represented as a dictionary with keys:
        - 'movie_id': str
        - 'title': str
        - 'total_seats': int
        - 'available_seats': int
        """

        pass