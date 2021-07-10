clc 
clear all
close all

x= imread('lena.tif');
[rows, columns, numberOfColorChannels] = size(x)
subplot(1,2,1)
imshow(x)
title('original')
size(x);

mask = imread('lena.tif');
[rowsm, columnsm, numberOfColorChannelsm] = size(mask)
mask = mask(:,:,1) > 128; % Convert to binary.
subplot(1,2,2)
imshow(mask)
title('binary image')

if rows ~= rowsm || columns ~= columnsm
	% Resize mask to match image.
	mask = imresize(mask, [rows, columns], 'Nearest');
end


% Mask the image using bsxfun() function to multiply the mask by each channel individually.  Works for gray scale as well as RGB Color images.
maskedRgbImage = bsxfun(@times, im2bw(x), cast(mask, 'like', im2bw(x)));
% Display the final masked image.
figure
imshow(maskedRgbImage, []);
title('Masked image')

and= im2bw(x) & mask;
figure
imshow(and)
title('& operation')

or= im2bw(x) | mask;
figure
imshow(or)
title('| operation')

