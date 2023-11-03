from PIL import Image, ImageFilter
from domain.Photo import Photo

class Service:
    '''
    New Service Object that has all the filter methods that can be applied to a photo.
    '''
    def __init__(self) -> None:
        '''
        Class initializer.
        '''
        self.__index = 0

    def create_photo_object(self,file_path) -> Photo:
        '''
        This method creates a Photo object.
        :param file_path: str
        :return: Photo
        '''
        photo = Photo(f"image_{self.__index}",file_path)
        self.__index = self.__index+1
        return photo

    def sharpen_image(self, photo) -> Image:
        '''
        This method sharpens a given image.
        :param photo: Image
        :return: Image
        '''
        return photo.filter(ImageFilter.SHARPEN)

    def gaussian_blur_image(self,photo) -> Image:
        '''
        This method blurs a given image.
        :param photo: Image
        :return: Image
        '''
        return photo.filter(ImageFilter.GaussianBlur)


    def smooth_image(self,photo) -> Image:
        '''
        This method smooths a given image.
        :param photo: Image
        :return: Image
        '''
        return photo.filter(ImageFilter.SMOOTH)


    def enhance_details_image(self,photo) -> Image:
        '''
        This method enhances the details of a given image.
        :param photo: Image
        :return: Image
        '''
        return photo.filter(ImageFilter.DETAIL)


    def enhance_edges_image(self,photo) -> Image:
        '''
        This method enhances the edges of a given photo.
        :param photo: Image
        :return: Image
        '''
        return photo.filter(ImageFilter.EDGE_ENHANCE)




