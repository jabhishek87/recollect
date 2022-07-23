def test_main(test_app):
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to your beanie powered app!"
    }
