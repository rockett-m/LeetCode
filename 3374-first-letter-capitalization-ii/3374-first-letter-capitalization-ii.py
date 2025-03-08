import pandas as pd

def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:

    user_content['converted_text'] = None
    sents = user_content['content_text']
    for i in range(len(sents)):
        out = ''
        for w in sents[i].split(' '):
            if '-' in w:
                out += '-'.join([x.capitalize() for x in w.split('-')])
            else:
                out += w.capitalize()
            out += ' '

        user_content['converted_text'].iloc[i] = out[:-1]

    user_content.rename(columns={'content_text': 'original_text'}, inplace=True)

    return user_content