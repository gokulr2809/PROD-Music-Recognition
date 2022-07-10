from email.mime import image
import python.code.utils.music_finder

class Data():
    def __init__(self, music_data):
        self.music_extracted_data = music_data

    def result(self):
        '''Total result from the api as json data'''
        if  (self.music_extracted_data['result'] == None): 
            return None
        else:
            return self.music_extracted_data['result']

    def artist(self):
        '''artist'''
        if  (self.music_extracted_data['result'] == None): 
            return None
        else:
            return self.music_extracted_data['result']['artist']

    def title(self):
        '''music title'''
        if  (self.music_extracted_data['result'] == None): 
            return None
        else:
            return self.music_extracted_data['result']['title']

    def album(self):
        '''album name'''
        if  (self.music_extracted_data['result'] == None): 
            return None
        else:
            return self.music_extracted_data['result']['album']

    def release_date(self):
        '''release_date for the music'''
        if  (self.music_extracted_data['result'] == None): 
            return None
        else:
            return self.music_extracted_data['result']['release_date']

    def label(self):
        '''label of the music'''
        if  (self.music_extracted_data['result'] == None): 
            return None
        else:
            return self.music_extracted_data['result']['label']

    def SPOTIFY_spotify(self):
        if  (self.music_extracted_data['result'] == None): 
            return None
        else:
            return self.music_extracted_data['result']['spotify']['external_urls']['spotify']
    def SPOTIFY_img(self):
        if  (self.music_extracted_data['result'] == None): 
            return None
        else:
            return self.music_extracted_data['result']['spotify']['album']['images'][1]['url']
    
