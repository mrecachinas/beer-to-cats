cellSize = 8;
uiopen('/path/to/image',1);
im = im2single(image);
hog = vl_hog(im, cellSize, 'verbose');
imhog = vl_hog('render', hog, 'verbose');
clf; imagesc(imhog); colormap gray;