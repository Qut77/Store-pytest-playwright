def test_login(login_page) -> None:
    login_page.open()
    login_page.login('plovhaha@gmail.com', '123')
    login_page.expect_user_logged_in()

