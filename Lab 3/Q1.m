clc
clear all 
close all

x= imread('rose.jpg')
imshow(x)
info= imfinfo('rose.jpg')
size(x)

R=x(:,:,1);
G=x(:,:,2);
B=x(:,:,3);

subplot(2,2,1)
imshow(x)
title('original')

subplot(2,2,2)
imshow(R)
title('R')

subplot(2,2,3)
imshow(G)
title('G')

subplot(2,2,4)
imshow(B)
title('B')
