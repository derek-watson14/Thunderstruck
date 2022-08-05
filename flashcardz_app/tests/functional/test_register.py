"""
User registration page.
GET requests serve sign - up page.
POST requests validate form & user creation.
"""

# Pass test_client fixture as an argument into the test function
def test_register_get_with_fixture(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is request (GET)
    THEN check that the response is valid
    """
    response = client.get('/register')
    assert response.status_code == 200
    assert b'CREATE ACCOUNT' in response.data

# Pass test_client fixture as an argument into the test function
def test_register_post_with_fixture(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is posted to (POST)
    THEN check that '405' status code is returned
    """
    response = client.post('/register')
    assert response.status_code == 405
    assert b'CREATE ACCOUNT' not in response.data