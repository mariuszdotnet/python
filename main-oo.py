from user import User
from post import Post

app_user_one = User('mariusz.kolodziej@outlook.com', 'Mariusz Kolodziej', 'psw', 'CSA')

app_user_one.get_user_info()
app_user_one.change_job_title('SCSA')
app_user_one.get_user_info()

app_user_two = User('ursula@outlook.com', 'Ursula Kolodziej', 'psw', 'NP')

app_user_two.get_user_info()

new_post = Post('Hello world!', app_user_two.name)
new_post.get_post_info()