from app import app

def test_app():
    tester = app.test_client()
    response = tester.get("/")
    assert response.status_code == 200
    assert b"Hello, this is CI/CD beginning"

