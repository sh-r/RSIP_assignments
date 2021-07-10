x=imread('home1.png');
x=rgb2gray(x);
[M,N]=size(x);
y=fft2(x);

u = 0:(M-1); 
v = 0:(N-1); 
idx = find(u > M/2); 
u(idx) = u(idx)- M; 
idy = find(v > N/2); 
v(idy) = v(idy)- N; 
[V, U] = meshgrid(v, u);

D0=47; 
D = sqrt(U.^2 + V.^2);
H =( double(D <=D0));

%IPLF
IPLF=real(ifft2(H.*y));

%GLPF
Hg = exp(-(D.^2)./(2*(D0^2)));
GLPF=real(ifft2(Hg.*y));

% High pass filter 
Hp=1-H; 
HPF=real(ifft2(Hp.*y));

%subplot(2,2,1);
figure
imshow(x)
%subplot(2,2,2);
figure
imshow(IPLF,[])
%subplot(2,2,3);
figure
imshow(GLPF,[])
%subplot(2,2,4);
figure
imshow(HPF,[])
