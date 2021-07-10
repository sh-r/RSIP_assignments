clc 
clear all
close all

x= imread('birds.jpg');
imshow(x)
title('original')
size(x)

bw= im2bw(x);
% convert image to black and white
figure,imshow(bw)
title('black and white')
size(bw)

[l,x]= bwlabel(bw,4);
% where l is the labels (label matrix)
% where x= number of objects found in the image
x

[m,y]= bwlabel(bw,8);
y

%refer workspace window for the info

bwc= imcomplement(bw);
figure, imshow(bwc)
title('complement')
[n,z]= bwlabel(bw,4);
z
[p,q]= bwlabel(bw,8);
q