from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import Open_website
import Login
import Find_part
import Add_user
import Edit_user
import User_detail
import Froze_user
import Password_reset
import Delete_user
import Search_user

#######################
# 以下为打开主页面部分  #
#######################

url = 'http://127.0.0.1:9011'

driver = Open_website.open_website(url)

Login.login(driver)

WebDriverWait(driver, 10).until(
    EC.url_changes('http://127.0.0.1:9011')
)

time.sleep(3)

print("New URL after login:", driver.current_url)

#########################
# 以下为用户管理页面测试  #
#########################

welcome_url = driver.current_url

Find_part.find_part(driver, '用户管理')

# 等待页面跳转并打印新地址
WebDriverWait(driver, 10).until(EC.url_changes(welcome_url))
print("New URL after clicking 'User Management':", driver.current_url)

#########################
# 以下为测试新增用户功能

skip_option = input("Do you want to skip the add user function test? y/n").strip().lower()

if skip_option == 'n':
    Add_user.add_user(driver)
    print("Add user function test successfully!")
    time.sleep(3)
else:
    print("Skip the add user function test!")


########################
# 以下为测试编辑用户功能

skip_option = input("Do you want to skip the edit user function test? y/n").strip().lower()
if skip_option == 'n':
    Edit_user.edit_user(driver)
    print("Edit user function test successfully!")
    time.sleep(3)
else:
    print("Skip the edit user function test!")

########################
# 以下为测试查看详情功能

skip_option = input("Do you want to skip the user detail function test? y/n").strip().lower()
if skip_option == 'n':
    User_detail.user_detail(driver)
    print("User detail function test successfully!")
    time.sleep(3)
else:
    print("Skip the user detail function test!")


########################
# 以下为测试冻结功能

skip_option = input("Do you want to skip the froze user function test? y/n").strip().lower()
if skip_option == 'n':
    Froze_user.froze_user(driver)
    print("Froze user function test successfully!")
    time.sleep(3)
else:
    print("Skip the froze user function test!")



########################
# 以下为测试密码重置功能

skip_option = input("Do you want to skip the password reset function test? y/n").strip().lower()
if skip_option == 'n':
    Password_reset.password_reset(driver)
    print("Password reset function test successfully!")
    time.sleep(3)
else:
    print("Skip the password reset function test!")


########################
# 以下为测试删除功能

skip_option = input("Do you want to skip the delete user function test? y/n").strip().lower()
if skip_option == 'n':
    Delete_user.delete_user(driver)
    print("Delete user function test successfully!")
    time.sleep(3)
else:
    print("Skip the delete user function test!")


########################
# 以下为测试查询用户功能

skip_option = input("Do you want to skip the search user function test? y/n").strip().lower()
if skip_option == 'n':
    Search_user.search_user(driver)
    print("Search user function test successfully!")
    time.sleep(3)
else:
    print("Skip the search user function test!")
