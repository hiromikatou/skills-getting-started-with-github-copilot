from fastapi.testclient import TestClient

from src.app import app, activities


client = TestClient(app)


def setup_function():
    activities["Chess Club"]["participants"] = [
        "michael@mergington.edu",
        "daniel@mergington.edu",
    ]


def test_unregister_participant_removes_student_from_activity():
    response = client.delete(
        "/activities/Chess Club/unregister?email=michael@mergington.edu"
    )

    assert response.status_code == 200
    assert "michael@mergington.edu" not in activities["Chess Club"]["participants"]


def test_unregister_returns_404_for_unknown_activity():
    response = client.delete("/activities/Unknown/unregister?email=test@mergington.edu")

    assert response.status_code == 404
