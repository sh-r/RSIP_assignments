clc 
clear all
close all

x= imread('cell_blood.JPG')
imshow(x)
title('original')
size(x)

bw= im2bw(x);
% convert image to black and white
subplot(2,1,1)
imshow(bw)
title('black and white')
size(bw)

grayscale= rgb2gray(x);
subplot(2,1,2)
imshow(grayscale)
title('grayscale')
size(grayscale)

bwc= imcomplement(bw);
figure
imshow(bwc)
title('complement')

CC4= bwconncomp(bwc,4);
CC8= bwconncomp(bwc,8);
