def get_phrase():
    phrase =  input("Choose phrase: ")
    phrase_result = [s for s in hashtag_all if phrase in s]
    return phrase_result


def get_number(phrase_result):
    import random
    
    try:
        hashtag_num = int(input("How many hashtags do you need?: "))
        hashtag_set = random.sample(phrase_result, hashtag_num)
    
    except ValueError:
        print("This Hashtag has only", len(phrase_result), "positions. They have been added.")
        hashtag_set = random.sample(phrase_result, len(phrase_result))
        for hashtag in hashtag_set:
            export_list.append(hashtag)
        return len(phrase_result)
    
    else:
        for hashtag in hashtag_set:
            export_list.append(hashtag)
        return hashtag_num
