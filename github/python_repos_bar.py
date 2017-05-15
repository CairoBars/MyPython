#_*_ coding:utf-8 _*_
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
#执行API迪奥弄并存储响应
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print("Status code:",r.status_code)

#将API响应存储在一个变量中
response_dict=r.json()
print("Total repositories:",response_dict['total_count'])


#搜索有关仓库的信息
repo_dicts=response_dict['items']

names,plot_dicts=[],[]


for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	result_dict={
		'value':repo_dict['stargazers_count'],
		'label':repo_dict['description']
	}
	plot_dicts.append(result_dict)


#可视化
my_style=LS('#333366',base_style=LCS)
chart=pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)

chart.title='Python Projects'
chart.x_labels=names
chart.add('',plot_dicts)
chart.render_to_file('gg.svg')