How to run:
    Open this link: https://movie-theater-booking-1f9z.onrender.com
    Use these credentials to log in
        Username: user
        Password: aPassword1
    To book a movie: 
        Click book now for your movie of choice
    Then choose a seat to book
    To view booked seat click "Booking History" in navigation bar

Project structure and purpose for each file:
    cs4300
        homework2                 ---> root directory
            bookings              ---> Django app containing models, views, and templates

                features          ---> BDD tests
                    steps
                        booking_steps.py
                    booking.feature
                    environment.py

                migrations

                templates
                    base.html              ---> base template with navigation bar
                    booking_history.html   ---> user booking history
                    login.html             ---> login page
                    movie_list.html        ---> homepage
                    seat_booking.html      ---> seat selection page

                __init__.py
                admin.py             ---> admin configuration
                apps.py
                models.py            ---> Movie, Seat, Booking models
                serializers.py       ---> DRF serializers
                tests.py             ---> Unit and integration tests
                urls.py              ---> URL routing
                views.py             ---> Template views and API ViewSets


            movie_theater_booking    ---> Django project settings
                __init__.py
                asgi.py
                settings.py
                urls.py
                wsgi.py

            (virtual environments)      ---> to run application and run tests
            behave.ini                  ---> BDD testing configuration
            build.sh                    ---> Render build script
            render.yaml                 ---> Render deployment configuration
            requirements.txt            ---> dependencies



Local Setup: (in terminal)
    1. Clone repository
        git clone https://github.com/trinityjfalcon/cs4300.git
        cd cs4300/homework2
    2. Create and activate virtual environment
        python3 -m venv myenv --system-site-packages
        source myenv/bin/activate
    3. Install dependencies
        pip install -r requirements.txt
    4. Run migrations:
        python3 manage.py migrate
    5. Create a superuser
        python3 manage.py createsuperuser
    6. Start server:
        python3 manage.py runserver 0.0.0.0:3000
    7. In your browser visit http://127.0.0.1:3000/
 
 How to run tests:
    1. Activate virtual environment
        source your_venv/bin/activate
    2. Navigate to homework2 folder
        cd cs4300/homework2
    3. For the unit and integration tests run this
        python3 manage.py test bookings
    4. BDD testing with behave
        python3 manage.py behave


Use of AI:
    Debug and figure out how to deploy on Render
        Helped with build.sh and debugging in settings.py after I followed the instructions on the given site

    Understanding serializers and looking at example but not to code

    Coded lines 15-17 in models.py (class BookingStatus ()) as I had done it incorrectly initially

    Helped debug testing as well as understanding BDD testing better