close all hidden
clear all
clc
cd
set(gca,'FontSize',18)
set(gca,'LineWidth',2)
%% Place variables for eqn
V0 = 1;
u0 = 0.2;
delta = 0.5;
H = 0.4;
beta = 5.42;
eta = 2;
% Set the parameters for the differential equation, namely: b, r, q
b = 3/(V0 - u0)^4 + (delta^2/12)/((V0 - u0)^3) + 0.5/(V0 - u0)^3;
r = delta*(H^2)/(8*beta) + 0.5*(V0 - u0)^3 + H^2/(8*(V0 - u0));
q = 0.5*eta;


N = 256;
x = linspace(-10,50,N);
delta_x = x(2) - x(1);
delta_k = 2*pi/(N*delta_x);

k = [0:delta_k:(N/2-1)*delta_k,0,-(N/2-1)*delta_k:delta_k:-delta_k];
t=0;
%c_1=16;
%c_2 = 8;

%u = 1/2*c_1*(sech(sqrt(c_1)*(x+8)/2)).^2 + 1/2*c_2*(sech(sqrt(c_2)*(x+1)/2)).^2;
u = sqrt(6*r/b)*(1 + tanh(x));% - 8*r*t));
mkdir kdvb_sols;
cd kdvb_sols;
%name = 'two_soliton.gif';
%eval(['delete ',name])

delta_t = 0.4/N^2;
plot(x,u,'LineWidth',2)
axis([-10 50 -10 10])
xlabel('x')
ylabel('u')
text(6,9,['t = ',num2str(t,'%1.2f')],'FontSize',18)
drawnow
%gif_add_frame(gcf,name,2);
%drawnow

tmax = 4; nplt = floor((1/100)/delta_t); nmax = round(tmax/delta_t);
udata = u.'; tdata = 0;
U = fft(u);
j = 1;
for n = 1:nmax
    t = n*delta_t;
    % first do the linear part
    U = U.*exp(1i*k.^3*delta_t);
    
    % then solve the nonlinear part
    
    U = U  - (3i*k*delta_t).*fft((real(ifft(U))).^2);
    
    if mod(n,nplt) == 0
        u = real(ifft(U));
        udata = [udata u.']; tdata = [tdata t];
        if mod(n,4*nplt) == 0
            plot(x,u,'LineWidth',2)
            axis([-10 50 -10 10])
            xlabel('x')
            ylabel('u')
            text(6,9,['t = ',num2str(t,'%1.2f')],'FontSize',18)
            fname = strcat("soliton_",num2str(j, '%d'));
            print(fname, '-djpeg');
            drawnow
            j=j+1;
            %gif_add_frame(gcf,name,2);
        end
    end
end

figure

waterfall(x,tdata(1:4:end),udata(:,1:4:end)')
colormap(1e-6*[1 1 1]); view(-20,25)
xlabel x, ylabel t, axis([-10 10 0 tmax 0 10]), grid off
zlabel('u')
set(gca,'ztick',[0 10]), pbaspect([1 1 .13])
print -djpeg two_soliton