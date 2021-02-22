from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from wsgiref.util import FileWrapper
from gallery import settings

from .models import Gallery, CategoryTable
from .forms import *

import os
  
'''
Created By Ashwini G M on 21 Feb 2021
'''


'''
This function is used to display main page
'''
def image_view(request): 
  
    # Collect the media path
    media_path = settings.MEDIA_ROOT

    # Replace the file seperator with forward slash to view in gallery
    path = media_path.replace(os.sep, '/') + '/images/'

    # Store the final path here
    images = []
    
    if request.method == 'POST':
        # Collect the values of gallery form 
        form = GalleryForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 

            # Save the path in category table
            img = form.cleaned_data['image'].name
            savepath = CategoryTable(category = form.cleaned_data['category'],path =os.path.join(path,img))
            savepath.save()
            
     
    form = GalleryForm() 

    # List all the image files in the media path
    imgs = os.listdir(media_path + '/images/')

    # Collect all the image paths
    for img in imgs:
        img = os.path.join(path , img)
        if 'jpg|png' in img:
            images.append(img)

    
    return render(request, 'index.html', {'form' : form, 'images':images}) 

'''
This function is used to display filtered images
'''
def SearchPage(request):
    form = GalleryForm() 

    # Get the category we need to search
    srh = request.GET['category']

    # Get the list of image paths which matches the above category
    search_results = CategoryTable.objects.values_list('path', flat=True).filter(category__icontains=srh)       

    return render(request, 'index.html', {'form' : form,'images': search_results})


'''
The below code is used to convert from image format to byte format
'''
class FixedFileWrapper(FileWrapper):
    def __iter__(self):
        self.filelike.seek(0)
        return self

def loadFileInByte(request, path):
    response = HttpResponse(FixedFileWrapper(open(path,'rb')), content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=%s' %os.path.basename(path)
    response['Content-Length'] = os.path.getsize(path)

    return response
  
  