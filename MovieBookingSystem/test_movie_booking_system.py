import unittest
from MovieBookingSystem import MovieBookingSystem


class TestMovieBookingSystem(unittest.TestCase):

    def setUp(self):
        self.booking_system = MovieBookingSystem()

    def test_01_addMovie_success(self):
        movie_id = self.booking_system.addMovie("Avengers", 100)
        self.assertIsNotNone(movie_id)
        self.assertIsInstance(movie_id, str)
        # Test that movie can be used for booking
        booking_id = self.booking_system.bookSeats(movie_id, 10)
        self.assertIsNotNone(booking_id)

    def test_02_addMovie_multiple_movies(self):
        movie1 = self.booking_system.addMovie("Movie1", 100)
        movie2 = self.booking_system.addMovie("Movie2", 200)
        # Movies should be different
        self.assertNotEqual(movie1, movie2)
        # Both movies should work independently
        booking1 = self.booking_system.bookSeats(movie1, 10)
        booking2 = self.booking_system.bookSeats(movie2, 20)
        self.assertIsNotNone(booking1)
        self.assertIsNotNone(booking2)

    def test_03_addMovie_title_with_special_chars(self):
        movie_id = self.booking_system.addMovie("Spider-Man: No Way Home", 150)
        self.assertIsNotNone(movie_id)

    def test_04_addMovie_title_with_numbers(self):
        movie_id = self.booking_system.addMovie("Fast & Furious 9", 120)
        self.assertIsNotNone(movie_id)

    def test_05_addMovie_very_long_title(self):
        long_title = "A" * 200
        movie_id = self.booking_system.addMovie(long_title, 100)
        self.assertIsNotNone(movie_id)

    def test_06_addMovie_title_with_leading_trailing_spaces(self):
        movie_id = self.booking_system.addMovie("  Inception  ", 100)
        self.assertIsNotNone(movie_id)

    def test_07_addMovie_large_seat_count(self):
        movie_id = self.booking_system.addMovie("IMAX Movie", 500)
        # Verify by booking seats
        booking_id = self.booking_system.bookSeats(movie_id, 100)
        self.assertIsNotNone(booking_id)

    def test_08_addMovie_single_seat(self):
        movie_id = self.booking_system.addMovie("Private Screening", 1)
        # Verify by booking the only seat
        booking_id = self.booking_system.bookSeats(movie_id, 1)
        self.assertIsNotNone(booking_id)

    def test_09_addMovie_sequential_ids(self):
        movies = []
        for i in range(5):
            movie = self.booking_system.addMovie(f"Movie{i}", 100)
            movies.append(movie)
        # All movies should be unique
        self.assertEqual(len(set(movies)), 5)

    def test_10_bookSeats_success(self):
        movie_id = self.booking_system.addMovie("Movie", 100)
        booking_id = self.booking_system.bookSeats(movie_id, 10)
        self.assertIsNotNone(booking_id)
        self.assertIsInstance(booking_id, str)

    def test_11_bookSeats_exact_available_seats(self):
        movie_id = self.booking_system.addMovie("Movie", 50)
        booking_id = self.booking_system.bookSeats(movie_id, 50)
        self.assertIsNotNone(booking_id)

    def test_12_bookSeats_multiple_bookings(self):
        movie_id = self.booking_system.addMovie("Movie", 100)
        booking1 = self.booking_system.bookSeats(movie_id, 20)
        booking2 = self.booking_system.bookSeats(movie_id, 30)
        # Bookings should be different
        self.assertNotEqual(booking1, booking2)

    def test_13_bookSeats_single_seat(self):
        movie_id = self.booking_system.addMovie("Movie", 100)
        booking_id = self.booking_system.bookSeats(movie_id, 1)
        self.assertIsNotNone(booking_id)

    def test_14_bookSeats_sequential_booking_ids(self):
        movie_id = self.booking_system.addMovie("Movie", 100)
        bookings = []
        for i in range(5):
            booking = self.booking_system.bookSeats(movie_id, 5)
            bookings.append(booking)
        # All bookings should be unique
        self.assertEqual(len(set(bookings)), 5)

    def test_15_bookSeats_after_partial_booking(self):
        movie_id = self.booking_system.addMovie("Movie", 100)
        self.booking_system.bookSeats(movie_id, 30)
        # Should still be able to book more
        booking_id = self.booking_system.bookSeats(movie_id, 20)
        self.assertIsNotNone(booking_id)

    def test_16_cancelBooking_success(self):
        movie_id = self.booking_system.addMovie("Movie", 100)
        booking_id = self.booking_system.bookSeats(movie_id, 20)
        available_seats = self.booking_system.cancelBooking(booking_id)
        # Should return an integer (available seats)
        self.assertIsInstance(available_seats, int)
        self.assertGreaterEqual(available_seats, 20)

    def test_17_cancelBooking_restore_all_seats(self):
        movie_id = self.booking_system.addMovie("Movie", 50)
        booking_id = self.booking_system.bookSeats(movie_id, 50)
        available_seats = self.booking_system.cancelBooking(booking_id)
        self.assertEqual(available_seats, 50)

    def test_18_cancelBooking_partial_restoration(self):
        movie_id = self.booking_system.addMovie("Movie", 100)
        booking1 = self.booking_system.bookSeats(movie_id, 30)
        booking2 = self.booking_system.bookSeats(movie_id, 20)
        available_seats = self.booking_system.cancelBooking(booking1)
        # Should have 80 seats available (100 - 20 still booked)
        self.assertEqual(available_seats, 80)

    def test_19_cancelBooking_single_seat(self):
        movie_id = self.booking_system.addMovie("Movie", 100)
        booking_id = self.booking_system.bookSeats(movie_id, 1)
        available_seats = self.booking_system.cancelBooking(booking_id)
        self.assertEqual(available_seats, 100)

    def test_20_cancelBooking_multiple_cancellations(self):
        movie_id = self.booking_system.addMovie("Movie", 100)
        booking1 = self.booking_system.bookSeats(movie_id, 20)
        booking2 = self.booking_system.bookSeats(movie_id, 30)
        self.booking_system.cancelBooking(booking1)
        available_seats = self.booking_system.cancelBooking(booking2)
        self.assertEqual(available_seats, 100)

    def test_21_multiple_movies_isolation(self):
        movie1 = self.booking_system.addMovie("Movie1", 100)
        movie2 = self.booking_system.addMovie("Movie2", 200)
        booking1 = self.booking_system.bookSeats(movie1, 30)
        booking2 = self.booking_system.bookSeats(movie2, 50)
        # Canceling one shouldn't affect the other
        self.booking_system.cancelBooking(booking1)
        # Movie2 should still have booking2 active
        self.assertIsNotNone(booking2)

    def test_22_booking_workflow_complete(self):
        movie_id = self.booking_system.addMovie("Action Movie", 100)
        booking1 = self.booking_system.bookSeats(movie_id, 25)
        booking2 = self.booking_system.bookSeats(movie_id, 35)
        # Cancel first booking
        available_seats = self.booking_system.cancelBooking(booking1)
        self.assertEqual(available_seats, 65)

    def test_23_stress_test_many_movies(self):
        movies = []
        for i in range(20):
            movie = self.booking_system.addMovie(f"Movie{i}", 100)
            movies.append(movie)
        # All movies should be unique
        self.assertEqual(len(set(movies)), 20)

    def test_24_stress_test_many_bookings(self):
        movie_id = self.booking_system.addMovie("Popular Movie", 100)
        bookings = []
        for i in range(10):
            booking = self.booking_system.bookSeats(movie_id, 1)
            bookings.append(booking)
        # All bookings should be unique
        self.assertEqual(len(set(bookings)), 10)

    def test_25_edge_case_book_cancel_rebook(self):
        movie_id = self.booking_system.addMovie("Movie", 50)
        booking1 = self.booking_system.bookSeats(movie_id, 50)
        self.booking_system.cancelBooking(booking1)
        # Should be able to book again
        booking2 = self.booking_system.bookSeats(movie_id, 30)
        self.assertIsNotNone(booking2)

    def test_26_booking_data_integrity(self):
        movie_id = self.booking_system.addMovie("Movie", 100)
        booking_id = self.booking_system.bookSeats(movie_id, 25)
        # Booking should be valid for cancellation
        available_seats = self.booking_system.cancelBooking(booking_id)
        self.assertIsInstance(available_seats, int)

    def test_27_movie_seat_consistency(self):
        movie_id = self.booking_system.addMovie("Consistent Movie", 150)
        # Multiple operations shouldn't break the movie
        booking1 = self.booking_system.bookSeats(movie_id, 50)
        booking2 = self.booking_system.bookSeats(movie_id, 25)
        self.booking_system.cancelBooking(booking1)
        # Should still be able to book
        booking3 = self.booking_system.bookSeats(movie_id, 30)
        self.assertIsNotNone(booking3)

    def test_28_booking_id_type_consistency(self):
        movie_id = self.booking_system.addMovie("Movie", 100)
        booking_id = self.booking_system.bookSeats(movie_id, 10)
        self.assertIsInstance(booking_id, str)

    def test_29_movie_id_type_consistency(self):
        movie_id = self.booking_system.addMovie("Movie", 100)
        self.assertIsInstance(movie_id, str)

    def test_30_cancel_booking_return_value(self):
        movie_id = self.booking_system.addMovie("Movie", 100)
        booking_id = self.booking_system.bookSeats(movie_id, 30)
        returned_seats = self.booking_system.cancelBooking(booking_id)
        # Should return integer representing available seats
        self.assertIsInstance(returned_seats, int)
        self.assertGreaterEqual(returned_seats, 30)

    def test_31_empty_system_state(self):
        empty_system = MovieBookingSystem()
        # Should be able to add movies immediately
        movie_id = empty_system.addMovie("First Movie", 100)
        self.assertIsNotNone(movie_id)

    def test_32_title_preservation(self):
        special_title = "Avengers: Endgame (2019) - IMAX 3D"
        movie_id = self.booking_system.addMovie(special_title, 100)
        self.assertIsNotNone(movie_id)

    def test_33_unicode_title_support(self):
        unicode_title = "映画タイトル"
        movie_id = self.booking_system.addMovie(unicode_title, 100)
        self.assertIsNotNone(movie_id)

    def test_34_large_seat_operations(self):
        movie_id = self.booking_system.addMovie("Mega Theater", 10000)
        booking_id = self.booking_system.bookSeats(movie_id, 5000)
        available = self.booking_system.cancelBooking(booking_id)
        self.assertEqual(available, 10000)

    def test_35_alternating_book_cancel_pattern(self):
        movie_id = self.booking_system.addMovie("Pattern Movie", 100)
        for i in range(5):
            booking = self.booking_system.bookSeats(movie_id, 10)
            self.booking_system.cancelBooking(booking)
        # Should still be able to book after all cancellations
        final_booking = self.booking_system.bookSeats(movie_id, 50)
        self.assertIsNotNone(final_booking)

    def test_36_multiple_movies_booking_isolation(self):
        movie1 = self.booking_system.addMovie("Movie A", 100)
        movie2 = self.booking_system.addMovie("Movie B", 200)
        booking1 = self.booking_system.bookSeats(movie1, 50)
        booking2 = self.booking_system.bookSeats(movie2, 75)

        # Cancel booking for movie1
        available1 = self.booking_system.cancelBooking(booking1)
        self.assertEqual(available1, 100)

        # Movie2 booking should still be active
        self.assertIsNotNone(booking2)

    def test_37_booking_system_state_consistency(self):
        movie_id = self.booking_system.addMovie("State Movie", 100)
        bookings = []

        # Make 10 bookings of 5 seats each
        for i in range(10):
            booking = self.booking_system.bookSeats(movie_id, 5)
            bookings.append(booking)

        # Cancel first 5 bookings
        for booking in bookings[:5]:
            self.booking_system.cancelBooking(booking)

        # Should have 75 seats available (100 - 25 still booked)
        # Verify by trying to book exactly that amount
        final_booking = self.booking_system.bookSeats(movie_id, 25)
        available = self.booking_system.cancelBooking(final_booking)
        self.assertEqual(available, 75)

    def test_38_complete_workflow_scenario(self):
        cinema = MovieBookingSystem()

        movie1 = cinema.addMovie("Blockbuster 1", 200)
        movie2 = cinema.addMovie("Indie Film", 50)
        movie3 = cinema.addMovie("Documentary", 100)

        booking1 = cinema.bookSeats(movie1, 75)
        booking2 = cinema.bookSeats(movie1, 50)
        booking3 = cinema.bookSeats(movie2, 30)
        booking4 = cinema.bookSeats(movie3, 25)

        # Cancel one booking
        available1 = cinema.cancelBooking(booking2)
        self.assertEqual(available1, 125)  # 200 - 75 remaining booked

        # Try to book more seats
        booking5 = cinema.bookSeats(movie1, 100)
        self.assertIsNotNone(booking5)

        # Verify we can't overbook (should have 25 seats left)
        # This tests the seat availability logic indirectly
        remaining_seats = cinema.cancelBooking(booking5)
        self.assertEqual(remaining_seats, 125)

    def test_39_booking_cancellation_restores_exact_seats(self):
        movie_id = self.booking_system.addMovie("Exact Test", 100)

        # Book different amounts
        booking1 = self.booking_system.bookSeats(movie_id, 15)
        booking2 = self.booking_system.bookSeats(movie_id, 23)
        booking3 = self.booking_system.bookSeats(movie_id, 7)

        # Cancel middle booking
        available = self.booking_system.cancelBooking(booking2)
        # Should have 100 - 15 - 7 = 78 available
        self.assertEqual(available, 78)

    def test_40_sequential_operations_maintain_consistency(self):
        movie_id = self.booking_system.addMovie("Sequential Test", 200)

        # Perform a series of operations
        b1 = self.booking_system.bookSeats(movie_id, 50)
        b2 = self.booking_system.bookSeats(movie_id, 30)
        self.booking_system.cancelBooking(b1)
        b3 = self.booking_system.bookSeats(movie_id, 40)
        available = self.booking_system.cancelBooking(b2)

        # Should have 200 - 40 = 160 available (only b3 remains)
        self.assertEqual(available, 160)

    def test_41_getMovieList_empty_system(self):
        movie_list = self.booking_system.getMovieList()
        self.assertIsInstance(movie_list, list)
        self.assertEqual(len(movie_list), 0)

    def test_42_getMovieList_single_movie(self):
        movie_id = self.booking_system.addMovie("Test Movie", 100)
        movie_list = self.booking_system.getMovieList()

        self.assertIsInstance(movie_list, list)
        self.assertEqual(len(movie_list), 1)

        movie = movie_list[0]
        self.assertIsInstance(movie, dict)
        self.assertIn('movie_id', movie)
        self.assertIn('title', movie)
        self.assertIn('total_seats', movie)
        self.assertIn('available_seats', movie)

        self.assertEqual(movie['movie_id'], movie_id)
        self.assertEqual(movie['title'], "Test Movie")
        self.assertEqual(movie['total_seats'], 100)
        self.assertEqual(movie['available_seats'], 100)

    def test_43_getMovieList_multiple_movies(self):
        movie1 = self.booking_system.addMovie("Movie 1", 100)
        movie2 = self.booking_system.addMovie("Movie 2", 200)
        movie3 = self.booking_system.addMovie("Movie 3", 150)

        movie_list = self.booking_system.getMovieList()

        self.assertEqual(len(movie_list), 3)

        # Extract movie IDs from the list
        movie_ids = [movie['movie_id'] for movie in movie_list]
        self.assertIn(movie1, movie_ids)
        self.assertIn(movie2, movie_ids)
        self.assertIn(movie3, movie_ids)

        # Verify all movies have correct structure
        for movie in movie_list:
            self.assertIn('movie_id', movie)
            self.assertIn('title', movie)
            self.assertIn('total_seats', movie)
            self.assertIn('available_seats', movie)

    def test_44_getMovieList_after_bookings(self):
        movie_id = self.booking_system.addMovie("Booking Test", 100)
        self.booking_system.bookSeats(movie_id, 30)

        movie_list = self.booking_system.getMovieList()

        self.assertEqual(len(movie_list), 1)
        movie = movie_list[0]

        self.assertEqual(movie['movie_id'], movie_id)
        self.assertEqual(movie['title'], "Booking Test")
        self.assertEqual(movie['total_seats'], 100)
        self.assertEqual(movie['available_seats'], 70)

    def test_45_getMovieList_after_cancellations(self):
        movie_id = self.booking_system.addMovie("Cancellation Test", 100)
        booking_id = self.booking_system.bookSeats(movie_id, 40)
        self.booking_system.cancelBooking(booking_id)

        movie_list = self.booking_system.getMovieList()

        self.assertEqual(len(movie_list), 1)
        movie = movie_list[0]

        self.assertEqual(movie['available_seats'], 100)  # Should be back to full capacity

    def test_46_getMovieList_multiple_movies_with_bookings(self):
        movie1 = self.booking_system.addMovie("Action Movie", 150)
        movie2 = self.booking_system.addMovie("Comedy Movie", 120)
        movie3 = self.booking_system.addMovie("Drama Movie", 80)

        # Make bookings on different movies
        self.booking_system.bookSeats(movie1, 50)
        booking2 = self.booking_system.bookSeats(movie2, 30)
        self.booking_system.bookSeats(movie3, 20)

        # Cancel one booking
        self.booking_system.cancelBooking(booking2)

        movie_list = self.booking_system.getMovieList()
        self.assertEqual(len(movie_list), 3)

        # Find each movie and verify available seats
        movie_dict = {movie['movie_id']: movie for movie in movie_list}

        self.assertEqual(movie_dict[movie1]['available_seats'], 100)  # 150 - 50
        self.assertEqual(movie_dict[movie2]['available_seats'], 120)  # 120 - 30 + 30 (cancelled)
        self.assertEqual(movie_dict[movie3]['available_seats'], 60)   # 80 - 20

    def test_47_getMovieList_title_preservation(self):
        special_titles = [
            "Spider-Man: No Way Home",
            "Fast & Furious 9",
            "The Lord of the Rings",
            "映画タイトル",  # Unicode
            "Movie with    spaces",
            "A" * 50  # Long title
        ]

        for title in special_titles:
            self.booking_system.addMovie(title, 100)

        movie_list = self.booking_system.getMovieList()
        retrieved_titles = [movie['title'] for movie in movie_list]

        for title in special_titles:
            self.assertIn(title, retrieved_titles)

    def test_48_getMovieList_data_types(self):
        movie_id = self.booking_system.addMovie("Type Test", 100)
        movie_list = self.booking_system.getMovieList()

        movie = movie_list[0]

        self.assertIsInstance(movie['movie_id'], str)
        self.assertIsInstance(movie['title'], str)
        self.assertIsInstance(movie['total_seats'], int)
        self.assertIsInstance(movie['available_seats'], int)

    def test_49_getMovieList_immutability_check(self):
        movie_id = self.booking_system.addMovie("Immutable Test", 100)

        # Get movie list twice
        movie_list1 = self.booking_system.getMovieList()
        movie_list2 = self.booking_system.getMovieList()

        # Lists should contain the same data but be separate objects
        self.assertEqual(len(movie_list1), len(movie_list2))
        self.assertEqual(movie_list1[0]['movie_id'], movie_list2[0]['movie_id'])

        # Modifying one list shouldn't affect the other (if implementation is correct)
        if movie_list1:
            original_title = movie_list1[0]['title']
            movie_list1[0]['title'] = "Modified"

            movie_list3 = self.booking_system.getMovieList()
            self.assertEqual(movie_list3[0]['title'], original_title)

    def test_50_getMovieList_comprehensive_workflow(self):
        # Create multiple movies
        action_movie = self.booking_system.addMovie("Action Hero", 200)
        comedy_movie = self.booking_system.addMovie("Laugh Out Loud", 150)
        drama_movie = self.booking_system.addMovie("Tears of Joy", 100)

        # Perform various operations
        booking1 = self.booking_system.bookSeats(action_movie, 75)
        booking2 = self.booking_system.bookSeats(comedy_movie, 50)
        booking3 = self.booking_system.bookSeats(action_movie, 25)
        booking4 = self.booking_system.bookSeats(drama_movie, 30)

        # Cancel some bookings
        self.booking_system.cancelBooking(booking2)  # Comedy back to 150
        self.booking_system.cancelBooking(booking1)  # Action: 200 - 25 = 175

        # Get final movie list
        movie_list = self.booking_system.getMovieList()

        self.assertEqual(len(movie_list), 3)

        # Verify each movie's state
        movie_dict = {movie['movie_id']: movie for movie in movie_list}

        # Action movie: 200 total, 25 booked (booking3), 175 available
        self.assertEqual(movie_dict[action_movie]['total_seats'], 200)
        self.assertEqual(movie_dict[action_movie]['available_seats'], 175)

        # Comedy movie: 150 total, booking cancelled, 150 available
        self.assertEqual(movie_dict[comedy_movie]['total_seats'], 150)
        self.assertEqual(movie_dict[comedy_movie]['available_seats'], 150)

        # Drama movie: 100 total, 30 booked, 70 available
        self.assertEqual(movie_dict[drama_movie]['total_seats'], 100)
        self.assertEqual(movie_dict[drama_movie]['available_seats'], 70)


if __name__ == '__main__':
    unittest.main()