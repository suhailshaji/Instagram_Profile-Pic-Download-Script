import instaloader


insta_loader_def = instaloader.Instaloader()
username = input("Enter the Username: ")

insta_loader_def.download_profile(username , profile_pic_only=True)
print(f"{username}'s Profile Picture is Downloaded")


#Requirement
#pip install instaloader
#pip install request
#urllib3
