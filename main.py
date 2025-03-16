import imageio.v3 as iio
# add yout image file names in the list
files =[
    'im0.jpg',
    'im1.jpg',
    'im2.jpg',
    'im3.jpg',
    'im4.jpg',
    'im5.jpg',
    'im6.jpg',
    'im7.jpg',
    'im8.jpg',
    'im9.jpg',
    'im10.jpg'
]

images =[]

for image in files:
    images.append(iio.imread(image))

iio.imwrite('Gif_name.gif',
images, duration = 100, loop =0)