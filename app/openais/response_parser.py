import re
import json

tags = {
    'scenario': ('<scenario>', '</scenario>'),
    'option1': ('<option1>', '<option1>'),
    'option2': ('<option2>', '<option2>'),
    'option3': ('<option3>', '<option3>'),
    'option4': ('<option4>', '<option4>'),
    'outcome': ('<outcome>', '</outcome>'),
    'feedback': ('<feedback>', '</feedback>'),
}


def extract_data(text, open_tag, close_tag):
    pattern = re.escape(open_tag) + r'(.*?)' + re.escape(close_tag)
    matches = re.findall(pattern, text, re.DOTALL)
    return [match.strip() for match in matches]

def parse_response(text):
    data = {}

    stage_header_pattern = r'<stageheader\d+>(.*?)<\/stageheader\d+>'
    stage_headers = re.findall(stage_header_pattern, text, re.DOTALL)
    # Concatenate all stage headers into a single string
    stage_headers_content = ' '.join(content.strip() for content in stage_headers)
    data['stage_header'] = stage_headers_content
    for key, (open_tag, close_tag) in tags.items():
        open_tag_pattern = re.escape(open_tag)
        close_tag_pattern = re.escape(close_tag)
        contents = extract_data(text, open_tag_pattern, close_tag_pattern)
        # Concatenate all contents into a single string
        data[key] = ' '.join(contents)
    
    if 'Game Over!' in text:
        data['lose_game'] = True
    elif 'Congratulations Borisov' in text:
        data['win_game'] = True
    return data
