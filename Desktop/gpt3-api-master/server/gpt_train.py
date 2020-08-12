import openai
from gpt import Example
from gpt import GPT
from converter import convert
import os
import requests
from dataretrieve import get_data,get_content,get_answer

openai.api_key = 'sk-r5uc6is7lzeluGzpT0DOfYjbeJh7s8WPmMyfhngY'
PATH = './train_html'

data = get_data('github')

# for instance in data:
#     print (get_content(instance))
#     print (get_answer(instance))
#     break

def read_html(path):

    with open(path,'r') as f:
        resp = f.read()
        f.close()
        resp = convert(resp)
    return resp



# train_mails = {
#     'Auth.html':'resp1',
#     'email_added.html':'resp4',
#     'invite1.html':'resp2',
#     'verification.html':'resp3',
#     'verify_email.html':'resp5',
#     'pass_reset_conf.html':'resp6',
#     'inviteTrello.html':'resp7',
#     'pullreq.html':'resp9',
# }




# resp = {
#     'resp1':'{"Type":"Auth", "name":"rahul81", "application":"Dockship", "link":"https://github.com/settings/connections/applications/ccb42a8e19665bcd148e", "From":"The GitHub Team"}',
#     'resp2':'{"Type":"Invitation", "invitor":"rahul81", "repo":"GPT3parser", "repolink":"https://github.com/rahul81/GPT3parser", "For":"sahilpohare@gmail.com"}',
#     'resp3':'{"Type":"Verfication", "name":"rahul81", "Device":"Linux", "verification_code":"849680", "From":"The GitHub Team"}',
#     'resp4':'{"Type":"email_added", "name":"rahul81", "new_email":"rahul.das@adypu.edu.in", "From":"The GitHub Team"}',
#     'resp5':'{"Type":"email_verify", "name":"rahul81", "email":"rahuldas.rr81@gmail.com", "From":"GitHub" }',
#     'resp6':'{"Type":"password_reset_confirmation", "name":"rahul81", "email":"rahuldas.rr81@gmail.com"}',
#     'resp7':'{"Type":"Invite", "inviter":"Rahul D", "board":"Turista-SIH2020","From":"Trello"}',
#     'resp9':'{"Type":"Pull_Request","repo_link":"https://github.com/nikhilm21/Movie-Recommender/pull/1","patch_links":"[https://github.com/nikhilm21/Movie-Recommender/pull/1.patch, https://github.com/nikhilm21/Movie-Recommender/pull/1.diff]"}'
# }




def parse(test):
    gpt3 = GPT(engine='davinci',temperature=0.9,max_tokens=80)

    for instance in data:
        # mail = read_html(os.path.join(PATH,key))
        gpt3.add_example(Example(get_content(instance),get_answer(instance)))
    # print(gpt3.craft_query(test))

    output = gpt3.get_top_reply(test).replace('output: ','').strip()

    return output







