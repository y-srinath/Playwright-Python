
def test_GET_api(playwright):
    # Setup API request context
    request = playwright.request.new_context()
    response = request.get("https://fake-json-api.mock.beeceptor.com/users")

    # ----------Status Code Assertions----------
    print(f"\n📡 Response Status Code: {response.status}")
    print(f"📡 Response OK: {response.ok}")
    assert response.status == 200, f"Expected 200 but got {response.status}"
    assert response.ok, "Response is not OK"
    
    #----------Response Body--------------------
    data = response.json()
    print(f"\n📦 Total users returned: {len(data)}")
    print(f"📦 First user: {data[0]['name']}")
    print(f"📦 Last user: {data[-1]['name']}")
    
    # ---------- Data Structure Assertions ----------
    assert isinstance(data, list), "Response should be a list"
    assert len(data) > 0, "User list should not be empty"
    assert len(data) == 10, f"Expected 10 users but got {len(data)}"

    # ---------- First User Field Assertions ----------
    first_user = data[0]
    print(f"\n👤 Validating first user: {first_user['name']}")

    assert first_user["id"] == 1
    assert "name" in first_user, "Missing 'name' field"
    assert "email" in first_user, "Missing 'email' field"
    assert "@" in first_user["email"], "Invalid email format"
    assert isinstance(first_user["id"], int), "ID should be an integer"
    assert first_user["name"] != "", "Name should not be empty"

    # ---------- Loop Through All Users ----------
    print(f"\n🔁 Checking all {len(data)} users have required fields...")
    for user in data:
        assert "id" in user
        assert "name" in user
        assert "email" in user
        assert "@" in user["email"]
        print(f"  ✅ User {user['id']}: {user['name']} ({user['email']})")

    # ---------- Cleanup ----------
    request.dispose()
    print("\n✅ All assertions passed! API request disposed.")
