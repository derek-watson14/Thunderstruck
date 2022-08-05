# Pass in new_user fixture as an argument into the function
# new_user was created in conftest.py
def test_new_user_with_fixture(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email and password_hashed fields are defined correctly
    """
    user = User(
        email='cool@test.edu'
    )
    user.set_password('testpassword')
    db.session.add(user)
    db.session.commit()

    print(f"new_user: {new_user}")
    # Confirm that the email is stored properly
    assert new_user.email == 'cool@test.edu'

    # Check that the hashed password does not = plaintext password
    assert new_user.password != 'testpassword'