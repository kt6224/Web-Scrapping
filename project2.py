from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# Create a Chrome WebDriver instance
driver = webdriver.Chrome()
time.sleep(2)

driver.maximize_window()
time.sleep(2)

# Navigate to the Instahyre website
data = []
for i in range(2008,2024):
    driver.get(f"https://www.iplt20.com/matches/results/{i}")
    time.sleep(2)

# //*[@id="team_archive"]/li[1]
# //*[@id="team_archive"]/li[2]

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    elements = driver.find_elements(By.XPATH,value='//*[@id="team_archive"]/li')

#print(len(elements))

#seasons = driver.find_elements(By.XPATH,value='//*[@id="smResultsWidget"]/div/div[1]/div/div[1]/div/div[4]/div/div[2]')
#seasons = driver.find_elements(By.XPATH, '//*[@id="smResultsWidget"]//div[@class="match-scroller"]/div[@class="match-list"]/div/div[1]/div/div[1]/div/div[2]')


#print(len(seasons))


# //*[@id="smResultsWidget"]/div/div[1]/div/div[1]/div/div[4]/div/div[2]/div[1]
# //*[@id="smResultsWidget"]/div/div[1]/div/div[1]/div/div[4]/div/div[2]/div[2]

    for idx, element in enumerate(elements,start=1):


        x_path_season = f'//*[@id="smResultsWidget"]/div/div[1]/div/div[1]/div/div[4]/div/div[1]'

        x_path_match_number = f'//*[@id="team_archive"]/li[{idx}]/div[1]/div[1]/span[1]'
# # # //*[@id="team_archive"]/li[2]/div[1]/div[1]/span[1]
# # # //*[@id="team_archive"]/li[59]/div[1]/div[1]/span[1]
        x_path_venue = f'//*[@id="team_archive"]/li[{idx}]/div[1]/div[2]/span/p'
# # //*[@id="team_archive"]/li[2]/div[1]/div[2]/span/p
#
        x_path_time_date = f'//*[@id="team_archive"]/li[{idx}]/div[1]/div[2]/div'
#
        x_path_winning_team = f'//*[@id="team_archive"]/li[{idx}]/div[2]/div[1]/div'
# # //*[@id="team_archive"]/li[2]/div[2]/div[1]/div
#
        x_path_first_team = f'//*[@id="team_archive"]/li[{idx}]/div[2]/div[2]/div/div[1]/div'
#     #//*[@id="team_archive"]/li[1]/div[2]/div[2]/div/div[1]/div
#
        x_path_second_team = f'//*[@id="team_archive"]/li[{idx}]/div[2]/div[2]/div/div[2]/div'
# # //*[@id="team_archive"]/li[1]/div[2]/div[2]/div/div[2]
        x_path_link = f'//*[@id="team_archive"]/li[{idx}]/div[2]/div[3]/div/a'

        # season = driver.find_element(By.XPATH,value=x_path_season).text
        # print(f'{season}')

        season = i
        print(i)

        match_number = driver.find_element(By.XPATH,value=x_path_match_number).text
        #number = match_number.split()[1]
        if any(char.isdigit() for char in match_number):
            number = ''.join(filter(str.isdigit, match_number))
            print(f'{number}')
        else:
            number = match_number
            print(f': {number}')
        #print(f'{number}')

        venue = driver.find_element(By.XPATH,value=x_path_venue).text
        print(f'{venue}')

        time_date = driver.find_element(By.XPATH,value=x_path_time_date).text
        print(f'{time_date}')

        winning_team = driver.find_element(By.XPATH,value=x_path_winning_team ).text
        print(f'{winning_team}')

        first_team = driver.find_element(By.XPATH,value=x_path_first_team).text
        print(f'{first_team}')

        second_team = driver.find_element(By.XPATH,value=x_path_second_team).text
        print(f'{second_team}')

        link_element = driver.find_element(By.XPATH,value=x_path_link)
        link = link_element.get_attribute("href")
        print(f'{link}')

        data.append({
            'Season': season,
            'Matchnumber': number,
            'Venue': venue,
            'Date_Time': time_date,
            'Winningteam': winning_team,
            'Firstteam': first_team,
            'Secondteam': second_team,
            'Link':link
        })


time.sleep(5)
driver.quit()

df = pd.DataFrame(data)
df.to_csv('ipl_dataset.csv', index=False)















