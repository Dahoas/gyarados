import json

datapath = 'data/CodeReviewSE_clean.json'
with open(datapath, 'r') as f:
    data = json.load(f)

'''
Datastructure:
	(answers: List, body: str, comments: str, metadata: dict)
'''
def print_dataset():
	print(json.dumps(data['1'], sort_keys=True, indent=4))

def get_user():
	user_id = '1'
	posts = {}

	for question_id, question in data.items():
		Id = question['meta_data']['Id']
		if Id == user_id:
			posts[question_id] = question
			continue
		answers = question['answers']
		for answer in answers:
			body = answer['body']
			comments = answer['comments']
			metadata = answer['meta_data']
			Id = metadata['Id']
			if user_id == Id:
				posts[question_id] = question
				break
			for comment in comments:
				if comment['Id'] == user_id:
					posts[question_id] = question
					break

	with open(f'{user_id}_posts.txt', 'w') as f:
		f.write(json.dumps(posts, sort_keys=True, indent=4))
	print(len(posts))

if __name__ == '__main__':
	get_user()
