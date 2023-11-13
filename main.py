import re
import long_responses as long

def message_probablity(user_msg, recognized_words, single_res=False, req_words=[]):
    msg_certainity = 0
    have_req_words = True
    
    for word in user_msg:
        if word in recognized_words:
            msg_certainity += 1
            
    percentage = float(msg_certainity) / float(len(recognized_words))
    
    for word in req_words:
        if word not in user_msg:
            have_req_words = False
            break

    if have_req_words or single_res:
        return int(percentage*100)
    else:
        return 0
    
def check_all_msgs(message):
    highest_prob_list = {}
    
    def response(bot_res, list_of_words, single_res=False, req_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_res] = message_probablity(message, list_of_words, single_res, req_words)
        
    # Responses----------------------------------------------------------------------------------------------------------------------------->
    response('Hello!', ['hello', 'hi', 'hey', 'sup'], single_res=True)
    response('I\'m doing fine, and you?', ['how','are','you','doing'], req_words=['how'])
    response('Thank you!', ['i','love','you'], req_words=['love'])
    
    response(long.R_ADVICE, ['give', 'advice'], req_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], req_words=['you', 'eat'])
        
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    
    return long.unknown() if highest_prob_list[best_match] < 1 else best_match
    
def get_response(user_input):
    split_msg = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    res = check_all_msgs(split_msg)
    return res

while True:
    print('Bot: ' + get_response(input('You: ')))