#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:pyy
# datetime:2019/1/9 14:01
import json

import requests
web_site_url = "http://127.0.0.1:8888"
tsessionid = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6Nywibmlja25hbWUiOiJ2YW5uZXNzIiwiZXhwIjoxNTUwMDE4MTA5fQ.Hq_DVr1WQZdIhbeuj4pp3NBJrF9Es3n3EUQwxovfQ-I"
headers = {"tsessionid": tsessionid}

# requests.get(url=web_site_url, headers=headers)


def create_group():
    files = {
        "front_image": open("D:/images/python.png", "rb")
    }
    data = {
        "name": "学前教育交流角",
        "desc": "这里是学前教育的交流中心，大家有什么问题可以一起来交流讨论！欢迎大家的加入！",
        "notice": "这里是学前教育的交流中心，大家有什么问题可以一起来交流讨论！欢迎大家的加入！",
        "category": "教育同盟"
    }
    res = requests.post("{}/groups/".format(web_site_url), headers=headers, data=data, files=files)
    print(res.status_code)
    print(json.loads(res.text))


def apply_group(group_id, apply_reason):
    data = {
        "apply_reason": apply_reason,
    }
    res = requests.post("{}/groups/{}/members/".format(web_site_url, group_id), headers=headers, json=data)
    print(res.status_code)
    print(json.loads(res.text))

def add_post(group_id):
    #发帖
    data = {
        "title":"tornado从入门到实战",
        "content":"tornado从入门到实战"
    }
    res = requests.post("{}/groups/{}/posts/".format(web_site_url, group_id), headers=headers, json=data)
    print(res.status_code)
    print(json.loads(res.text))

def add_comment(post_id):
    # 发帖
    data = {
        "content": "文章写的非常棒"
    }
    res = requests.post("{}/posts/{}/comments/".format(web_site_url, post_id), headers=headers, json=data)
    print(res.status_code)
    print(json.loads(res.text))

def get_comments(post_id):
    res = requests.get("{}/posts/{}/comments/".format(web_site_url, post_id), headers=headers)
    print(res.status_code)
    print(json.loads(res.text))


def get_replys(comment_id):
    res = requests.get("{}/comments/{}/replys/".format(web_site_url, comment_id), headers=headers)
    print(res.status_code)
    print(json.loads(res.text))


if __name__ == "__main__":
    # create_group()
    # apply_group(7, "study together!!!")
    # add_post(8)

    # add_comment(2)
    # get_comments(2)
    get_replys(4)