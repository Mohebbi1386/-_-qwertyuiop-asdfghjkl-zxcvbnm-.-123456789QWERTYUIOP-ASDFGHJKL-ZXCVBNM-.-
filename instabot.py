from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import instaloader
import os
import subprocess

loader = instaloader.Instaloader()

def login_insta_1():
    #loader = instaloader.Instaloader()
    #loader.login(username, password)
    #loader.dirname_pattern = r"C:\Users\Lenovo\Desktop\bot"
    #loader.save_session_to_file(username)
    loader.load_session_from_file("telensta", filename=r"C:\Users\Lenovo\Desktop\bot\telensta")

def download_profile (id):
    loader.download_profile(id,profile_pic_only=True)
    picture = subprocess.getoutput(fr"dir C:\Users\Lenovo\Desktop\bot\{id}")
    picture = picture.split("\n")
    for i in picture:
        if "jpg" in i :
            picture = i
    picture = picture.split(" ")
    name = picture[-1]
    return name
def biography(id):
    profile = instaloader.Profile.from_username(loader.context,id)
    return profile.biography
def number_of_follower (id):
    profile = instaloader.Profile.from_username(loader.context,id)
    return profile.followers
def number_of_followees (id):
    profile = instaloader.Profile.from_username(loader.context,id)
    return profile.followees
def is_verified (id):
    profile = instaloader.Profile.from_username(loader.context,id)
    return profile.is_verified
def caption (id):
    list = []
    profile = instaloader.Profile.from_username(loader.context,id)
    for posts in profile.get_posts():
        list.append(posts.caption)
    return list
def story(id):
    profile = loader.check_profile_id(id)
    profile = str(profile)
    profile = profile.replace("<","")
    profile = profile.replace("Profile","")
    profile = profile.replace(">","")
    profile = profile.replace(id,"")
    profile = profile.replace(")","")
    profile = profile.replace("(","")
    profile = profile.replace(" ","")
    profile = int(profile)
    loader.download_stories(userids=[profile])
    return profile
def post(id):
    try:
        subprocess.getoutput(f"instaloader profile {id}")
    except:
        pass
def storys():
    dir = os.listdir(r'C:\Users\Lenovo\Desktop\bot\：stories')
    storys = []
    for i in dir:
        if 'jpg' in i or 'webp' in i:
            if 'profile' not in i:
                if 'webp' in i:
                    os.rename(fr'C:\Users\Lenovo\Desktop\bot\：stories\{i}',fr'C:\Users\Lenovo\Desktop\bot\：stories\{i[:-4] + "jpg"}')
                    i = i[:-4] + 'jpg'
                    if i[:-4]+'.mp4' not in dir:
                        storys.append(i)
        if 'mp4' in i:
            if i[:-4]+'.jpg' in dir:
                os.remove(fr'C:\Users\Lenovo\Desktop\bot\：stories\{i[:-4]+".jpg"}')
            storys.append(i)
    return storys
def posts(id):
    dir = os.listdir(fr'C:\Users\Lenovo\Desktop\bot\{id}')
    posts = []
    for i in dir:
        if 'jpg' in i:
            if 'profile' not in i:
                if i[:-4]+'.mp4' not in dir:
                    posts.append(i)
        if 'mp4' in i:
            if i[:-4]+'.jpg' in dir:
                os.remove(fr'C:\Users\Lenovo\Desktop\bot\{id}\{i[:-4]+".jpg"}')
            posts.append(i)
    return posts
def highlight(id):
    profile = loader.check_profile_id(id)
    profile = str(profile)
    profile = profile.replace("<","")
    profile = profile.replace("Profile","")
    profile = profile.replace(">","")
    profile = profile.replace(id,"")
    profile = profile.replace(")","")
    profile = profile.replace("(","")
    profile = profile.replace(" ","")
    profile = int(profile)
    userids=profile
    id = profile
    for highlight in loader.get_highlights(id):
        # highlight is a Highlight object
        for item in highlight.get_items():
            # item is a StoryItem object
            try:
                loader.download_storyitem(item, '{}/{}'.format(highlight.owner_username, highlight.title))
            except:
                pass
def highlights(id):
    dir = os.listdir(r'C:\Users\Lenovo\Desktop\bot')
    list = {}
    for i in dir:
        if id+"∕" in i:
            for j in os.listdir(fr'C:\Users\Lenovo\Desktop\bot\{i}'):
                if 'webp' in j or 'jpg' in j or 'mp4' in j:
                    if 'profile' not in j:
                        if 'webp' in j:
                            os.rename(fr'C:\Users\Lenovo\Desktop\bot\{i}\{j}',fr'C:\Users\Lenovo\Desktop\bot\{i}\{j[:-4] + "jpg"}')
                    if '.mp4' in j:
                        try:
                            os.remove(fr'C:\Users\Lenovo\Desktop\bot\{i}\{j[:-4] + ".jpg"}')
                        except:
                            pass

    for i in dir:
        if id+"∕" in i:
            for j in os.listdir(fr'C:\Users\Lenovo\Desktop\bot\{i}'):
                if 'webp' in j or 'jpg' in j or 'mp4' in j:
                    if 'profile' not in j:
                        if 'webp' in j:
                            os.rename(fr'C:\Users\Lenovo\Desktop\bot\{i}\{j}',fr'C:\Users\Lenovo\Desktop\bot\{i}\{j[:-4] + "jpg"}')
                    list[fr'C:\Users\Lenovo\Desktop\bot\{i}\{j}'] = i
    return list

#story("perspolis")
#print(number_of_follower("perspolis"))
#print(number_of_followees("perspolis"))
#str(download_profile("psg"))
#print(biography("perspolis"))
#print(is_verified("perspolis"))
