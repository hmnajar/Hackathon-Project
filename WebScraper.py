from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
import os

# importing libraries

# define website to be scraped
website = 'https://www.vlr.gg/event/stats/2004/champions-tour-2024-americas-stage-1'

# use options library to keep Chrome window from popping up while still allowing for data to be scraped
script_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_dir, "chromedriver")

# create path for program to access chrome
#path = r'C:\Users\Hector\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'
service = Service(path)
driver = webdriver.Chrome(options=options, service=service)


# open the website, wait until it's loaded in, and scrape the rows in the table
driver.get(website)
WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME,'tr')))
data = driver.find_elements(By.TAG_NAME,'tr')


# empty lists for scraped data to be copied to, names correspond to different names and stats
player_name = []
average_combat_score = []
kill_death_ratio = []
kill_assist_survive_trade = []
first_kill_per_round = []
clutch_percent = []

# for loop to go through the entire table on the website and pick certain stats that are going to be used
for stats in data:
    # try loop in case there is an error
    try:
        # find by class name is used for the player name to avoid also grabbing the team name
        player = stats.find_element(By.CLASS_NAME,"text-of").text
        player_name.append(player)
        
        # find by xpath is used for the remaining because they don't have unique class names
        # xpath is taken from inspecting element on the target page
        acs = stats.find_element(By.XPATH,'./td[5]').text
        average_combat_score.append(acs)

        kdr = stats.find_element(By.XPATH, './td[6]').text
        kill_death_ratio.append(kdr)

        kast = stats.find_element(By.XPATH, './td[7]').text
        kill_assist_survive_trade.append(kast)

        fkpr = stats.find_element(By.XPATH, './td[11]').text
        first_kill_per_round.append(fkpr)

        clutch = stats.find_element(By.XPATH, './td[14]').text
        clutch_percent.append(clutch)
    # catch exception in case something goes wrong and move to the next row
    except Exception as e:
        print(f"Error: Skipping row:  {e}")
# close Google Chrome window when finished
driver.quit()

# use pandas library to add the data to a csv file
df = pd.DataFrame({'Name': player_name, 'ACS': average_combat_score, 'KD': kill_death_ratio, 'KAST': kill_assist_survive_trade, 'FKPR': first_kill_per_round, 'Clutch': clutch_percent})
df.to_csv('player_data.csv', index=False)
