clc 
clear all
close all

x= imread('imadd1.jpg');
subplot(2,3,2)
imshow(x)
title('imadd1')
size(x)

y= imread('imadd2.jpg');
subplot(2,3,4)
imshow(y)
title('imadd2')
size(y)

y1=imresize(y,[225 300]); 
subplot(2,3,6)
imshow(y1)
title('resized imadd2')
size(y1)

z= imadd(x,y1);
figure
imshow(z)
title('added image')

w= im2bw(x)|im2bw(y1);    %arithmetic logical operators work only with bw image
figure
imshow(w)
title('merged image')
