# Movie Booking System
Design and implement a simple Movie Booking System. Your solution should include clean, extendable, and correct code that can handle the following requirements:

## Add Movies
Each movie has a title and a total number of seats.
When a movie is added, return a unique movie_id (string).
Multiple movies should be supported and operate independently.

## Book Seats
Given a movie_id and number of seats, book those seats if available.
Return a unique booking_id (string) for each successful booking.
Prevent overbooking: if not enough seats remain, booking should not succeed.

## Cancel Bookings
Given a booking_id, cancel the booking and restore the seats for that movie.
Return the number of available seats for the movie after cancellation.

## Report Available Movies
Provide a method to return a list of all movies currently in the system.
For each movie, include its movie_id, title, total seats, and available seats.