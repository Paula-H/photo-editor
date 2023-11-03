import tkinter as tkinter
from PIL import Image
class Photo:
    '''
    New Object that contains an Image and its name.
    '''
    def __init__(self, name, image_link) -> None:
        '''
        Class initializer.
        :param name: string
        :param image_link: path -> string
        '''
        self.__name = name
        self.__image_link = Image.open(image_link)

    def getImage(self) -> Image:
        '''
        Getter for the Image object.
        :return: Image
        '''
        return self.__image_link

    def getName(self) -> str:
        '''
        Getter for the name.
        :return: str
        '''
        return self.__name

    def setImage(self,image_link) -> None:
        '''
        Setter for the Image object.
        :param image_link: Image
        :return: None
        '''
        self.__image_link = image_link

    def setName(self, name) -> None:
        '''
        Setter for the name.
        :param name: str
        :return: None
        '''
        self.__name = name


