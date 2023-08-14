""" 构建云足迹 """
import os

import sys
import re
# import json
# import datetime
import requests

# https://github.com/twfb/DeployIssue
# https://github.com/twfb/DeployIssue/blob/main/deploy_issue.py

REPO = sys.argv[1]
TOKEN = sys.argv[2]
POST_DIR = "docs/footmarks/"

HEADERS = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": "token " + TOKEN,
}

# 读取目录中的 .md 文件，截取不含后缀的文件名作为文章列表；
all_posts = list(map(lambda x: x.split(".md")[0], os.listdir(POST_DIR)))

# 要删除的文章列表；
remove_posts = filter(
    lambda x: x["title"] in all_posts,
    requests.get(
        f"https://api.github.com/repos/{REPO}/issues?labels=unpick",
        headers=HEADERS,
        timeout=10,
    ).json(),
)

# API 接口请求 issues 列表，并过滤不需要的项目；
add_posts = filter(
    lambda x: "unpick" not in str(x["labels"]),
    requests.get(
        f"https://api.github.com/repos/{REPO}/issues?labels=pick",
        headers=HEADERS,
        timeout=10,
    ).json(),
)


def get_comment(item):
    """获取评论"""
    str_rlt = ""
    if item["comments"] == 0:
        return str_rlt
    add_comments = filter(
        lambda x: x["author_association"] == "OWNER",
        requests.get(
            item["comments_url"],
            headers=HEADERS,
            timeout=10,
        ).json(),
    )
    for comment in add_comments:
        str_rlt += comment["body"] + "\n\n"
    return str_rlt


def update_sidebar(dst_file, arg_info):
    """更新侧边栏"""
    # 替换 <!-- footmarks --> 到 <!-- footmarks end--> 之间的内容
    arg_info = "<!-- footmarks -->\n" + arg_info + "\n<!-- footmarks end-->"
    arg_info = arg_info.replace("docs/", "")
    # 获取 dst_file 内容
    with open(dst_file, "r", encoding="utf-8") as file:
        dst_file_content = file.read()
    # print(arg_info)
    new_dst_file_content = re.sub(
        r"<!-- footmarks -->(.|\n)+<!-- footmarks end-->",
        arg_info,
        dst_file_content,
        1,
    )
    with open(dst_file, "w", encoding="utf-8", newline="\n") as file:
        file.write(new_dst_file_content)
    return True


# 更新链接到 _sidebar.md


# add, update, delete
count = [0, 0, 0]

INFO = ""

for post in add_posts:
    file_path = POST_DIR + post["title"] + ".md"
    INFO += f"  * [{post['title']}]({file_path})\n"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(post["body"])
        f.write("\n\n")
        f.write(get_comment(post))
    os.system("git add " + file_path + " >/dev/null 2>&1")
    if post["title"] in all_posts:
        count[1] += 1
    else:
        count[0] += 1

update_sidebar("docs/_sidebar.md", INFO)
os.system("git add docs/_sidebar.md >/dev/null 2>&1")

for post in remove_posts:
    os.system("git rm " + POST_DIR + post["title"] + ".md" + " >/dev/null 2>&1")
    count[2] += 1

print(f"autoupdate \n add {count[0]}，update {count[1]}，delete {count[2]}")
