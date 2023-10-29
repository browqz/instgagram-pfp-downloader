from instaloader import Instaloader

username = input("Enter the username of the account you want to get informations  : ")

loader = Instaloader()

try:
    loader.download_profile(username, profile_pic_only=True)
    print(f"the pfp of '{username}' as been downloaded successfully.")
except Exception as e:
    print(f"there is an error : {str(e)}")