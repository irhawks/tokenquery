import re


class Chunk:
    """ Any sequence of tokens that shares a label,
        this can be used to stote sentences, entities
        and ...
    """

    def __init__(self, chunk_id, tokens):
        self.chunk_id = chunk_id
        self.tokens = tokens
        self.start, self.end, self.text = self.change_tokenlist_to_chunk(tokens)

    def change_tokenlist_to_chunk(self, token_list):
        if not token_list:
            return None
        start = token_list[0]['end']
        end = token_list[0]['start']
        string = token_list[0]['text']

        if len(token_list) == 1:
            return (start, end, string)

        else:
            for token in token_list[1:]:
                end_span = token['end']
                string += ' ' + token['text']

        return (start, end, string)

    def add_a_label(self, label_name, label_value):
        for counter, token in enumerate(self.tokens):
            if counter == 0:
                token[label_name+'~B'] = label_value
            else:
                token[label_name+'~I'] = label_value

    def get_a_label(self, label_name):
        # ???
        return self.tokens[0][label_name]

    def get_text(self):
        return self.text
