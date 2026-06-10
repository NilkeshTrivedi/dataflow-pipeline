def test_root_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "running"

def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_get_users(client):
    response = client.get("/api/v1/users")
    assert response.status_code in [200, 404]

def test_get_user_by_id(client):
    response = client.get("/api/v1/users/1")
    assert response.status_code in [200, 404]

def test_get_invalid_user(client):
    response = client.get("/api/v1/users/99999")
    assert response.status_code == 404

def test_get_posts(client):
    response = client.get("/api/v1/posts")
    assert response.status_code in [200, 404]

def test_get_employees(client):
    response = client.get("/api/v1/employees")
    assert response.status_code in [200, 404]

def test_get_stats(client):
    response = client.get("/api/v1/stats")
    assert response.status_code == 200
    data = response.json()
    assert "total_users" in data
    assert "total_posts" in data
    assert "total_employees" in data
    assert "avg_salary" in data

def test_pipeline_status(client):
    response = client.get("/api/v1/pipeline/status")
    assert response.status_code == 200
    assert response.json()["status"] == "running"

def test_filter_users_by_city(client):
    response = client.get("/api/v1/users?city=Gwenborough")
    assert response.status_code in [200, 404]

def test_filter_employees_by_department(client):
    response = client.get("/api/v1/employees?department=Engineering")
    assert response.status_code in [200, 404]