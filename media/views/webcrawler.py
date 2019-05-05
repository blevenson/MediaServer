"""
RangerVid web crawler

"""

from bs4 import BeautifulSoup
import requests


def get_episode_counts(show_name):
    # Return array of number of episodes in seasons
    # [20, 21, 18]

    # Parse website
    url = "http://www.watchepisodeseries.com/" + show_name
    print(url)
    soup = BeautifulSoup(requests.get(url).text, "html.parser")

    # First get number of seasons
    season_div = soup.findAll("div", {"class": "el-season-buttons"})
    season_count = int(season_div[0].findChildren()[-1].text[7:])

    # Now find episode counts for each season
    # Grab all divs with item
    item_div = soup.findAll("div", {"class": "el-item"})

    prev_season = 1
    output = []
    for index, div in enumerate(item_div):
        season_num = int(div.findChildren()[4].findChildren()[0].text[7:])
        # print(str(index) + "\t" + str(season_num))

        # Skip season 0
        if season_num == 0:
            continue

        # If switched season
        if prev_season != season_num:
            prev_episode_num = item_div[
                index - 1].findChildren()[4].findChildren()[1].text[7:]
            # print('Prev Num: ' + prev_episode_num)
            output.append(int(prev_episode_num))

        # Update prev season
        prev_season = season_num

        # print(season_num + "\t" + episode_num)

    # Append the last season
    last_episode_num = item_div[-1].findChildren()[4].findChildren()[
        1].text[7:]
    output.append(int(last_episode_num))

    return output
