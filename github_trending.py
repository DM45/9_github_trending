import requests
import datetime


def get_current_date_minus_week():
    current_data = datetime.date.today()
    delta_date = current_data + datetime.timedelta(weeks=-1)
    return delta_date


def get_trending_repositories(delta_date, top_size):
    r = requests.get(
        'https://api.github.com/search/repositories?q=created:>'
        + '{}&page=1&per_page={}&sort=stars&order=desc'
        .format(delta_date, top_size))
    return r.json()


def get_output_data_to_console(full_repositories_data):
    repositories_data = full_repositories_data['items']
    print('Name, url and count of open issues: ')
    for datas in repositories_data:
    	print(datas['full_name'], datas['html_url'], datas['open_issues'])


if __name__ == '__main__':
    _top_size = input('Enter value of top size: ')
    _delta_date = get_current_date_minus_week()
    _trending_repositories = get_trending_repositories(_delta_date, _top_size)
    output_data = get_output_data_to_console(_trending_repositories)
