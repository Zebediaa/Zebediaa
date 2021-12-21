clear variables
close all

load("onde_grav.mat")

Fe = 4096


Nx = length(x);
nx = (0:Nx-1);

Nu = length(u);
nu = (0:Nu-1)

Dt = (1/Fe);

tx = nx*Dt;
tu = nu*Dt;

##PART 1  

##figure
##plot(tx,x)
##xlabel("Temps")
##ylabel("Signal")

##figure
##plot(tu,u)
##xlabel("Temps")
##ylabel("Signal th?orique")


##PART 2

##h = conj(flip(u));
##c = conv (x,h,"same");

##figure
##plot(tx,c)
##xlabel("Temps")
##ylabel("Signal th?orique")


##Part 3

##win = hanning(Nx/4)
##[dsp,f] = dspwelch(x,win,Nx,Fe);

##figure
##semilogy(f,dsp)
##xlabel("f")
##ylabel("PHI-B")


##Part 4 

##Xf = fft(x)

##H = (exp(-1j*2*3.14*f*2)).*conj(Xf)./(dsp)

##Yf = Xf.*H
##y = ifft(Yf)


##figure
##plot(tx,y)
##xlabel("temps")
##ylabel("signal")

##Part5

##fband = [43,300];
##[b,a] = butter(4,[2*fband(1)/Fe,2*fband(2)/Fe]);
##x_wband = filtfilt(b,a,y);



##figure
##plot(tx,x_wband)
##xlabel("temps")
##ylabel("signal");

publish('tp3rendusignal.m','pdf');

