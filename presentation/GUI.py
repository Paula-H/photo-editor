import tkinter as tk
import tkinter.ttk
from tkinter import filedialog, TOP
from service.Service import Service
from PIL import ImageTk

class GUI:
    '''
    Presentation Class using tkinter.
    '''

    def __export_image(self) -> None:
        '''
        This method exports the current image.
        :return: None
        '''
        data = [('png', '*.png')]
        filesave = filedialog.asksaveasfilename(filetypes=data, defaultextension=data,initialfile = self.__current_name)
        newfile = self.__image_copy.save(filesave)

    def __apply_enhance_edges(self) -> None:
        '''
        This method enhances the edges of the current photo by calling the Service method.
        :return: None
        '''
        self.__image_copy = self.__service.enhance_edges_image(self.__image_copy)

    def __apply_enhance_details(self) -> None:
        '''
        This method enhances the details of the current photo by calling the Service method.
        :return: None
        '''
        self.__image_copy = self.__service.enhance_details_image(self.__image_copy)

    def __apply_smooth(self) -> None:
        '''
        This method applies the smooth filter to the current photo by calling the Service method.
        :return: None
        '''
        self.__image_copy = self.__service.smooth_image(self.__image_copy)

    def __apply_sharpen(self) -> None:
        '''
        This method applies the sharpen filter to the current photo by calling the Service method.
        :return: None
        '''
        self.__image_copy = self.__service.sharpen_image(self.__image_copy)

    def __apply_gaussian_blur(self) -> None:
        '''
        This method applies the gaussian blur filter to the current photo by calling the Service method.
        :return: None
        '''
        self.__image_copy = self.__service.gaussian_blur_image(self.__image_copy)

    def switcher(self,filter):
        '''
        Switch for the filter.
        :param filter: str
        :return: function
        '''
        switcher_map={
            "Gaussian Blur" : self.__apply_gaussian_blur(),
            "Sharpen Image" : self.__apply_sharpen(),
            "Smooth Image" : self.__apply_smooth(),
            "Enhance Details" : self.__apply_enhance_details(),
            "Enhance Edges" : self.__apply_enhance_edges()
        }
        return switcher_map.get(filter)

    def __apply_filter(self, filter) -> None:
        '''
        This method is used for applying a filter on an already existing photo.
        :param filter: str
        :return: None
        '''
        self.switcher(filter)
        self.__image = ImageTk.PhotoImage(self.__image_copy)
        self.__canvas.create_image((0, 0), image=self.__image, anchor="nw")
        self.__canvas.update()

    def __add_image(self) -> None:
        '''
        This method is used for adding an image in the editor.
        :return: None
        '''
        self.__file_path = filedialog.askopenfilename(initialdir="D:/Projects/PhotoEditor")
        self.__current_name = self.__image = self.__service.create_photo_object(self.__file_path).getName()
        self.__current_path = "D:/Projects/PhotoEditor"+self.__current_name
        self.__image = self.__service.create_photo_object(self.__file_path).getImage()
        self.__image_copy = self.__service.create_photo_object(self.__file_path).getImage()
        self.__canvas.config(width = self.__image.width, height = self.__image.height)
        self.__image = ImageTk.PhotoImage(self.__image)
        self.__canvas.create_image((0,0),image=self.__image, anchor="nw")
        self.__canvas.update()

    def __init__(self) -> None:
        '''
        Class initializer
        '''
        self.__service = Service()
        self.__root = tk.Tk()
        self.__file_path = None
        self.__image = None
        self.__image_copy = None
        self.__canvas = tk.Canvas(self.__root,width=750, height = 600, bg="white")
        self.__current_name = None
        self.__current_path = None
        self.__new_name_variable = tk.StringVar
        self.initialize()



    def initialize(self) -> None:
        '''
        This method creates the main window and places its targets within its contents.
        :return: None
        '''

        self.__root.geometry("1000x600")
        self.__root.title("Editing App Software")
        self.__root.config(bg="white")

        left_frame = tk.Frame(self.__root, width=200, height=600, bg="white")
        left_frame.pack(side="left", fill="y")

        self.__canvas.pack()

        image_button = tk.Button(left_frame, text="Add Image", bg="white", command=self.__add_image)
        image_button.pack(pady=15, side = TOP)

        filer_label = tk.Label(left_frame, text="Select Filter", bg="white")
        filer_label.pack( side = TOP)
        filter_combobox = tk.ttk.Combobox(left_frame, values = ["Sharpen Image", "Gaussian Blur",
                                                                "Smooth Image","Enhance Details","Enhance Edges"])

        filter_combobox.bind("<<ComboboxSelected>>", lambda event: self.__apply_filter(filter_combobox.get()))
        filter_combobox.pack()

        export_button = tk.Button(left_frame, text="Export Image", bg="white", command=self.__export_image)
        export_button.pack(pady=15, side=TOP)

        self.__root.mainloop()


