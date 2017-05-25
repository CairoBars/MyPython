import json

jsonstr='''{
    "postList": [
	        {
	            "post_id": "14611057",
	            "type": "multi-photo",
	            "url": "https://huafox.tuchong.com/14611057/",
	            "site_id": "375410",
	            "author_id": "375410",
	            "published_at": "2017-05-16 16:30:33",
	            "excerpt": "",
	            "favorites": 410,
	            "comments": 29,
	            "rewardable": false,
	            "image_count": 8
	          }
        		]
        	}'''

obj=json.loads(jsonstr)

print obj['postList'][0]['post_id']