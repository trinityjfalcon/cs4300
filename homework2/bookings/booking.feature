Feature: Movie Theater Booking

    Scenario: User views movie list
        Given I am on the homepage
        Then I should see the list of movies page

    Scenario: User books an available seat
        Given I am a logged in user
        And there is a movie with an available seat
        When I book the seat
        Then the seat should be marked as unavailable
        And a booking should be created
        And a booking displays in booking history page

    Scenario: User vies booking history
        Given I am a logged in user
        And I have an existing booking
        When I visit the booking history page
        Then I should see my booking