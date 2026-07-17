from src.app import activities


def test_get_activities_returns_all_activities(client):
    response = client.get("/activities")

    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, dict)
    assert set(payload.keys()) == set(activities.keys())


def test_each_activity_has_expected_fields(client):
    response = client.get("/activities")

    assert response.status_code == 200
    payload = response.json()

    for _, activity in payload.items():
        assert "description" in activity
        assert "schedule" in activity
        assert "max_participants" in activity
        assert "participants" in activity
        assert isinstance(activity["participants"], list)
