from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\chromedriver.exe") 
driver.implicitly_wait(10)

players = []

url = "https://fbref.com/en/comps/9/stats/Premier-League-Stats"

driver.get(url)


# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[3]')).ENTER()
#     )
    
# except:
#     driver.quit()


element = driver.find_element_by_xpath('//*[@id="qc-cmp2-ui"]/div[2]/div/button[3]')
driver.execute_script("arguments[0].click();", element)
time.sleep(2)

# for player in driver.find_elements_by_tag_name('tr'):
#     player_name = player.find_element_by_xpath('//*[@id="stats_standard"]/tbody/tr[1]/td[1]/a').text
#     nation = player.find_element_by_xpath('//*[@id="stats_standard"]/tbody/tr[1]/td[2]/a/span/span').text
#     pos = player.find_element_by_xpath('//*[@id="stats_standard"]/tbody/tr[1]/td[3]').text
#     squad = player.find_element_by_xpath('//*[@id="stats_standard"]/tbody/tr[1]/td[4]/a').text

#     players.append({'Name': player_name, 'Nationality': nation, 'Position': pos, 'Club Team': squad})

# print(players)

user_search = input("""

Input a player name to see their historical data:

""")


search_bar = driver.find_element_by_xpath('//*[@id="header"]/div[3]/form/div/div/input[2]')
search_bar.send_keys(user_search)
search_bar.send_keys(Keys.ENTER)
time.sleep(2)


player_pos_XPATH = driver.find_element_by_xpath('//*[@id="meta"]/div[2]')


print(player_pos_XPATH.text)

if 'Position: FW' in player_pos_XPATH.text:
    player_pos = 'FW'
elif 'Position: MF' in player_pos_XPATH.text:
    player_pos = 'MF'
elif 'Position: DF' in player_pos_XPATH.text:
    player_pos = 'DF'
else:
    print("Couldn't assign position")


    
for i in range(1, 22):
    player_data_rows = driver.find_elements_by_xpath(f'//*[@id="scout_summary_{player_pos}"]/tbody/tr[{i}]')
    for stat in player_data_rows:
        print(stat.text)




# search.send_keys('test')
# search.send_keys(Keys.ENTER)

# print(search.text)

# time.sleep(3)

# driver.quit()