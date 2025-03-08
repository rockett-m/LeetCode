import pandas as pd

def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:

    user_content['converted_text'] = None
    sents = user_content['content_text']
    for i in range(len(sents)):
        words = sents[i].split(' ')
        print(i, sents[i], words)
        out = ''
        for w in words:
            if '-' in w:
                z = w.split('-')
                out += '-'.join([x.capitalize() for x in z])
            else:
                out += w.capitalize()
            out += ' '

        user_content['converted_text'].iloc[i] = out[:-1]

    user_content.rename(columns={'content_text': 'original_text'}, inplace=True)

    return user_content